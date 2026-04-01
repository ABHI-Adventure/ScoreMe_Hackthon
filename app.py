from fastapi import FastAPI, HTTPException
from database import SessionLocal, engine
from models import Base, Request, AuditLog
from rules_engine import RulesEngine
from workflow_engine import WorkflowEngine

app = FastAPI()

Base.metadata.create_all(bind=engine)

rules_engine = RulesEngine()
workflow_engine = WorkflowEngine()


@app.post("/process")
def process_request(payload: dict):

    db = SessionLocal()

    request_id = payload.get("request_id")

    # ✅ Idempotency check
    existing = db.query(Request).filter_by(request_id=request_id).first()
    if existing:
        return {
            "status": existing.status,
            "message": "Duplicate request"
        }

    try:
        # Save initial request
        req = Request(
            request_id=request_id,
            type=payload.get("type"),
            status="PROCESSING",
            input_data=payload.get("data")
        )
        db.add(req)
        db.commit()

        # Workflow execution
        workflow_engine.execute(payload.get("type"))

        # Rules evaluation
        decision, logs = rules_engine.evaluate(
            payload.get("type"),
            payload.get("data")
        )

        # Save audit logs
        for log in logs:
            audit = AuditLog(
                request_id=request_id,
                rule=log["rule"],
                result=log["result"],
                reason=""
            )
            db.add(audit)

        # Update status
        req.status = decision
        db.commit()

        return {
            "status": decision,
            "audit": logs
        }

    except Exception as e:
        req.status = "RETRY"
        db.commit()

        raise HTTPException(status_code=500, detail=str(e))

    finally:
        db.close()