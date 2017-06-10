import sys

print("Please enter your height:")
height = int(sys.stdin.readline())

print("Please enter your weight:")
weight = int(sys.stdin.readline()) 

msg = "Height: {}, Weight: {}".format(height, weight)
print(msg)

bmi = weight / ((height / 100) * (height / 100))
print("BMI: {} !!!".format(bmi))
