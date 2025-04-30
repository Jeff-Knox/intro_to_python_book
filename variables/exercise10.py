obj = 42 # initializes
obj = 'ABcd' # reassigns
obj.upper() # mutates
obj = obj.lower() # reassigns
print(len(obj)) # neither
obj = list(obj) # reassigns
obj.pop() # neither
obj[2] = 'X' # mutates
obj.sort() # mutates
set(obj) # neither
obj = tuple(obj) # mutate