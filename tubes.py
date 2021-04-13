# fungsi login
def login():
    while True:
        a = input("Username: ")
        p = input("Password: ")
        if a == "farrel" and p=="rel111":
            print("Logged in !\n")
            break
        else:
            print("Wrong Username/Password")

while True:
    a = input(">>> ")
    if a == 'login':
        login()
    elif a == 'exit':
        break

#hello world
