from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# inherit DeclarativeBase class when you write up a model.
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata

# set the connection string here
engine = create_engine('sqlite:///exampl2.db')
Session = sessionmaker(bind=engine, autocommit=True)

# import the dbsession instance to execute queries on your database
dbsession = Session()

# import your models.
#from models.auth import Group, Permission, User

# calling this will create the tables at the database
#__create__ = lambda: (setattr(engine, 'echo', True), metadata.create_all(engine))

