# This will contain Person Superclass, (Student and Employee) subclasses.

class Person:
    def __init__(self, name, age, email):
        # Basic personal information
        self.name = name
        self.age = age
        self.email = email

    def view_profile(self):
        # Return profile information
        return f"Name: {self.name}, Age: {self.age}, Email: {self.email}"

    def update_contact(self, email):
        # Validate email
        if not isinstance(email, str) or "@" not in email:
            return "Invalid email format. Please provide a valid email address."

        if email.strip() == "":
            return "Email cannot be empty. Please provide a valid email address."

        # Update email
        self.email = email
        return f"Email updated successfully to {self.email}"


# *************************************************** STUDENT CLASS ********************************************************** #

class Student(Person):
    def __init__(self, studentId, name, age, email, gpa):
        # Inherit Person attributes
        super().__init__(name, age, email)

        # Student-specific attributes
        self.studentId = studentId
        self.gpa = gpa
        self.department = None  # Will be set when student is enrolled

    def enroll(self, dept_obj):
        # Set a department for the student
        self.department = dept_obj

        # Add student to department list
        dept_obj.students.append(self)

        # Return confirmation
        return f"{self.name}:{self.studentId} has been enrolled in {dept_obj.departmentName} department."

    def get_level(self):
        # Base student level
        return "Student"

    def update_gpa(self, new_gpa):
        # Validate GPA
        if not isinstance(new_gpa, (int, float)):
            return "Invalid GPA. Please provide a numeric value."
        if new_gpa < 0.0 or new_gpa > 4.0:
            return "Invalid GPA. Please provide a value between 0.0 and 4.0."

        # Update GPA
        self.gpa = new_gpa
        return f"{self.name}:{self.studentId}'s GPA has been updated to {self.gpa}."


class Undergrad(Student):
    # Undergraduate student subclass
    def get_level(self):
        return "Undergraduate"


class PostGrad(Student):
    # Postgraduate student subclass
    def __init__(self, studentId, name, age, email, gpa, thesis_required=True):
        super().__init__(studentId, name, age, email, gpa)
        self.thesis_required = thesis_required

    def get_level(self):
        return "Postgraduate"
