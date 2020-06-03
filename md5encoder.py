import hashlib

mystring = input("Enter a string to Hash:")
hashed_obj = hashlib.md5(mystring.encode())
print(hashed_obj.hexdigest())
print(len(hashed_obj.hexdigest()))
