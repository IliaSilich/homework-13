from dataclasses import dataclass
from typing import NamedTuple, TypedDict
from pydantic import BaseModel, validator


@dataclass
class StudentDTO:
    name: str
    surname: str
    age: int
    course: int
    average_grade: float

    def validate(self):
        self._validate_name()
        self._validate_age()
        self._validate_course()
        self._validate_average_grade()

    def _validate_name(self):
        if not (self.name.isalpha() and self.surname.isalpha()):
            raise ValueError("Name and surname should consist only of English letters.")
        if not (self.name[0].isupper() and self.surname[0].isupper()):
            raise ValueError("Name and surname should start with a capital letter.")

    def _validate_age(self):
        if not (18 <= self.age <= 30):
            raise ValueError("Age should be between 18 and 30.")

    def _validate_course(self):
        if not (1 <= self.course <= 6):
            raise ValueError("Course should be between 1 and 6.")

    def _validate_average_grade(self):
        if not (1 <= self.average_grade <= 100):
            raise ValueError("Average grade should be between 1 and 100.")


class StudentDTO_nt(NamedTuple):
    name: str
    surname: str
    age: int
    course: int
    average_grade: float

    def validate(self):
        pass

class StudentDTO_td(TypedDict):
    name: str
    surname: str
    age: int
    course: int
    average_grade: float

    def validate(self):
        pass


class StudentDTO_pydantic(BaseModel):
    name: str
    surname: str
    age: int
    course: int
    average_grade: float

    @validator("name", "surname")
    def validate_name(cls, value):
        if not value.isalpha():
            raise ValueError("Name and surname should consist only of English letters.")
        if not value[0].isupper():
            raise ValueError("Name and surname should start with a capital letter.")
        return value

    @validator("age")
    def validate_age(cls, value):
        if not (18 <= value <= 30):
            raise ValueError("Age should be between 18 and 30.")
        return value

    @validator("course")
    def validate_course(cls, value):
        if not (1 <= value <= 6):
            raise ValueError("Course should be between 1 and 6.")
        return value

    @validator("average_grade")
    def validate_average_grade(cls, value):
        if not (1 <= value <= 100):
            raise ValueError("Average grade should be between 1 and 100.")
        return value
