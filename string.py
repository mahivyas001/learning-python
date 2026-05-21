message = 'Hello World'

print(message)        # Hello World  (full string)
print(message[0])     # H            (first character)
print(message[0:5])   # Hello        (index 0 to 4)
print(message[:5])    # Hello        (same as above, 0 is default)
print(message[0::2])  # HloWrd       (every 2nd character)
print(message[-1::-1]) # dlroW olleH (reversed!)
print(message[-1::-3]) # dWl         (reversed, every 3rd)