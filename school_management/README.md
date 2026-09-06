---

# ⭐ **README.md — School Management System (Python OOP Project)**

```
# School Management System (Python OOP Project)

This project was created to study and understand **Encapsulation**, **Inheritance**, **Composition**, and **Aggregation** in Python using Object-Oriented Programming (OOP).  
It models a simple school management system with classes representing people, students, employees, departments, and the school itself.

The project demonstrates:

- **Encapsulation**  
  - Controlled access to attributes (GPA, email, tasks, department)
  - Methods that safely update internal state (`update_gpa`, `update_contact`, `assign_task`)

- **Inheritance**  
  - `Person` → `Student` → `Undergrad` / `PostGrad`
  - `Person` → `Employee` → `Teacher` / `SupportStaff`
  - Overridden methods (`get_level`, `get_role`)

- **Composition**  
  - A `School` *owns* its `Departments`
  - A `Department` *owns* its `students[]` and `employees[]`
  - If the parent is deleted, the children cannot exist independently

- **Aggregation**  
  - A `School` *has* Students and Employees
  - Students and Employees exist independently and can be created before being added to a school

- **Polymorphism**  
  - Same method name, different behavior depending on subclass  
  - Example: `get_level()` returns different values for Student, Undergrad, PostGrad

---

## 📁 Project Structure

```
school_management/
│
├── main.py            # Demonstrates Encapsulation + Inheritance
├── people.py          # Person, Student, Undergrad, PostGrad
├── emp_type.py        # Employee, Teacher, SupportStaff
└── school_core.py     # School and Department classes
```

---

## 🧩 Class Overview

### **Person (Base Class)**  
Attributes: `name`, `age`, `email`  
Methods: `view_profile()`, `update_contact()`

---

### **Student (inherits Person)**  
Attributes: `studentId`, `gpa`, `department`  
Methods: `enroll()`, `update_gpa()`, `get_level()`

#### **Undergrad (inherits Student)**  
Overrides: `get_level()`

#### **PostGrad (inherits Student)**  
Attributes: `thesis_required`  
Overrides: `get_level()`

---

### **Employee (inherits Person)**  
Attributes: `empId`, `role`, `tasks`, `department`  
Methods: `assign_task()`, `get_role()`

#### **Teacher (inherits Employee)**  
Overrides: `get_role()`

#### **SupportStaff (inherits Employee)**  
Overrides: `get_role()`

---

### **Department**  
Attributes: `departmentId`, `departmentName`, `headOfDept`  
Contains: `students[]`, `employees[]`  
Relationship: **Composition** (Department cannot exist without School)

---

### **School**  
Attributes: `schoolName`, `Address`, `Contact`  
Contains: `departments[]`, `students[]`, `employees[]`  
Relationships:  
- **Composition** with Department  
- **Aggregation** with Student  
- **Aggregation** with Employee  

Methods:  
`addDept()`, `registerStudent()`, `hire_emp()`, `list_all_students()`, `list_all_employees()`

---

## ▶️ Running the Project

Run:

```
python main.py
```

This will:

- Create a school  
- Create departments  
- Create students (Undergrad + PostGrad)  
- Create employees (Teacher + SupportStaff)  
- Register students  
- Hire employees  
- Demonstrate Encapsulation  
- Demonstrate Inheritance  
- List all students and employees  

---

## 🎯 Learning Objectives

This project helps you understand:

### ✔ Encapsulation  
Protecting internal data using methods.

### ✔ Inheritance  
Building specialized classes from general ones.

### ✔ Polymorphism  
Same method name, different behavior.

### ✔ Composition  
Strong ownership relationships.

### ✔ Aggregation  
Weak “has‑a” relationships.

---

## 📌 Future Enhancements (Optional)

- CLI menu (interactive program)
- JSON saving/loading
- Auto‑generate student IDs
- Department reports
- GPA transcript printing
- UML diagram export
```

---

