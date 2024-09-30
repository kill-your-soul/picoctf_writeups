# res = open('enc', 'r').readline()
# print(f)
res = input("Input enc flag: ")
original_flag = ''
for char in res:
    combined_value = ord(char)
    first_byte = (combined_value >> 8) & 0xFF  # старший байт
    second_byte = combined_value & 0xFF  # младший байт
    original_flag += chr(first_byte) + chr(second_byte)

print(original_flag)