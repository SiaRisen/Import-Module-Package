from datetime import datetime

from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge

if __name__ == '__main__':
    print(datetime.today())
    cs()
    ge()
