#Author JTI 10/6/21

grade = input("Enter numerical grade: ")

if int(grade) >= 93:
  print("Your letter grade is an A")
elif int(grade) >= 90:
  print("Your letter grade is a A-")
elif int(grade) >= 87:
  print("Your letter grade is a B+")
elif int(grade) >= 83:
  print("Your letter grade is a B")
elif int(grade) >= 80:
  print("Your letter grade is a B-")
elif int(grade) >= 77:
  print("Your letter grade is a C+")
elif int(grade) >= 73:
  print("Your letter grade is a C")
elif int(grade) >= 70:
  print("Your letter grade is a C-")
elif int(grade) >= 65:
  print("Your letter grade is a D+")
elif int(grade) >= 60:
  print("Your letter grade is a D")
else:
  print("Your letter grade is a F")
  
