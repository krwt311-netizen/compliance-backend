from fastapi import HTTPException
from database import SessionLocal
from models import Scan , FieldCheck
from  fastapi import FastAPI
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
        overall_status="Non-Compliant"
    )
]

@app.get("/")
def home():
    return {"message": "Welcome to the Scan API!"}
@app.get("/scans")
def get_all_scans():
    db=SessionLocal()
    db.query()
    return scans



@app.get("/scans/{id}")
def get_scan_by_id(id: int):
    for i in range(len(scans)):
        if scans[i].id == id:
            return scans[i]
    raise HTTPException(status_code=404, detail="scan not found")   

@app.post("/scans")
def add_scan(scan: Scan):
    scans.append(scan)
    return {"message": "Scan added successfully."}   

@app.put("/scans/{id}")
def update_scan(id: int, scan: Scan):
    for i in range(len(scans)):
        if scans[i].id == id:
            scans[i] = scan
            return {"message": "Scan updated successfully."}
    raise HTTPException(status_code=404, detail="invalid scan id")    

@app.delete("/scans/{id}")
def delete_scan(id: int):
    for i in range(len(scans)):
        if scans[i].id == id:
            del scans[i]
            return {"message": "Scan deleted successfully."}
    raise HTTPException(status_code=404, detail="unavailable")

