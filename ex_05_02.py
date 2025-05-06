largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num.lower() == 'done':
        break
    try:
        test= int(num)
        if largest is None or test > largest:
            largest = test
        if smallest is None or test < smallest:
            smallest = test
    except ValueError:
        print('Invalid input')
        
    
print('Maximum is', largest)
print('Minimum is', smallest)