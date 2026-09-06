# This will contain School and Department classes

from people import Student
from emp_type import Employee

class School:
    def __init__(self, schoolName, Address, Contact):
        # School information
        self.schoolName = schoolName
        self.Address = Address
        self.Contact = Contact

        # Lists to hold departments, students, and employees
        self.departments = []
        self.students = []
        self.employees = []

    def addDept(self, departmentObj):
        # Validate department object
        if departmentObj is None:
            return "Invalid department. Please provide a valid department."

        if not isinstance(departmentObj, Department):
            return "Object must be a Department instance."

        # Prevent duplicate department ID
        for dept in self.departments:
            if dept.departmentId == departmentObj.departmentId:
                return "Department already exists."

        # Add department
        self.departments.append(departmentObj)
        return f"{departmentObj.departmentName}:{departmentObj.departmentId} has been added to {self.schoolName} school."

    def registerStudent(self, student_obj, dept_obj):
        # Validate student
        if not isinstance(student_obj, Student):
            return "Object must be a Student instance."

        # Validate department
        if dept_obj not in self.departments:
            return "Department does not belong to this school."

        # Prevent duplicate student ID
        for s in self.students:
            if s.studentId == student_obj.studentId:
                return "Student already exists."

        # Add student to school
        self.students.append(student_obj)

        # Add student to department
        dept_obj.students.append(student_obj)

        # Link student to department
        student_obj.department = dept_obj

        return f"{student_obj.name}:{student_obj.studentId} has been registered to {self.schoolName} school and {dept_obj.departmentName} department."

    def hire_emp(self, emp_obj, dept_obj):
        # Validate employee
        if not isinstance(emp_obj, Employee):
            return "Object must be an Employee instance."

        # Validate department
        if dept_obj not in self.departments:
            return "Department does not belong to this school."

        # Prevent duplicate employee ID
        for e in self.employees:
            if e.empId == emp_obj.empId:
                return "Employee already exists."

        # Add employee to school
        self.employees.append(emp_obj)

        # Add employee to department
        dept_obj.employees.append(emp_obj)

        # Link employee to department
        emp_obj.department = dept_obj

        return f"{emp_obj.name}:{emp_obj.empId} has been hired to {self.schoolName} school and {dept_obj.departmentName} department."

    def list_all_students(self):
        # Return all students
        return self.students

    def list_all_employees(self):
        # Return all employees
        return self.employees


class Department:
    def __init__(self, departmentId, departmentName, headOfDept):
        # Department information
        self.departmentId = departmentId
        self.departmentName = departmentName
        self.headOfDept = headOfDept

        # Lists to hold students and employees
        self.students = []
        self.employees = []

    def get_dept_info(self):
        # Return department details
        return f"Department ID: {self.departmentId}, Department Name: {self.departmentName}, Head of Department: {self.headOfDept}"
