# string formatting options

a, b, c, d = 10, 20.12345678, "Hello World", True

print("The Value of a = ", a, " b=", b, " c=", c, " d=", d) #immature way

print("The value of a is %i, b is %f, c is %s , d is %d" % (a, b, c, d))

print("The value of a is %i, b is %3.2f, c is %s , d is %d" % (a, b, c, d))

print("The value a is {}, b is {}, c is {}, d is {}".format(a, b, c, d))

print("The value of a is {0}, b is {1}, c is {2}, d is {3}\n {1} is b, {2} is c, {3} is d".format(a, b, c, d))

print("The values are {x} , {y}, {z}, {e} ".format(y=b, x=a, z=c, e=d))

# f string , newly introduced

print(f"The values are a={a} b={b} c={c} d={d}")

print(f" The Sum of 10 & 20 is {10 + 20}")

# you can also separately format the strings

empName = "Prateek"
empCode = "ACC100"
empLocation = "Hyderabad"
empRole = "Python Developer"

employeeDetails = "Employee Description : \n Employee Name is {} with EmployeeCode {} is working from {} location as a {}".format(
    empName, empCode, empLocation, empRole)

print(employeeDetails)

employeeDetails = f"Employee Description : \n Employee Name is {empName} with EmployeeCode {empCode} is working from {empLocation} location as a {empRole}"

print(employeeDetails)
