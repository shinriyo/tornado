from sqlalchemy import create_engine, Column, Integer, Table, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_url = 'sqlite:///example.db'
engine = create_engine(database_url)
Base = declarative_base(engine)
metadata = Base.metadata

users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(40)),
    Column('profile_url', String(40)),
    Column('access_token', String(40)),
)

try:
    users.create()
except:
    pass

Session = sessionmaker(bind=engine)
dbsession = Session()
