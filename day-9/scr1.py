# Using encode()
text = "Hi"
data = text.encode()

print(f"text = {text} & its Type : {type(text)}")
print(f"data = {data} & its Type : {type(data)}")
print("=" * 50)

# Using decode()
rbd = b'Hi'
textt = rbd.decode()
print(f"rbd = {rbd} & its Type : {type(rbd)}")
print(f"textt = {textt} & its Type : {type(textt)}")

