switch_status = False #เปิดปิดไฟ

def turnon():   #เปิด
    global switch_status
    witch_status = True
    print("light on")

def turnoff():  #ปิด
    global switch_status
    witch_status = False
    print("light off")

if __name__ == "__main__":
    print(f'light status: {switch_status}')
    turnon()
    turnoff()
    turnon()
    turnoff()