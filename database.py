from sqlmodel import create_engine, Session

DATABASE_NAME = "HospitalProject.db"
DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = Session(bind=engine)

# from sqlmodel import create_engine, Session
#
# sqlite_file_name = "database.db"
# sqlite_url = f"sqlite:///{sqlite_file_name}"
#
#
# engine = create_engine(sqlite_url, echo=True)
#
# SessionLocal = Session(bind=engine)
#
#
# def get_db():
#     db = SessionLocal
#     try:
#         yield db
#     finally:
#         db.close()
