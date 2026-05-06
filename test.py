import base64

encoded = "YWtoaWw6MTIzNA=="
decoded = base64.b64decode(encoded).decode()

print(decoded)