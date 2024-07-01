def count_calls():
    global calls
    calls = calls + 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    matches = False
    for i in list_to_search:
        if(string.lower() != i.lower()):
            continue
        else:
             matches = True
    return matches


calls = 0

print(string_info('Capybara'))
print(calls)
print(string_info('Armageddon'))
print(calls)
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)


'''
(8, 'CAPYBARA', 'capybara')
1
(10, 'ARMAGEDDON', 'armageddon')
2
True
False
4
'''
