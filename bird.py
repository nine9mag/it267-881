from turtle import color


class Bird:
    global bird_type #global variable
    #ถ้าไม่ใช่คำว่า global ตัวแปร bird_type จะกลายเป็น class variable
    bird_type = 'parrot'
    bird_name = 'Lori' #class variable

    def __init__(self,color) -> None:
        self.color = color #instance variable
        name = 'Peter' #Local variable
        print(f'{name} in init')

if __name__ == '__main__':
    my_bird = Bird('Green,blue')

    #เรียกใช้ instance variable
    print(my_bird.color)

    #เรียกใช้ class variable
    print(Bird.bird_name)

    #เรียกใช้ global variable
    print(bird_type)