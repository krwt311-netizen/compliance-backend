from fastapi import HTTPException ,Depends
from database import SessionLocal 
import database_model
from models import Scan , FieldCheck
from  fastapi import FastAPI
from sqlalchemy.orm import Session
app = FastAPI()

    
scans = [
    Scan(
        id=1,
        mrp=FieldCheck(value="₹99, inclusive of all taxes", is_valid=True, message="OK"),
        net_quantity=FieldCheck(value="500g", is_valid=True, message="OK"),
        manufacturer_address=FieldCheck(value="XYZ Pvt Ltd, Delhi", is_valid=True, message="OK"),
        mfg_date=FieldCheck(value="not found", is_valid=False, message="Missing on label"),
        consumer_care=FieldCheck(value="care@xyz.com", is_valid=True, message="OK"),
        unit_of_measurement=FieldCheck(value="g", is_valid=True, message="OK"),
        country_of_origin=FieldCheck(value="India", is_valid=True, message="OK"),
        overall_status="Non-Compliant"
    ),
]
def get_db():
  db = SessionLocal ()
  try:
    yield db
  finally:
        db.close()
   



@app.get("/home")
def home():
    return {"message": "Welcome to the Scan API!"}

@app.get("/scans")
def get_all_scans(db:Session = Depends(get_db)):
    db_Scans = db.query(database_model.Scan).all()
    
    return db_Scans



@app.get("/scans/{id}")
def get_scan_by_id(id: int,db:Session = Depends(get_db)):
    db_Scan = db.query(database_model.Scan).filter(database_model.Scan.id == id).first()
    if not db_Scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    return db_Scan

@app.post("/scans")
def add_scan(scan: Scan, db:Session = Depends(get_db)):
    db.add(scan)
    db.commit()
    db.refresh(scan)
    return {"message": "Scan added successfully."}   

@app.put("/scans/{id}")
def update_scan(id: int, scan: Scan, db:Session = Depends(get_db)):
    db_Scan = db.query(database_model.Scan).filter(database_model.Scan.id == id).first()
    if not db_Scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    for key, value in scan.dict().items():
        setattr(db_Scan, key, value)
    db.commit()
    db.refresh(db_Scan)
    return {"message": "Scan updated successfully."}
    scans[i] = scan
    return {"message": "Scan updated successfully."}
    raise HTTPException(status_code=404, detail="invalid scan id")    

@app.delete("/scans/{id}")
def delete_scan(id: int, db:Session = Depends(get_db)):
    db_Scan = db.query(database_model.Scan).filter(database_model.Scan.id == id).first()
    if not db_Scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    db.delete(db_Scan)
    db.commit()
    return {"message": "Scan deleted successfully."}
    raise HTTPException(status_code=404, detail="unavailable")

