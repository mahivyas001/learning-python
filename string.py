message = 'Hello World'

print(message)        # Hello World  (full string)
print(message[0])     # H            (first character)
print(message[0:5])   # Hello        (index 0 to 4)
print(message[:5])    # Hello        (same as above, 0 is default)
print(message[0::2])  # HloWrd       (every 2nd character)
print(message[-1::-1]) # dlroW olleH (reversed!)
print(message[-1::-3]) # dWl         (reversed, every 3rd)



my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#          0, 1, 2, 3, 4, 5, 6, 7, 8, 9
#        -10,-9,-8,-7,-6,-5,-4,-3,-2,-1

# list[start:end:step]

# print my_list[::-1]


sample_url = 'http://xyzxyzxyzxyz.com'
print(sample_url)

# Reverse the url
print(sample_url[::-1])

# # Get the top level domain
print(sample_url[-4:])

# # Print the url without the http://
print(sample_url[7:])

# # Print the url without the http:// or the top level domain
print(sample_url[7:-4])
