from database import engine
from database_model import base
base.metadata.create_all(bind=engine)
