# hope you enjoy the ride
print (' Hi there, today i am here to give you a magical calculator \n but its pretty simple so lets fire up \n you can use (+ \t - \t * \t / \t)')
def calculator():
    x = float (input ('what is you number thinking about? '))
    xy = input ('enter the element (+, -, *, /):')
    y = float (input ('what is the other number? '))


    if xy == '+':
        print ('result: ', x + y)
    elif xy == '-':
         print ('result: ', x - y)
    elif xy == '*':
         print ('result: ', x * y)
    elif xy == '/':
        print ('result: ', x / y 
           if y != 0 else 'there is no devide by 0 ! ')
    else:
        print ('not a true value! ')

calculator()