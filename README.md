# 🚀 Configurable Workflow Decision Platform

## 📌 Overview

This project is a **Resilient Workflow Decision System** designed to handle real-world business workflows with flexibility, auditability, and robustness.

The system processes incoming requests, evaluates configurable rules, executes workflows, maintains state, logs decisions, and handles failures with retry and idempotency support.

---

## 🎯 Objective

To build a **generic, configurable decision platform** that can support multiple business use cases without major code changes.

---

## 💡 Supported Use Cases

* Loan / Application Approval
* Claim Processing
* Employee Onboarding
* Vendor Approval
* Document Verification

---

## ⚙️ Core Features

### ✅ Input Handling

* Accepts structured JSON input
* Validates schema

### ✅ Rules Engine

* Config-driven rules (JSON-based)
* Supports:

  * Mandatory checks
  * Threshold checks
  * Conditional branching

### ✅ Workflow Engine

* Multi-stage workflow execution
* States:

  * `APPROVED`
  * `REJECT`
  * `MANUAL_REVIEW`
  * `RETRY`

### ✅ State Management

* Tracks request lifecycle
* Stores current state and history

### ✅ Audit Logging (Explainability)

* Logs:

  * Rules executed
  * Pass/Fail status
  * Decision reasoning

### ✅ Failure Handling

* Simulates external dependency failures
* Retry mechanism
* Graceful error handling

### ✅ Idempotency

* Prevents duplicate processing
* Same request returns same result

### ✅ Configurability

* Rules and workflows defined in JSON
* No need to change core code

---

## 🏗️ System Architecture

```
[Architecture Diagram](images/architecture.png)
```

---

## 📁 Project Structure

```
workflow-system/
│
├── app.py
├── database.py
├── models.py
├── workflow_engine.py
├── rules_engine.py
├── utils.py
│
├── config/
│   ├── workflow.json
│   ├── rules.json
│
├── requirements.txt
```

---

## 🛠️ Tech Stack

* **Backend**: FastAPI (Python)
* **Database**: SQLite (SQLAlchemy ORM)
* **Config**: JSON-based rules & workflows

---

## ▶️ How to Run

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Start Server

```bash
uvicorn app:app --reload
```

### 3. Open Swagger UI

```
http://127.0.0.1:8000/docs
```

---

## 📥 Sample API Request

### Endpoint:

`POST /process`

```json
{
  "request_id": "abc123",
  "type": "loan",
  "data": {
    "salary": 40000,
    "credit_score": 700
  }
}
```

---

## 📤 Sample Response

```json
{
  "status": "APPROVED",
  "audit": [
    {
      "rule": "salary_check",
      "result": "PASS"
    },
    {
      "rule": "credit_check",
      "result": "PASS"
    }
  ]
}
```

---

## 🔁 Failure & Retry Example

* If external dependency fails:

```json
{
  "status": "RETRY",
  "error": "External API Failure"
}
```

---

## 🔄 Idempotency Example

Sending same request again:

```json
{
  "status": "APPROVED",
  "message": "Duplicate request"
}
```

---

## 🧪 Test Scenarios Covered

* ✅ Happy Path
* ❌ Invalid Input
* 🔁 Duplicate Requests
* ⚠️ External Failure
* 🔄 Retry Flow
* 🔧 Rule Changes via Config

---

## ⚖️ Design Decisions & Trade-offs

| Decision         | Reason                                                 |
| ---------------- | ------------------------------------------------------ |
| JSON Config      | Easy to modify rules/workflows without code change     |
| FastAPI          | Fast, built-in Swagger UI                              |
| SQLite           | Lightweight for demo                                   |
| eval() for rules | Simple but replaceable with safer parser in production |

---

## 🚀 Future Improvements

* Replace `eval()` with rule parser
* Add Redis/Kafka for async retries
* UI dashboard for workflow visualization
* Rule versioning
* Microservices architecture

---

## 📊 Key Highlights (For Evaluators)

* ✔ Configurable workflows
* ✔ Explainable decisions
* ✔ Strong audit logging
* ✔ Idempotent system design
* ✔ Failure handling & retry
* ✔ Clean modular architecture

---

## 🏁 Conclusion

This system demonstrates how to build a **robust, scalable, and configurable decision platform** capable of adapting to real-world business workflows with minimal code changes.

---

## 👨‍💻 Author

Abhilash Alshi

---
