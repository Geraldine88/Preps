# This project is to create a School management project to study and understand Encapsulation,
# Inheritance in Python.
"""
I will call the functions of the classes in the main.py file to demonstrate the 
use of Encapsulation and Inheritance in Python.
"""

from school_core import School, Department
from people import Undergrad, PostGrad
from emp_type import Teacher, SupportStaff


# ---------------------------------------------------------
# 1. Create School
# ---------------------------------------------------------
school1 = School("CarThan University", "7777777 Way North, WA", "777-777-7777")

# ---------------------------------------------------------
# 2. Create Departments
# ---------------------------------------------------------
dept1 = Department("CS100", "Computer Science", "Dr. Nnene")
dept2 = Department("MAT200", "Mathematics", "Dr. Kelvin")

print(school1.addDept(dept1))
print(school1.addDept(dept2))

# ---------------------------------------------------------
# 3. Create Students (Undergrad + PostGrad)
# ---------------------------------------------------------
student1 = Undergrad("CS30A001", "Layla James", 17, "layjames@caru.edu", 3.99)
student2 = PostGrad("CS30A002", "Michael Stone", 24, "mstone@caru.edu", 3.75)

print(school1.registerStudent(student1, dept1))
print(school1.registerStudent(student2, dept1))

# ---------------------------------------------------------
# 4. Create Employees (Teacher + SupportStaff)
# ---------------------------------------------------------
teacher1 = Teacher("EMP100", "Dr. Smith", 45, "smith@caru.edu")
staff1 = SupportStaff("EMP200", "Janet Cole", 33, "jcole@caru.edu")

print(school1.hire_emp(teacher1, dept1))
print(school1.hire_emp(staff1, dept2))

# ---------------------------------------------------------
# 5. Demonstrate Encapsulation
# ---------------------------------------------------------
print(student1.update_gpa(3.85))
print(teacher1.update_contact("drsmith@caru.edu"))
print(student1.view_profile())

# ---------------------------------------------------------
# 6. Demonstrate Inheritance
# ---------------------------------------------------------
print(student1.get_level())
print(student2.get_level())

print(teacher1.get_role())
print(staff1.get_role())

# ---------------------------------------------------------
# 7. Department Info
# ---------------------------------------------------------
print(dept1.get_dept_info())
print(dept2.get_dept_info())

# ---------------------------------------------------------
# 8. List all students (show LEVEL, not GPA)
# ---------------------------------------------------------
print("\n*************************** ALL STUDENTS ***************************************")
for s in school1.list_all_students():
    print(f"{s.studentId} - {s.name} - Level: {s.get_level()} - Dept: {s.department.departmentName}")

# ---------------------------------------------------------
# 9. List all Employees 
# ---------------------------------------------------------
print("\n*************************** ALL EMPLOYEES ***************************************")
for emp in school1.list_all_employees():
    print(f"{emp.empId} - {emp.name} - Role: {emp.get_role()} - Dept: {emp.department.departmentName}")
