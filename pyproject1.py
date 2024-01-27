print("your email id is: ")
email=input()
c=email.index('@')
print("name :",email[0:c]);
print("domain:",email[c:]);
