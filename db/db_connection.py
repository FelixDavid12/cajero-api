from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# DATABASE_URL = "postgresql://postgres:4561@localhost:5432/MISION_TIC"
DATABASE_URL = os.environ['DATABASE_URL']
# DATABASE_URL = "postgres://viozdwtzzszddn:a35acb2522bf2b1199d6e97d28452ab1c65dab5c2e177c38b29de8ef8403013f@ec2-54-88-130-244.compute-1.amazonaws.com:5432/d41v2mjf65h6da"
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
Base.metadata.schema = "cajerodb"


