from sqlalchemy import create_engine
from conf.config import DB_CONN_STRING
from sqlalchemy.orm import scoped_session, sessionmaker

engine = create_engine(DB_CONN_STRING)
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=engine))
