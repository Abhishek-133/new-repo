# creating the hash password
# import bcrypt
# password='passwordabc'
# bytes=password.encode('utf-8')
# salt=bcrypt.gensalt()
# hash=bcrypt.hashpw(bytes,salt)
# print(hash)

import bcrypt
password =input("Enter database stored value: ")
bytes=password.encode('utf-8')
salt=bcrypt.gensalt()
hash=bcrypt.hashpw(bytes,salt)
print(hash)
print("\n")
userPassword=input("Enter user entered value: ")
userBytes=userPassword.encode('utf-8')
salt=bcrypt.gensalt()
user=bcrypt.hashpw(userBytes,salt)
print(user)
result=bcrypt.checkpw(userBytes,hash)
print("\n")
print(result)
print("Abhishek")
