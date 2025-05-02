def is_even_or_odd(number):
    if type(number) != int:
        print(f'{number} is not an integer I can evaluate!')
        return
    
    if number % 2 == 0:
        print(f'{number} is even!')
    elif number % 2 != 0:
        print(f'{number} is odd!')

is_even_or_odd(4)
is_even_or_odd(5)
is_even_or_odd(4.5)
is_even_or_odd('ketchup')
