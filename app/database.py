from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings


import psycopg2
from psycopg2.extras import RealDictCursor


sqlalchemy_url = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
engine = create_engine(sqlalchemy_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres',
#                                 password='admin', cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print('Database connection successful')
#         break
#     except Exception as err:
#         print('Connection to database failed')
#         print(err)