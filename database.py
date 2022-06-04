from sqlmodel import create_engine, Session

DATABASE_NAME = "/hopitalproject"
DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = Session(bind=engine)
