from sqlalchemy import Column, String, ForeignKey, Integer, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

database = create_engine("mysql+pymysql://hbnb_dev:hbnb_dev_pwd@localhost/hbnb_dev_db")
Base = declarative_base()
Session = sessionmaker(bind=database)
session = Session()

class Student(Base):
    __tablename__ = 'student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(120))
    subjects = relationship("Subjects")

    def __repr__(self):
        return f"<studentsId={self.id}>, name={self.name}"


class Subjects(Base):
    __tablename__ = 'subject'

    sub_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100))
    student_id = Column(ForeignKey("student.id"))
    student = relationship("Student")

    def __repr__(self):
        return f"<subjectId={self.sub_id}>, subjectName={self.name}"

Base.metadata.create_all(database)
