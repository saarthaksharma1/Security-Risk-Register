
from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase
from unittest.mock import patch

import pandas as pd

from scripts.access_reconciliation import reconcile_access


ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = ROOT / "evidence" / "F-001"


class TestAccessReconciliation(TestCase):

    def setUp(self):
        self.temp_dir = TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)

        self.output = Path(self.temp_dir.name) / "exceptions.csv"

    def test_baseline_detects_two_exceptions(self):
        access_file = EVIDENCE / "application_access_export.csv"

        reconcile_access(access_file, self.output)

        result = pd.read_csv(self.output)

        self.assertEqual(len(result), 2)
        self.assertEqual(
            set(result["employee_id"]),
            {"E101", "E102"}
        )

    def test_remediation_detects_zero_exceptions(self):
        access_file = EVIDENCE / "remediation_access_export.csv"

        reconcile_access(access_file, self.output)

        result = pd.read_csv(self.output)

        self.assertEqual(len(result), 0)

    def test_unmatched_employee_is_rejected(self):
        access_file = Path(self.temp_dir.name) / "unknown_user.csv"

        pd.DataFrame([{
            "employee_id": "E999",
            "application": "Jira",
            "account_status": "Active",
            "export_date": "2026-11-01"
        }]).to_csv(access_file, index=False)

        with self.assertRaises(ValueError):
            reconcile_access(access_file, self.output)

    def test_duplicate_hr_records_are_rejected(self):
        hr_file = Path(self.temp_dir.name) / "duplicate_hr.csv"

        pd.DataFrame([
            {
                "employee_id": "E101",
                "employment_status": "Terminated",
                "termination_date": "2026-09-18"
            },
            {
                "employee_id": "E101",
                "employment_status": "Terminated",
                "termination_date": "2026-09-18"
            }
        ]).to_csv(hr_file, index=False)

        with patch("scripts.access_reconciliation.HR_FILE", hr_file):
            with self.assertRaises(ValueError):
                reconcile_access(
                    EVIDENCE / "application_access_export.csv",
                    self.output
                )
    
    def test_unrecognized_account_status_is_rejected(self):
        access = pd.read_csv(
            EVIDENCE / "application_access_export.csv", dtype=str
        )

        access.loc[0, "account_status"] = "Unknown"

        test_file = Path(self.temp_dir.name) / "unknown_status.csv"
        access.to_csv(test_file, index=False)

        with self.assertRaises(ValueError):
            reconcile_access(test_file, self.output)

    def test_missing_employee_id_is_rejected(self):
        access = pd.read_csv(
            EVIDENCE / "application_access_export.csv", dtype=str
        )

        access.loc[0, "employee_id"] = ""

        test_file = Path(self.temp_dir.name) / "missing_id.csv"
        access.to_csv(test_file, index=False)

        with self.assertRaises(ValueError):
            reconcile_access(test_file, self.output)

    def test_duplicate_application_account_is_rejected(self):
        access = pd.read_csv(
            EVIDENCE / "application_access_export.csv", dtype=str
        )

        access = pd.concat(
            [access, access.iloc[[0]]],
            ignore_index=True
        )

        test_file = Path(self.temp_dir.name) / "duplicate_account.csv"
        access.to_csv(test_file, index=False)

        with self.assertRaises(ValueError):
            reconcile_access(test_file, self.output)

