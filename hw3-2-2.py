#Author: JTI 10/6/21

height = input("Enter your hight in meters: ")
weight = input("Enter yout weight in kilograms: ")

bmi = (int(weight) / int(height)) ** 2

if int(bmi) < 19:
  print("You are underwight ")
elif int(bmi) < 25:
  print("You are healthy ")
elif int(bmi) < 30:
  print("You are overwight ")
elif int(bmi) < 40: 
  print("You are obese ")
else:
  print("You are extremly obese")
