from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

@pytest.fixture(scope="module")
def db():
    engine = create_engine(
        "sqlite:///./test.db",
        connect_args={"check_same_thread": False}
    )

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    session = TestingSessionLocal()

    Base.metadata.create_all(bind=engine)

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)