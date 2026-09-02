from pydantic import BaseModel
from typing import Optional
class FieldCheck(BaseModel):
    value: str
    is_valid: bool
    message: str   
class Scan(BaseModel):
   id:int 
   mrp:FieldCheck
   net_quantity:FieldCheck
   expiry_date: FieldCheck
   manufacturer_address: FieldCheck
   mfg_date: FieldCheck
   consumer_care: FieldCheck
   unit_of_measurement: FieldCheck
   country_of_origin: Optional[FieldCheck] = None
   overall_status: str
