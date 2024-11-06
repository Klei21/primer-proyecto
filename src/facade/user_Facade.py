from logic.buisnes_logic import *

class UserFacade:
    def __init__(self):
        self.logic = User_logic() 

    def log_in(self, email, password):
        log = self.logic.log_in(email, password)
        return log
    
    def get_all_persons(self):
        persons = self.logic.get_all_persons()
        users = User.dictionaries_for_Users(persons)
        return users
    
    def check_mail(self, mail):
        verify = self.logic.check_mail(mail)
        return verify


    def insert_person(self, user):
        personId = self.logic.new_user(user)
        return personId

    def update_person(self, fname, lname, mail, password, person):
        row_count = self.logic.update_user(fname, lname, mail, password, person)
        return row_count

    def get_one_person(self, id):
        person = self.logic.get_one_person(id)
        user = User.dictionary_to_User(person)
        return user 

    def delete_person(self, id):
        row_count = self.logic.delete_person(id)
        return row_count
        
    def close(self):
        self.logic.close()