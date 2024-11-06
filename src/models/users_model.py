class User:
    def __init__(self,userid, firstname, lastname, mail, password):
        self.userid = userid
        self.firstname = firstname
        self.lastname = lastname
        self.mail = mail
        self.password = password
        if firstname=="" or lastname=="" or mail=="":
            raise TypeError("You must insert your information!")
        if len(password) <=4:
            raise TypeError("Your password must contain 4 characters")

    
    def display (self):
        print(f"Person ID: {self.userid}, Full name: {self.firstname} {self.lastname}, mail: {self.mail}")
    

    @staticmethod 
    def dictionary_to_User(dictionary):
        person = User(dictionary["userid"], dictionary["fname"], dictionary["lname"], dictionary["email"], dictionary["password"])
        return person

    @staticmethod 
    def dictionaries_for_Users(list_of_dictionaries):
        persons = [] 
        for item in list_of_dictionaries:
            person = User.dictionary_to_User(item)
            persons.append(person)         
        return persons 