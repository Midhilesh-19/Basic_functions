index = int(input("enter index:"))


if index == 0:
    print("i am here ")
else:
    print("oops")

#exponent function (power)

def power(base_num , pow_num):
    result = 1 
    for index in range(pow_num):
        result = result * base_num    
    return result


print(power(3,7))

#2D Lists
number = [ [1,2,3],[4,5,6],[7,8,9],[0]]

print(number[3][0])

for row in number:
    
        print(row)

#try/except



try:
    value = 10/0
    num = int(input("Enter a number:"))
    print(num)

except ZeroDivisionError as err:
    print(err)  

except ValueError:
    print("Invalid input")


#reading files

employees = open("employee.txt","r")
'''her .txt file is a notepad file where we have to write the data and save so this opens file 
& writing will add data what we gave '''

for employee in employees:
    print(employees.read())

#writing files

employees = open("employee.txt","a")

employees.write("\nToby - Developer")


