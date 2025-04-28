my_dict = {
    'title': "Monty Python's Flying Circus",
    'cast': [
        'Eric Idle',
        'John Cleese',
        'Terry Gilliam',
        'Graham Chapman',
    ],
    'first_season': 1969,
    'last_season': 1974,
    'reboot_season': None,
}

cast_members = my_dict['cast']
print(cast_members[3])

my_dict['cast'].append('Michael Palin')

print(my_dict['cast'])
print(my_dict['cast'][-1])