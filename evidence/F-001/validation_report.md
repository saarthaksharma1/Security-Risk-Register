
# F-001 — Remediation Validation Report

> SIMULATED GRC PORTFOLIO EXERCISE — All employees, systems, actions, and evidence are fictional.

## 1. Finding Overview

- **Finding ID:** F-001
- **Risk ID:** R-001
- **Control ID:** AC-02
- **Control Name:** Terminated User Access Removal
- **Risk Rating:** High
- **Control Owner:** IT Operations
- **Validation Date:** 2026-11-01 (simulated)
- **Finding Status:** Open — Pending Closure Validation

## 2. Original Finding

Two terminated employees retained active access to business applications after their employment ended.

This control weakness could allow unauthorized access to organizational systems and information.

The original remediation target date was October 30, 2026.

## 3. Remediation Objective

Verify that:
1. Access for the two terminated employees has been disabled.
2. Active employees retain appropriate access.
3. A recurring HR-to-application access reconciliation process has been established.
4. Supporting evidence is documented and available for review.

## 4. Evidence Reviewed

| Evidence File | Purpose |
|---|---|
| hr_termination_records.csv | Identify terminated and active employees |
| application_access_export.csv | Establish original access conditions |
| remediation_access_export.csv | Verify simulated post-remediation account statuses |
| remediation_action_log.csv | Document corrective actions and responsible owner |
| weekly_access_reconciliation.csv | Review one simulated HR-to-access reconciliation |

## 5. Validation Procedures

1. Review HR records to identify terminated employees.
2. Match employee IDs against the original application access export.
3. Identify terminated employees with active accounts.
4. Compare original and remediation exports.
5. Verify that the two identified accounts now show Disabled.
6. Review the reconciliation record for remaining exceptions.
7. Assess whether available evidence demonstrates ongoing weekly control operation.

## 6. Testing Results

| Test | Result | Observation |
|---|---|---|
| Identify terminated employees | Pass | E101 and E102 identified |
| Identify original access exceptions | Pass | Two active accounts associated with terminated employees |
| Verify account remediation | Pass | E101 and E102 show Disabled on November 1 |
| Check active employee accounts | Pass | E103 and E104 remain Active |
| Review sample reconciliation | Pass | Four records reviewed; zero exceptions |
| Verify ongoing weekly operation | Pending | Only one reconciliation record available |

## 7. Validation Conclusion

The simulated post-remediation access export indicates that both originally identified terminated-user accounts have been disabled.

The sample reconciliation contains no active-access exceptions for the terminated employees reviewed.

However, one reconciliation does not establish consistent weekly control operation, and the sample does not independently prove the completeness of all application accounts or the timing of access removal.

**Validation Outcome:** Immediate account remediation passed the simulated sample test. Overall finding closure remains pending.

## 8. Outstanding Evidence and Actions

- Document the recurring reconciliation procedure and review frequency.
- Assign responsibility for performing and approving each review.
- Retain additional weekly reconciliation records and reviewer sign-offs.
- Confirm the population covers all relevant terminated users and applications.
- Retain verifiable account-disabling timestamps or audit logs where available.

## 9. Closure Recommendation

**Recommendation: Keep F-001 Open pending additional control validation.**

Do not record a successful final closure validation or an actual closure date until the required evidence has been reviewed.

The original October 30 remediation target was missed; closure should not erase that historical fact.

## 10. Assessment Limitations

This report documents a fictional security assessment created for portfolio demonstration. CSV files represent synthetic sample evidence, not exports from live enterprise systems. No real employee accounts were accessed, modified, or disabled.
