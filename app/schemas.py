from datetime import date, datetime
from decimal import Decimal
from typing import Optional, List

from pydantic import BaseModel, ConfigDict


# ------------USER / AUTH ----------------
class UserCreate(BaseModel):
    full_name: str
    username: str
    passowrd: str
    role: str

class UserLogin(BaseModel):
    username: str
    password: str

class UserOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    full_name: str
    username: str
    role: str
    is_active: bool


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserOut

# ------------OWNER SESSION ----------------
class OwnerSessionOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    owner_active: bool
    activated_by: Optional[int] = None
    activated_at: Optional[datetime] = None

# ---------------- COURSE ----------------

class CourseCreate(BaseModel):
    name: str
    total_years: int = 3


class CourseUpdate(BaseModel):
    name: Optional[str] = None
    total_years: Optional[int] = None
    is_active: Optional[bool] = None


class CourseOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    total_years: int
    is_active: bool

#-----------------COURSE FEE-----------------
class CourseFeeCreate(BaseModel):
    course_id: int
    study_year: str

    tuition_fee: Decimal = Decimal("0")
    practical_fee: Decimal = Decimal("0")
    exam_fee: Decimal = Decimal("0")
    other_fee: Decimal = Decimal("0")

class CourseFeeUpdate(BaseModel):
    tuition_fee: Optional[Decimal] = None
    practical_fee: Optional[Decimal] = None
    exam_fee: Optional[Decimal] = None

class CourseFeeOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    course_id: int
    study_year: str

    tuition_fee: Decimal
    practical_fee: Decimal
    exam_fee: Decimal
    other_fee: Decimal

#-----------------STUDENT-----------------
class DiscountIn(BaseModel):
    discount_amount: Decimal = Decimal("0")
    discount_reason: Optional[str] = None
    discount_approved_by: Optional[str] = None


class StudentCreate(BaseModel):
    uid: str
    name: str
    father_name: str

    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

    course_id: int
    study_year: str

    admission_date: date
    photo_url: Optional[str] = None

    status: Optional[str] = "Active"

    discount_amount: Decimal = Decimal("0")
    discount_reason: Optional[str] = None
    discount_approved_by: Optional[str] = None

class StudentUpdate(BaseModel):
    name: Optional[str] = None
    father_name: Optional[str] = None

    phone = Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

    course_id: Optional[int] = None
    study_year: Optional[str] = None

    admission_date: Optional[date] = None
    photo_url: Optional[str] = None

    status: Optional[str] = None
    
    discount_amount: Optional[Decimal] = None
    discount_reason: Optional[str] = None
    discount_approved_by: Optional[str] = None

class StudentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    uid: str
    name: str
    father_name: str

    phone: Optional[str] = None
    email: Optional[str] = None
    address: Optional[str] = None

    course_id: int
    study_year: str
    admission_date: date
    photo_url: Optional[str] = None
    status: str

    discount_amount: Decimal
    discount_reason: Optional[str] = None
    discount_approved_by: Optional[str] = None

    created_at: datetime

# ---------------- PAYMENTS ----------------

class FeePaymentCreate(BaseModel):
    student_id: int
    payment_date: date
    amount: Decimal
    mode: str  # Cash, Online, Cheque, UPI
    receipt_no: str
    remarks: Optional[str] = None


class FeePaymentOut(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    student_id: int
    payment_date: date
    amount: Decimal
    mode: str
    receipt_no: str
    remarks: Optional[str] = None
    created_at: datetime


# ---------------- FEE SUMMARY ----------------

class FeeBreakupOut(BaseModel):
    tuition_fee: Decimal
    practical_fee: Decimal
    exam_fee: Decimal
    other_fee: Decimal


class StudentFeeSummaryOut(BaseModel):
    student: StudentOut
    fee_breakup: FeeBreakupOut
    total_fee: Decimal
    discount: Decimal
    final_fee: Decimal
    paid: Decimal
    balance: Decimal
    payments: List[FeePaymentOut]

