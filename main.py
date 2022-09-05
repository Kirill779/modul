from datetime import datetime
from application.salary import calculate_salary
from application.db.people import get_employees

import valcheck 0.0.6

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    datanow = datetime.today()
    print(datanow.date())
    Salary = calculate_salary()
    print (Salary)
    print()
    print(get_employees())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
