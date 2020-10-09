from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from Model.Models import Base

engine = create_engine('sqlite:///Model/message_handler.db')
Base.metadata.bind = engine
Base.metadata.create_all(engine, checkfirst=False)
DBSession = sessionmaker(bind=engine)
session = DBSession()



