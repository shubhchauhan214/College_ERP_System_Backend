from sqlalchemy import Column, Integer, String, Boolean, String, Date, DateTime, ForeignKey, Numeric, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(120), nullable=False)
    username = Column(String(80), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)

    role = Column(String(20), nullable=False)
    is_active = Column(Boolean, default=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    name=Column(String(80), unique=True, nullable=False)
    total_years = Column(Integer, nullable=False, default=3)
    is_active = Column(Boolean, default=True)

    fees = relationship("CourseFee", back_populates="course", cascade="all, delete-orphan")
    students = relationship("Student", back_populates="course")


class CourseFee(Base):
    __tablename__ = "course_fees"

    id = Column(Integer, primary_key=True, index=True)

    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    study_year = Column(String(30), nullable=False)

    tuition_fee = Column(Numeric(10,2), default=0)
    practical_fee = Column(Numeric(10,2), default=0)
    exam_fee = Column(Numeric(10,2), default=0)
    other_fee = Column(Numeric(10,2), default=0)

    course =relationship("Course", back_populates="fees")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)

    uid = Column(String(10), unique=True, index=True, nullable=False)
    name = Column(String(120), nullable=False)
    father_name = Column(String(120), nullable=False)

    phone = Column(String(20), nullable=False)
    email = Column(String(120), nullable=False)
    address = Column(Text, nullable=True)

    course_id = Column(Integer, ForeignKey("courses.id"), nullable=False)
    study_year = Column(String(30), nullable=False)

    admission_date = Column(Date, nullable=False)
    photo_url = Column(Text, nullable=True)    

    status = Column(String(30), default="Active")

    discount_amount = Column(Numeric(10,2), default=0)
    discount_reason = Column(Text, nullable=True)
    discount_approved_by = Column(String(120), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    course = relationship("Course", back_populates="students")
    payments = relationship("Payment", back_populates="student", cascade="all, delete-orphan")


class FeePayment(Base):
    __tablename__ = "fee_payments"

    id = Column(Integer, primary_key=True, index=True)

    student_id = Column(Integer, ForeignKey("students.id"), nullable=False)

    payment_date = Column(Date, nullable=False)
    amount = Column(Numeric(10,2), nullable=False)
    mode = Column(String(30), nullable=False)
    receipt_no = Column(String(50), unique=True, nullable=False)
    remarks = Column(Text, nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    student = relationship("Student", back_populates="payments")