import main
from main import PercentCalculator, AppliedPercentsCalculator


def calculate():
    m = int(input('เลือก mode ที่ต้องการ:'))
    c = PercentCalculator()
    if m == 1:
        c.get_output()
    elif m == 2:
        c.get_percents()
    elif m == 3:
        c.get_input()
    elif m == 4:
        c = AppliedPercentsCalculator()
    else:
        print('Please try again')
    return calculate()

calculate()
