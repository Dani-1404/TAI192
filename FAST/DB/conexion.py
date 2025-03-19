import os
from sqlalchemy import create_engine 
from sqlalchemy.orm.session import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

bdName="usuarios.sqlite"
base_dir= os.path.dirname(os.path.realpath(__file__))
bdURL= f"sqlite:///{os.path.join(base_dir,bdName)}"

engine= create_engine(bdURL,echo=True)
Session= sessionmaker(bind=engine)
Base = declarative_base()