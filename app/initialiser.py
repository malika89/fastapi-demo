from app.database.init_db import init_db
from app.database.session import SessionLocal


def init() -> None:
    db = SessionLocal()
    init_db(db)


def main() -> None:
    init()


if __name__ == "__main__":
    main()
