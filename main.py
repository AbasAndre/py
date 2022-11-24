username = "andre"
password = "123"

x = 1

while x == 1:

    a = input("username: ")
    b = input("password: ")

    if username == a and  password != b:
        print("password incorrect")
        x += 0
    elif username != a and password == b:
        print("username incorrect")
        x += 0
    elif username == a and password == b:
        print("username and password correct")
        break
    else:
        print("username and password incorrect")
        x += 0