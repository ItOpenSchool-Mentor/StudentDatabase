# न
# na = U+0928
#\u = 0000 to FFFF
#\U > FFFF 10000
#print("\u0928")

# utf-8
##a = "Hi".encode("utf-8")
##b = "न".encode("utf-8")
##print(f"a = {a}, Its Type : {type(a)}, & the Length : {len(a)}")
##print(f"b = {b}, Its Type : {type(b)}, & the Length : {len(b)}")

# utf-16
b = "न".encode("utf-16")
print(f"b = {b}, Its Type : {type(b)}, & the Length : {len(b)}")

# utf-32
b = "न".encode("utf-32")
print(f"b = {b}, Its Type : {type(b)}, & the Length : {len(b)}")
