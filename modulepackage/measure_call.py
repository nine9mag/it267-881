#วิธีที่1
from measure import Measure

if __name__ == '__main__':
    mobj = Measure()
    print(f'5 cm = {mobj.cm_inch(5):.2f} inch')
    print(f'18.5 inch = {mobj.inch_cm(18.5):.2f} cm')