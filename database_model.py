from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean
base = declarative_base()
class FieldCheckDB(base):
    __tablename__ = "field_checks"
    id = Column(Integer, primary_key=True, index=True)
    value = Column(String)
    is_valid = Column(Boolean)
    message = Column(String)
class Scan(base):
   __tablename__ = "scans"
   id=Column(Integer, primary_key=True , index=True)   
   mrp_value = Column(String)
   mrp_is_valid = Column(Boolean)
   mrp_message = Column(String)

   net_quantity_value = Column(String)
   net_quantity_is_valid = Column(Boolean)
   net_quantity_message = Column(String)   
    
   manufacturer_address_value = Column(String)
   manufacturer_address_is_valid = Column(Boolean)
   manufacturer_address_message = Column(String)

   mfg_date_value=Column(String)
   mfg_date_is_valid=Column(Boolean)
   mfg_date_message=Column(String)

   consumer_care_value=Column(String)
   consumer_care_is_valid=Column(Boolean)
   consumer_care_message=Column(String)

   unit_of_measurement_value=Column(String)
   unit_of_measurement_is_valid=Column(Boolean) 
   unit_of_measurement_message=Column(String) 

   country_of_origin_value=Column(String, nullable=True)
   country_of_origin_is_valid=Column(Boolean, nullable=True)
   country_of_origin_message=Column(String, nullable=True)

   overall_status=Column(String)