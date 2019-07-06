from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'tndo28'
USERNAME = 'admin'
PASSWORD = 'Root110qwe'

Db_Uri = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(
    USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)

engine = create_engine(Db_Uri)

Base = declarative_base(engine)
Session = sessionmaker(bind=engine)
session= Session()

if __name__=='__main__':
    connection = engine.connect()
    result = connection.execute('select 1')
    print(result.fetchone())

