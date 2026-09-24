from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Remember to put YOUR password here!
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:dipanshu1234@localhost:5432/defect_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()