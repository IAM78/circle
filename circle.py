print("\n Please enter the radius:")
r = float(input('R = '))
pi = 3.14

if 0<r :
    p = 2*pi*r
    a = pi*r**2
    print('\n Perimeter = ' + str(p))
    print('Area = ' + str(a))
else:
    print("Enter the radius of your circle greater than 0 ")