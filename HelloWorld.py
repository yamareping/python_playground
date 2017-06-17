import sys

def EnterNumer(msg, isAcceptZero):
    while True:
        try:
            print(msg)
            number = float(input())
            if isAcceptZero == False and number == 0: 
                print("cannot zero") 
                continue
            else: break
        except: 
            print("Error: please input number")
    return number


age = EnterNumer("How old are you?", True)

height = EnterNumer("Please enter your height", False)

weight = EnterNumer("Please enter your weight", False)

bmi = weight / ((height / 100) * (height / 100))

msg = "Age: {}, Height: {}, Weight: {}, BMI:{}".format(age, height, weight,bmi)

print(msg)

