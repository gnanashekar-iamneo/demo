from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings


#-------------- DB setup --------------
SQLALCHEMY_DATABASE_URL = settings.database_url
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
     #pool_size=10,
     #max_overflow=20,
     #pool_timeout=30,
     #pool_recycle=1800,
     #pool_pre_ping=True,
)
#^^^^^^^^^^note we need some specail imports for pool managment ref official docs 
SessionLocal = sessionmaker(
    autocommit=False, 
    autoflush=False,
    bind=engine
 )
Base = declarative_base()
#-------------- DB setup --------------

#-------------Db instance-------------
# This function will be used to create a new database session for each request
#Define a function to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
        # The yield statement allows us to return the db session
        # yield allows us to use this function as a context manager
    finally:
        db.close()
#-------------Db instance------------- #