# Transformation

### Given:
1. `res` — a string where each character is the result of combining two characters from the original `flag` string using bitwise operations.
2. algorithm of encryption

### Solution
1. Iterate over each character in `res`.
2. For each character, extract two bytes:
    - High byte: `(ord(char) >> 8) & 0xFF`
    - Low byte: `ord(char) & 0xFF`

3. Convert bytes back to characters and reconstruct the original flag.

```python
res = input("Input enc flag: ")
original_flag = ''
for char in res:
    combined_value = ord(char)
    first_byte = (combined_value >> 8) & 0xFF  # старший байт
    second_byte = combined_value & 0xFF  # младший байт
    original_flag += chr(first_byte) + chr(second_byte)

print(original_flag)
```