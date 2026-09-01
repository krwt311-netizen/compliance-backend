from fastapi import HTTPException ,Depends
from database import SessionLocal 
import database_model
from models import Scan , FieldCheck
from  fastapi import FastAPI
from sqlalchemy.orm import Session
app = FastAPI()

    
scans = [
    Scan(
        id=5,
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
    db_scan = database_model.Scan (
        mrp_value=scan.mrp.value,
        mrp_is_valid=scan.mrp.is_valid,
        mrp_message=scan.mrp.message,
        net_quantity_value=scan.net_quantity.value,
        net_quantity_is_valid=scan.net_quantity.is_valid,
        net_quantity_message=scan.net_quantity.message,
        manufacturer_address_value=scan.manufacturer_address.value,
        manufacturer_address_is_valid=scan.manufacturer_address.is_valid,
        manufacturer_address_message=scan.manufacturer_address.message,
        mfg_date_value=scan.mfg_date.value,
        mfg_date_is_valid=scan.mfg_date.is_valid,
        mfg_date_message=scan.mfg_date.message,
        consumer_care_value=scan.consumer_care.value,
        consumer_care_is_valid=scan.consumer_care.is_valid,
        consumer_care_message=scan.consumer_care.message,
        unit_of_measurement_value=scan.unit_of_measurement.value,
        unit_of_measurement_is_valid=scan.unit_of_measurement.is_valid,
        unit_of_measurement_message=scan.unit_of_measurement.message,
        country_of_origin_value=scan.country_of_origin.value if scan.country_of_origin else None,
        country_of_origin_is_valid=scan.country_of_origin.is_valid if scan.country_of_origin else None,
        country_of_origin_message=scan.country_of_origin.message if scan.country_of_origin else None,
        overall_status=scan.overall_status
                )
    db.add(db_scan)
    db.commit()
    db.refresh(db_scan)
    return {"message": "Scan added successfully."}

@app.put("/scans/{id}")
def update_scan(id: int, scan: Scan, db:Session = Depends(get_db)):

    db_Scan = db.query(database_model.Scan).filter(database_model.Scan.id == id).first()
    db_Scan.mrp_value = scan.mrp.value
    db_Scan.mrp_is_valid = scan.mrp.is_valid
    db_Scan.mrp_message = scan.mrp.message
    db_Scan.net_quantity_value = scan.net_quantity.value
    db_Scan.net_quantity_is_valid = scan.net_quantity.is_valid      
    db_Scan.net_quantity_message = scan.net_quantity.message
    db_Scan.manufacturer_address_value = scan.manufacturer_address.value
    db_Scan.manufacturer_address_is_valid = scan.manufacturer_address.is_valid  
    db_Scan.manufacturer_address_message = scan.manufacturer_address.message
    db_Scan.mfg_date_value = scan.mfg_date.value
    db_Scan.mfg_date_is_valid = scan.mfg_date.is_valid
    db_Scan.mfg_date_message = scan.mfg_date.message
    db_Scan.consumer_care_value = scan.consumer_care.value
    db_Scan.consumer_care_is_valid = scan.consumer_care.is_valid
    db_Scan.consumer_care_message = scan.consumer_care.message
    db_Scan.unit_of_measurement_value = scan.unit_of_measurement.value
    db_Scan.unit_of_measurement_is_valid = scan.unit_of_measurement.is_valid
    db_Scan.unit_of_measurement_message = scan.unit_of_measurement.message
    db_Scan.country_of_origin_value = scan.country_of_origin.value if scan.country_of_origin else None
    db_Scan.country_of_origin_is_valid = scan.country_of_origin.is_valid if scan.country_of_origin else None
    db_Scan.country_of_origin_message = scan.country_of_origin.message if scan.country_of_origin else None
    db_Scan.overall_status = scan.overall_status
    db.commit()
    db.refresh(db_Scan)
    
    if not db_Scan:
     raise HTTPException(status_code=404, detail="invalid scan id")   
    return {"message": "Scan updated successfully."} 

@app.delete("/scans/{id}")
def delete_scan(id: int, db:Session = Depends(get_db)):
    db_Scan = db.query(database_model.Scan).filter(database_model.Scan.id == id).first()
    if not db_Scan:
        raise HTTPException(status_code=404, detail="Scan not found")
    db.delete(db_Scan)
    db.commit()
    return {"message": "Scan deleted successfully."}
    raise HTTPException(status_code=404, detail="unavailable")

