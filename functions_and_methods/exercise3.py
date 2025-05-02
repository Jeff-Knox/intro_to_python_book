def multiply(first, second):
    return first * second

def get_num(num_count):
    return int(input(f'What is #{num_count} to multiply: '))

print(f'Result: {multiply(get_num(1), get_num(2))}')