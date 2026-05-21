message = 'Hello, World!'

print(message.upper())                           # HELLO, WORLD!  (all uppercase)
print(message.lower())                           # hello, world!  (all lowercase)

print(message.replace('World', 'Guys'))          # Hello, Guys!  (new string, original unchanged)
print(message)                                   # Hello, World!  (original is still the same)

replaced_message = message.replace('World', 'Guys')  # storing the new string in a variable
print(replaced_message)                          # Hello, Guys!

print(message.find('o'))                         # 4   (index of first 'o')
print(message.find('O'))                         # -1  (not found, case-sensitive!)
print(message.count('o'))                        # 2   (counts all occurrences)
print(len(message))  


greetings = 'Hello'  
name = 'ABC'

new_message = greetings + ' ' + name   + 'Welcome'    # 13  (total characters)
print(new_message)                        # Hello ABC