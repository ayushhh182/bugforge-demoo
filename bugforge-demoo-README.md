# 🐞 BugForge AI

## Autonomous Bug-to-PR Resolution Agent

**BugForge AI** is an autonomous software debugging agent built for the **“Agents That Act”** challenge.

Instead of only suggesting a fix, BugForge can investigate a real bug, inspect a GitHub repository, reproduce the issue in an isolated sandbox, identify the root cause, generate a minimal patch, verify the patch, and — after human approval — create a GitHub Pull Request.

---

## 🚀 What BugForge Does

```text
Bug Report
    ↓
Repository Inspection
    ↓
Bug Reproduction
    ↓
Root Cause Analysis
    ↓
Minimal Patch
    ↓
Sandbox Verification
    ↓
Human Approval
    ↓
GitHub Branch
    ↓
Pull Request
    ↓
Final Verification
```

The core principle is:

> **Investigate → Act → Verify → Ask for Approval → Act on GitHub**

---

## 🎯 Problem

Software teams spend a lot of time manually handling repetitive debugging work:

- Understanding bug reports
- Finding relevant source files
- Reproducing failures
- Identifying root causes
- Writing patches
- Running tests
- Creating branches and Pull Requests
- Preparing customer responses

BugForge automates this workflow while keeping **human approval before external repository changes**.

---

## 💡 Solution

BugForge combines an AI reasoning agent with GitHub tools and an isolated execution environment.

### The agent can:

- 🔎 Inspect repository files
- 🧪 Reproduce reported bugs
- 🧠 Analyze root causes
- 🛠️ Generate minimal patches
- ✅ Verify fixes using actual execution
- 👤 Pause for human approval
- 🔀 Create branches and Pull Requests
- 💬 Draft customer responses
- 🛡️ Report `COULD NOT REPRODUCE` instead of inventing results

---

# 🔬 Demonstrated Bug

This repository contains a small authentication example used to demonstrate BugForge's debugging workflow.

### Original implementation

```python
USERS = {
    "anubhav@gmail.com": {
        "name": "Anubhav"
    }
}

def login(email):
    return USERS[email]
```

### Reported issue

A user entering:

```text
ANUBHAV@GMAIL.COM
```

could not log in.

The original implementation attempted to directly use the supplied email as a dictionary key, resulting in:

```text
KeyError: 'ANUBHAV@GMAIL.COM'
```

---

## 🧠 Root Cause

The email address was used without case normalization.

The stored key was:

```text
anubhav@gmail.com
```

while the input could be:

```text
ANUBHAV@GMAIL.COM
```

Python dictionary lookup treats these as different strings.

---

## 🛠️ BugForge's Minimal Fix

BugForge identified the smallest required change:

```diff
 def login(email):
-    return USERS[email]
+    return USERS[email.lower()]
```

Only `auth.py` needed to be modified.

---

# 🧪 Verification

The final patch was checked against the Pull Request commit in an isolated sandbox.

The following assertions were executed:

```python
assert login("ANUBHAV@GMAIL.COM")["name"] == "Anubhav"
assert login("anubhav@gmail.com")["name"] == "Anubhav"
```

### Result

```text
✅ ASSERTIONS_PASSED
```

This demonstrates that both uppercase and lowercase email inputs are handled correctly.

---

# 🔐 Human-in-the-Loop Safety

BugForge does not blindly make external changes.

Before modifying the real repository, the agent stops for approval.

### Approval is required before:

- Creating a GitHub branch
- Modifying repository files
- Creating a Pull Request
- Sending a customer response

### Verification rule

> **No execution evidence = No verified success.**

If the sandbox cannot execute the required test, BugForge reports that the fix is **not verified**.

If the issue cannot be reproduced, BugForge reports:

```text
COULD NOT REPRODUCE
```

instead of fabricating a result.

---

# 🏗️ Architecture

