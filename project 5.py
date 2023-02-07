from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key) '''
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)


def view():
    with open('password.text', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,paswd = data.split("|")
            print("user:",user,"| password:",fer.decrypt(paswd.encode()).decode())
            



def add():
    name = input('account name: ')
    password = input("password: ")

    with open ('password.text','a') as f:
        f.write(name +"|" + fer.encrypt(password.encode()).decode() + "\n")


while True:
    mode = input("would you like to add a new password or view extsting ones ( view, add) press q to quit ?").lower()
    if mode == "q":
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue
