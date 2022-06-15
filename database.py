from sqlmodel import create_engine, Session

DATABASE_NAME = "HospitalProject.db"
DATABASE_URL = f"sqlite:///{DATABASE_NAME}"
# with sqlite we must passed the arguments
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread": False})

# no need of check_same_thread for mysql
# DATABASE_URL = "mysql+mysqldb://isrardawar:dawar96418@localhost:3306/FGPC"
# engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = Session(bind=engine)
