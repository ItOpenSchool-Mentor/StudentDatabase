# Use case #2: Creating hex escape bytes literal
# 233 = e9
print("\u00e9")
print(ord("\u00e9"))
print("=" * 50)

b = b'\xe9'

print(f"b = {b}, Value = {ord(b)} & {b[0]}, Char : {chr(ord(b))}")

