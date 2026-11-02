
# AC-02 — Weekly User Access Reconciliation Procedure

> SIMULATED GRC PORTFOLIO EXERCISE — This procedure represents a fictional control design.

## 1. Purpose

Ensure that terminated employees do not retain unauthorized access to organizational applications.

## 2. Control Information

- Control ID: AC-02
- Control Name: Terminated User Access Removal
- Control Owner: IT Operations
- Review Frequency: Weekly
- Review Performer: IT Operations Analyst
- Review Approver: IT Security
- Related Finding: F-001
- Related Risk: R-001

## 3. Scope

The reconciliation covers terminated employees and their assigned accounts across in-scope applications, including Jira and GitHub.

## 4. Procedure

### Step 1 — Obtain HR Records

Obtain the latest authorized HR employee status and termination records.

Confirm the reporting period and completeness of the HR termination population.

### Step 2 — Obtain Application Access Reports

Export the account inventory from each in-scope application.

Record the export dates and confirm that relevant employee accounts are included.

### Step 3 — Reconcile Records

Match HR records to application accounts using the employee ID or a documented identity mapping.

Identify:
- Terminated employees with active application access.
- Missing or unmatched employee identifiers.
- Accounts with unclear ownership.
- Incomplete or missing application exports.

### Step 4 — Investigate Exceptions

For every exception:

1. Document the affected employee and application.
2. Notify IT Operations.
3. Create or reference a remediation ticket.
4. Escalate according to the organization's access removal requirements.

### Step 5 — Verify Remediation

Review updated application access evidence and relevant audit logs.

Confirm the account was disabled and record the effective disabling timestamp where available.

### Step 6 — Document Review Results

Record:
- Review date.
- Applications and employee population reviewed.
- Exceptions identified.
- Remediation actions and evidence.
- Outstanding issues.
- Reviewer name and approval decision.

### Step 7 — Obtain Approval

IT Security reviews the reconciliation results and records approval or requests additional corrective actions.

## 5. Expected Control Outcome

Terminated employees should not retain active application access beyond the organization's defined offboarding requirements.

Any exceptions should be tracked, investigated, and resolved.

## 6. Evidence Retention

Maintain dated HR records, application exports, reconciliation results, remediation tickets, and reviewer approvals in the designated evidence repository according to the organization's retention policy.

## 7. Testing and Closure Criteria

Finding F-001 may be recommended for closure only when:

1. The original two account access exceptions are resolved.
2. Supporting remediation evidence is reviewed.
3. The reconciliation procedure is approved.
4. Additional weekly reconciliation records demonstrate operation over the selected testing period.
5. Reviewer sign-offs and exception handling are documented.
6. The required population and application coverage are verified.

## 8. Current Validation Status

As of the simulated November 1, 2026 assessment:

- Original access exceptions: 2
- Remaining exceptions in the post-remediation sample: 0
- Weekly reconciliation samples reviewed: 1
- Recurring operational effectiveness: Not yet established
- Finding F-001: Open — Pending further validation

This procedure is a proposed control design for a simulated environment, not evidence that an organization has implemented or approved it.
