number = 4936
ones = number % 10
number = number - ones

print(str(number) + ' ' + str(ones))

tens = number % 100
number = number - (tens * 10)

print(str(number) + ' ' + str(tens))

hundreds = number % 1000
number = number - (hundreds)

print(str(number) + ' ' + str(hundreds))

thousands = number % 10000
number = number - (thousands)

print(str(number) + ' ' + str(thousands))