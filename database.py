from sqlmodel import create_engine, Session

DATABASE_NAME = "HospitalProject.db"
DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

# DATABASE_URL = "mysql+mysqldb://isrardawar:dawar96418@localhost:3306/hospital"

engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})
SessionLocal = Session(bind=engine)


