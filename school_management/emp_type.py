# This will contain Employee subclasses (Teacher and SupportStaff)

from people import Person

class Employee(Person):
    def __init__(self, empId, name, age, email, role):
        # Inherit Person attributes
        super().__init__(name, age, email)

        # Employee-specific attributes
        self.empId = empId
        self.role = role
        self.department = None  # Will be set when employee is hired
        self.tasks = []  # Task list

    def assign_task(self, task):
        # Add task to employee’s task list
        self.tasks.append(task)
        return f"Task '{task}' has been assigned to {self.name}."

    def get_role(self):
        # Return employee role
        return f"{self.name} is a {self.role} in the {self.department.departmentName} department."


class SupportStaff(Employee):
    # Support staff subclass
    def __init__(self, empId, name, age, email, role="Support Staff"):
        super().__init__(empId, name, age, email, role)


class Teacher(Employee):
    # Teacher subclass
    def __init__(self, empId, name, age, email, role="Teacher"):
        super().__init__(empId, name, age, email, role)
