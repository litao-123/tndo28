from  models.db import Base
from datetime import datetime
from sqlalchemy import Column,Integer,String,DateTime

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),unique=True,nullable=False)
    password = Column(String(50))
    creatime = Column(DateTime,default=datetime.now)
    email = Column(String(80))

    def __repr__(self):
        return "<UserId:{},Username:{}>".format(self.id,self.name)


if __name__ == '__main__':
    Base.metadata.create_all()

