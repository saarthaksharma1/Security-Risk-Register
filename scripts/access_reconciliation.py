
from pathlib import Path
import argparse

import pandas as pd


# Locate the project root regardless of where the script is run.
PROJECT_ROOT = Path(__file__).resolve().parents[1]

HR_FILE = PROJECT_ROOT / "evidence/F-001/hr_termination_records.csv"


def reconcile_access(access_file, output_file):
    # Step 1: Read the simulated evidence.
    hr = pd.read_csv(HR_FILE, dtype=str)
    access = pd.read_csv(access_file, dtype=str)

    # Step 2: Confirm the required columns are available.
    hr_columns = {"employee_id", "employment_status", "termination_date"}
    access_columns = {
        "employee_id", "application", "account_status", "export_date"
    }

    if not hr_columns.issubset(hr.columns):
        raise ValueError("HR file is missing required columns.")

    if not access_columns.issubset(access.columns):
        raise ValueError("Access file is missing required columns.")

    # Each employee should have one HR record.
    if hr["employee_id"].isna().any() or hr["employee_id"].duplicated().any():
        raise ValueError("HR file has missing or duplicate employee IDs.")

    # Check for missing required HR values.
    for column in ["employee_id", "employment_status"]:
        if hr[column].isna().any() or hr[column].str.strip().eq("").any():
            raise ValueError(f"Missing HR value: {column}")

    # Check for missing required application values.
    for column in [
        "employee_id", "application", "account_status", "export_date"
    ]:
        if (
            access[column].isna().any()
            or access[column].str.strip().eq("").any()
        ):
            raise ValueError(f"Missing application value: {column}")

    # Reject unrecognized employment statuses.
    valid_hr_statuses = {"active", "terminated"}

    if not hr["employment_status"].str.strip().str.lower().isin(
        valid_hr_statuses
    ).all():
        raise ValueError("Unrecognized employment status detected.")

    # Reject unrecognized application account statuses.
    valid_account_statuses = {"active", "disabled"}

    if not access["account_status"].str.strip().str.lower().isin(
        valid_account_statuses
    ).all():
        raise ValueError("Unrecognized account status detected.")

    # Detect duplicate employee/application combinations.
    if access.duplicated(
        subset=["employee_id", "application"]
    ).any():
        raise ValueError("Duplicate application account detected.")

    # Step 3: Match application accounts to HR records.
    merged = access.merge(
        hr[["employee_id", "employment_status", "termination_date"]],
        on="employee_id",
        how="left",
        validate="many_to_one",
    )

    # Do not silently ignore accounts with missing HR records.
    if merged["employment_status"].isna().any():
        raise ValueError("Some application accounts have no matching HR record.")

    if merged["account_status"].isna().any():
        raise ValueError("Some application accounts have no account status.")

    # Step 4: Identify terminated employees with active accounts.
    terminated = (
        merged["employment_status"].str.strip().str.lower() == "terminated"
    )
    active_access = (
        merged["account_status"].str.strip().str.lower() == "active"
    )

    exceptions = merged.loc[terminated & active_access].copy()

    # Step 5: Save an exception report.
    output_file.parent.mkdir(parents=True, exist_ok=True)

    exceptions.to_csv(
        output_file,
        columns=[
            "employee_id",
            "application",
            "account_status",
            "export_date",
            "employment_status",
            "termination_date",
        ],
        index=False,
    )

    print(f"Application accounts reviewed: {len(access)}")
    print(f"Access exceptions identified: {len(exceptions)}")
    print(f"Exception report saved: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Identify terminated employees with active access."
    )
    parser.add_argument("--access", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    access_path = PROJECT_ROOT / args.access
    output_path = PROJECT_ROOT / args.output

    reconcile_access(access_path, output_path)
