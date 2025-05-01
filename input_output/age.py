age = int(input('Hello, how old are you? '))
AGE_STEP = 10

# Should store theoretical age in a separate variable
age += AGE_STEP
print(f'In {AGE_STEP}, you will be {age}')
age += AGE_STEP
print(f'In {AGE_STEP * 2}, you will be {age}')
age += AGE_STEP
print(f'In {AGE_STEP * 3}, you will be {age}')
age += AGE_STEP
print(f'In {AGE_STEP * 4}, you will be {age}')