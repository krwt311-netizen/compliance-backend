
from database import SessionLocal
from models import Scan , FieldCheck
import database_model
from main import scans


def init_db(): 
 db= SessionLocal()
 for s in scans :
     db_scan = database_model.Scan(
            mrp_value=s.mrp.value,
            mrp_is_valid=s.mrp.is_valid,
            mrp_message=s.mrp.message,
     
            net_quantity_value=s.net_quantity.value,
            net_quantity_is_valid=s.net_quantity.is_valid,
            net_quantity_message=s.net_quantity.message,
     
     
            manufacturer_address_value=s.manufacturer_address.value,
            manufacturer_address_is_valid=s.manufacturer_address.is_valid,
            manufacturer_address_message=s.manufacturer_address.message,
     
                 mfg_date_value=s.mfg_date.value,
                 mfg_date_is_valid=s.mfg_date.is_valid,
                 mfg_date_message=s.mfg_date.message,

                 expiry_date_value=s.expiry_date.value,
                 expiry_date_is_valid=s.expiry_date.is_valid,
                 expiry_date_message=s.expiry_date.message,
          
    
                 consumer_care_value=s.consumer_care.value,
                 consumer_care_is_valid=s.consumer_care.is_valid,
                 consumer_care_message=s.consumer_care.message,
          
     
                 unit_of_measurement_value=s.unit_of_measurement.value,
                 unit_of_measurement_is_valid=s.unit_of_measurement.is_valid,
                 unit_of_measurement_message=s.unit_of_measurement.message,
                 overall_status=s.overall_status,
       
                 country_of_origin_value=s.country_of_origin.value,
                 country_of_origin_is_valid=s.country_of_origin.is_valid,
                 country_of_origin_message=s.country_of_origin.message,
          )
     db.add(db_scan)
     db.commit()

init_db()