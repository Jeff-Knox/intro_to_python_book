def test_num(num):
    if num < 0:
        print(f'{num} is less than 0')
    elif num >= 0 and num <= 50:
        print(f'{num} is between 0 and 50')
    elif num >= 51 and num <= 100:
        print(f'{num} is between 50 and 100')
    elif num > 100:
        print(f'{num} is greater than 100')
    else:
        print('I have no clue what that number is')

test_num(-1)
test_num(0)
test_num(25)
test_num(50)
test_num(75)
test_num(100)
test_num(101)