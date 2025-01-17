#Alex Meador
#CS 161 week 2 homework assignment

#1
#The error I got was "TypeError: 'float' object cannot be interpreted as an integer"
x = 18
print(x, bin(x), hex(x))

y = 0b1011
z = 0xA3
print(y, z)

w = x + y + z
print("the sum is" , w)

#2 - compression

original_size = 240
dictionary_size = 25
compressed_text_size = 148

percent_of_compression = 1-((compressed_text_size + dictionary_size)/original_size)
print(f"Compressed text size: {compressed_text_size} characters")
print(f"     Dictionary size: {dictionary_size} characters")
print(f"               Total: {compressed_text_size + dictionary_size} characters")
print(f"Compressed text size: {compressed_text_size} characters")
print(f"  Original text size: {original_size} characters")
print(f"         Compression: {percent_of_compression * 100:.2f}%")

