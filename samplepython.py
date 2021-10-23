
list1 = [1, 3, 5, 4, 2]
list1.sort()
print('The sorted list is: {0}'.format(list1))

list1.reverse()
print('The reversed list is: {0}'.format(list1))

list2 = []
list2 = list1.copy()
print('The copied list is: ', list2)

indexvalue = list2[2:5]
print('The index values are: ', indexvalue)


user_value = int(input('Enter a number: '))
num1 = 0
num2 = 1
count = 0

if(user_value <= 0):
    print('Please enter a positive number')

elif(user_value == 1):
    print(user_value)

else:
    print('Fibonacci sequence: ')
    while count < user_value:
        print(num1)
        num3 = num1+num2
        num1 = num2
        num2 = num3
        count += 1
