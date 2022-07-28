import os
 
from sqlalchemy import Column, DateTime, String, Integer, ForeignKey, func
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
 
Base = declarative_base()
class Department(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    employees = relationship('Employee',secondary='department_employee_link', backref='dept', uselist=True )
 
class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    hired_on = Column(DateTime,default=func.now())
 
 
class DepartmentEmployeeLink(Base):
    __tablename__ = 'department_employee_link'
    department_id = Column(Integer, ForeignKey('department.id'), primary_key=True)
    employee_id = Column(Integer, ForeignKey('employee.id'), primary_key=True)

 
from sqlalchemy import create_engine
engine = create_engine('sqlite:///manytomany.sqlite')
 
from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)
session=Session()
Base.metadata.create_all(engine)