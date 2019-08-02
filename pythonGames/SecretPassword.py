passwordFile = open('password.txt')
secretPassword = passwordFile.read()  # it is only meant for first row and first coloumn
print('Enter your password.')
typedPassword = input()
if typedPassword == secretPassword:
    print('Access granted')
if typedPassword == '12345':
    print('That password is one that an idiot puts on their luggage.')
else:
    print('Access denied')
