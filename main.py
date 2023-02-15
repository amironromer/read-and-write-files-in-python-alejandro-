# remember to fork this and push to github

# f = open('test.txt', "r")
# print(f.readlines())
# f.close()

# with open('test.txt', 'r') as f:
#   f_contents = f.readlines()
#   print(f_contents, end='')

# employee_file = open("employees.txt", "r")
# print(employee_file.readlines())
# employee_file.close()

# employee_file = open("employees.txt", "r")
# print(employee_file.readlines()[1])
# employee_file.close()

employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
  print(employee)
employee_file.close()













