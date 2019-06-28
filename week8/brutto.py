class Employee:
    """docstring for Employee"""

    def __init__(self, employee_type, hourly_wage, working_hour):

        self.employee_type = employee_type
        self.hourly_wage = hourly_wage
        self.working_hour = working_hour

    def __str__(self):
        salary = (float)(self.hourly_wage) * (float)(self.working_hour)
        return f"The gross salary for the given employee is ${salary} every month."

if __name__ == '__main__':
    employee_types = ['angestellte', 'arbeiter']
    print("-----------salary calculation----------")
    type = input(
        "Please enter the type of employee ('angestellte' or 'arbeiter'): ")
    hour = input(
        "Please enter the working hour of the employee: ")
    if type.lower() == 'angestellte':
        employee = Employee(type.lower, 25, hour)
    elif type.lower() == 'arbeiter':
        employee = Employee(type.lower, 20, hour)
    print(employee)
