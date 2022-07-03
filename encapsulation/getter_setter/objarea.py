from area import Area

area = Area()
area.base = float(input("Enter base:"))
area.high = float(input("Enter high:"))
print(f'Area = {area.compute_area():.2f}')


"""#ถ้าไม่ใช่ property
base = float(input("Enter base: "))
high = float(input("Enter high: "))
area.setbase(base)
area.sethigh(high)
area.compute_area()"""