```text
                  ┌──────────────────┐
                  │    Bug Report    │
                  └────────┬─────────┘
                           ↓
                  ┌──────────────────┐
                  │   BugForge AI    │
                  │      Agent       │
                  └────────┬─────────┘
                           │
             ┌─────────────┼─────────────┐
             ↓             ↓             ↓
       ┌──────────┐  ┌──────────┐  ┌────────────┐
       │ GitHub   │  │ Daytona  │  │ AI         │
       │ MCP      │  │ Sandbox  │  │ Reasoning  │
       └────┬─────┘  └────┬─────┘  └────────────┘
            │             │
            └──────┬──────┘
                   ↓
             Root Cause
                   ↓
             Minimal Patch
                   ↓
             Test & Verify
                   ↓
             Human Approval
                   ↓
             GitHub Branch
                   ↓
             Pull Request
```

---

# 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| **TrueForge / TrueFoundry** | AI agent orchestration |
| **GPT-5.6** | Reasoning and code analysis |
| **GitHub MCP** | Repository inspection and GitHub actions |
| **Daytona** | Isolated code execution and testing |
| **GitHub** | Source control, branches and Pull Requests |
| **Python** | Demonstration application |
| **Pytest / Python assertions** | Verification |

---

# 📁 Repository Structure

```text
bugforge-demoo/
│
├── auth.py
│   └── Authentication logic and bug demonstration
│
├── testauth.py
│   └── Regression tests
│
└── README.md
    └── Project documentation
```

---

# 🔄 Agent Workflow

### 1. Receive
Read and understand the reported bug.

### 2. Inspect
Identify the repository and relevant source files.

### 3. Reproduce
Execute the reported scenario in the isolated Daytona sandbox.

### 4. Diagnose
Analyze the error and identify the root cause.

### 5. Patch
Generate the smallest reasonable code change.

### 6. Verify
Run the relevant tests or assertions in the sandbox.

### 7. Approve
Stop and request human approval before external GitHub changes.

### 8. Act
Create the approved branch, commit the patch and Pull Request.

### 9. Confirm
Verify the final patch and report evidence.

---

# 📌 Demonstrated Pull Request

The working demonstration created:

- **Repository:** `ayushhh182/bugforge-demoo`
- **Pull Request:** `#1`
- **Changed file:** `auth.py`
- **Commit:** `fa433e69848ffd0d124bcf98b63b1b9574410a25`
- **Verification:** `ASSERTIONS_PASSED`

The Pull Request contains the minimal one-line normalization fix.

---

# 🏆 Why This Project Matters

BugForge demonstrates an AI agent that can move beyond **code generation** into **real software-engineering action**.

Instead of:

```text
User → AI → Code Suggestion
```

BugForge enables:

```text
User
 ↓
Bug Ticket
 ↓
AI Investigation
 ↓
Real Reproduction
 ↓
Root Cause
 ↓
Patch
 ↓
Real Verification
 ↓
Human Approval
 ↓
GitHub Pull Request
```

This makes the agent useful for real-world developer support and ticket-resolution workflows.

---

# 🔮 Future Scope

- Jira integration
- Linear integration
- Zendesk integration
- Automated CI/CD verification
- Multi-repository debugging
- Intelligent test discovery
- AWS-based logs and monitoring
- Bug analytics dashboard
- Approval dashboard
- Automated customer-response review

---

# 🏁 Hackathon Demo

### Demo Scenario

> **“A customer reports that login fails when their email is entered in uppercase.”**

BugForge:

1. Inspects the repository
2. Finds the authentication logic
3. Reproduces the `KeyError`
4. Identifies missing case normalization
5. Generates the minimal fix
6. Tests the fix in an isolated sandbox
7. Requests human approval
8. Creates a GitHub branch
9. Creates the Pull Request
10. Verifies the final patch

### Final Result

```text
Bug identified       ✅
Bug reproduced       ✅
Root cause found     ✅
Minimal patch        ✅
Sandbox verified     ✅
Human approval       ✅
GitHub PR created    ✅
Assertions passed    ✅
Customer response    ⏸️ Human controlled
```

---

## 👨‍💻 Project

**BugForge AI**

**Challenge:** Agents That Act

**Built with:** TrueForge + GPT-5.6 + GitHub MCP + Daytona

> **From bug report to verified Pull Request — with evidence and human control.**

---

## 📄 License

This repository is a hackathon prototype.
