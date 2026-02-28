
class Chatbook:
    def __init__(self):
        self.email = ""
        self.passwd = ''
        self.loggedin = False
        self.menu()

    def menu(self):
        user_input = input("Welcome to chatbook Please choose an option !" \
        "1. Signup" \
        "2. Signin" \
        "3. Post an article" \
        "4. Press to exit")

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            pass
        else:
            exit()

    def signup(self):
        self.email = input("Please enter your email: ")
        self.passwd = input("Please enter your password: ")
        print("You have signedup successfully!!")
        print("\n")
        self.menu()   

    def signin(self):
        if self.email =='' and self.passwd == '':
            print("Please signup first by pressing 1 then login")
        else:
            uname = input("Please enter your username/email: ")
            pwd = input("Please enter your password: ")    
            if self.email == uname and self.passwd == pwd:
                print("You have signedin successfully!")
                self.loggedin = True
            else:
                print("Please input correct creds..")
        print("\n")
        self.menu() 
                            

obj = Chatbook()
