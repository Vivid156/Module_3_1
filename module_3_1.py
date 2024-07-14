calls = 0
def count_calls ():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    text = string
    return(len(text)), text.upper(), text.lower()

def is_contains(string, list_to_search):
    count_calls()
    list_to_search1 = [a.upper() for a in list_to_search]
    if string.upper() in list_to_search1:
       print (True)
    else:
        print (False)

print (string_info('Capybara'))
print (string_info('Armaggedon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)


