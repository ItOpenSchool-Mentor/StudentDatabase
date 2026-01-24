# Use Case No. 3
# 5
# 1. as int value 5
# 2. as hex bytes literal : b'\x05'
# 3. as ascii bytes literal : b'5'

a = 5
b = b'\x05'
c = b'5'

print(f"a = {a}, Value = {a}, Type = {type(a)}")
print(f"b = {b}, Value = {ord(b)}/{b[0]}, Type = {type(b)}")
print(f"c = {c}, Value = {ord(c)}/{c[0]}, Type = {type(c)}")
