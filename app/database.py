from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from .config import settings

SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}' # 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

sessionlocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

Base = declarative_base()

# while True:

#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='sqL850#datA', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to database was failed")
#         print("Error: ", error)
#         time.sleep(2)