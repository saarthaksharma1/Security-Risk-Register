# F-001 Automated Access Reconciliation Summary

> SIMULATED GRC PORTFOLIO EXERCISE

## Results

| Metric | Baseline | Post-Remediation |
|---|---:|---:|
| Application accounts reviewed | 4 | 4 |
| Terminated-user active-access exceptions | 2 | 0 |

## Sample Coverage Check

Matched across the two sample exports

This check compares account identifiers across the two provided
exports. It does not verify completeness of the enterprise account
population.

## Assessment

The original export identified 2 access
exceptions. The post-remediation export identified
0 exceptions.

Finding F-001 remains In Progress. Additional evidence is
required to establish recurring weekly control effectiveness.

## Evidence References

- evidence/F-001/hr_termination_records.csv
- evidence/F-001/application_access_export.csv
- evidence/F-001/remediation_access_export.csv
- outputs/baseline_exceptions.csv
- outputs/remediation_exceptions.csv

## Limitations

All evidence is synthetic. Results reflect only the supplied sample.
No live systems were accessed or modified.
