# Security Risk Assessment & GRC Automation

### Cedar Ridge Services | Simulated Small Business Security Assessment

## Overview

Cedar Ridge Services is a fictional IT services company with approximately 50 employees. The company relies on Microsoft 365, Jira, GitHub, Confluence, and cloud-based systems for its daily operations.

As the business grows, its small IT team faces challenges maintaining consistent security procedures, tracking vulnerabilities, managing user access, and documenting remediation efforts.

I developed this project to simulate an internal security assessment for the company, focusing on identifying control weaknesses, evaluating risk, and establishing a structured remediation process.

*All company information, employee records, and assessment evidence are fictional.*

## Security Assessment

The assessment reviews **12 security controls** using concepts from NIST SP 800-53, focusing on access management, authentication, vulnerability management, audit logging, change management, incident response, and business continuity.

The project includes:

- A control matrix documenting security requirements, testing procedures, and findings.
- A risk register evaluating inherent and residual risk using a 5×5 likelihood-and-impact matrix.
- A POA&M tracker for remediation ownership, deadlines, evidence requirements, and validation status.
- An Excel dashboard summarizing findings and remediation progress.
- An executive summary outlining risks requiring management attention.

### Assessment Results

| Metric | Result |
|---|---:|
| Controls Assessed | 12 |
| Security Findings | 9 |
| High Residual Risks | 4 |
| Findings In Progress | 2 |
| Overdue Findings | 4 |

Results reflect the simulated assessment as of November 1, 2026.

## Remediation Case Study: Employee Offboarding

One finding involved two terminated employees who retained active access to company applications.

I simulated the remediation process by comparing HR termination records with application access exports, documenting corrective actions, and reviewing post-remediation evidence.

Both identified accounts were disabled in the simulated follow-up. However, the finding remains open pending additional evidence of consistent weekly access reconciliation.

This exercise demonstrates the importance of validating corrective actions rather than closing findings solely because remediation was reported as completed.

## Python Automation

To reduce manual reconciliation work, I developed two Python scripts using Pandas.

**Access Reconciliation:** Matches employee records against application access exports, identifies terminated users with active accounts, and generates exception reports.

**Automated Reporting:** Compares baseline and post-remediation results and generates CSV and Markdown summaries for review.

| Reconciliation Result | Before | After |
|---|---:|---:|
| Accounts Reviewed | 4 | 4 |
| Access Exceptions | 2 | 0 |

The automation includes seven unit tests covering expected results, missing identifiers, unmatched records, duplicate entries, and invalid account statuses.

## Tools & Technologies

Python, Pandas, Microsoft Excel, Git, GitHub, VS Code, CSV, Markdown, and Python unittest.

## Running the Project

Install the dependencies:

`python -m pip install -r requirements.txt`

Run the baseline reconciliation:

`python scripts/access_reconciliation.py --access evidence/F-001/application_access_export.csv --output outputs/baseline_exceptions.csv`

Run the post-remediation reconciliation:

`python scripts/access_reconciliation.py --access evidence/F-001/remediation_access_export.csv --output outputs/remediation_exceptions.csv`

Generate the summary:

`python scripts/generate_access_summary.py`

Run the tests:

`python -m unittest discover -s tests -p "test_*.py" -v`

## Project Scope

This project represents a focused security assessment for a fictional small business, not a comprehensive audit or compliance certification.

The evidence uses synthetic records, and the automation evaluates only the supplied sample. Results do not establish complete enterprise account coverage or ongoing control effectiveness.