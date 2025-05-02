def to_upper(sentence):
    if len(sentence) > 10:
        return sentence.upper()
    else:
        return sentence

test1 = 'Hello world!'
test2 = 'goodbye!'

print(to_upper(test1))
print(to_upper(test2))