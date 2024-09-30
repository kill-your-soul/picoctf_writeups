flag = input("Input flag: ")
res = ''
for i in range(0, len(flag), 2):
    combined_char = (ord(flag[i]) << 8) + ord(flag[i + 1])
    res += chr(combined_char)

# res = ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])
print(res)

