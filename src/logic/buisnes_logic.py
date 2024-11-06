from utils.dal import *
from models.users_model import *
from models.users_model import * 
class User_logic:
    def __init__(self):
        self.dal = DAL()

    def log_in(self,email,password):
        sql = f"select userid, fname, lname, email, password from mydb.users where eMail='{email}' and password='{password}'"
        log = self.dal.log_in(sql)
        if log == None:
            raise ValueError("One of the parameters are wrong")
        return log

    def get_all_persons(self):
        sql = "SELECT userid,fname,lname,email,password FROM mydb.users"
        result = self.dal.get_table(sql)
        return result
    
    def get_one_person(self, id):
        sql = f"SELECT userid,fname,lname,email,password,rolename  \
                FROM mydb.users, mydb.roles \
                where mydb.users.roleid=mydb.roles.roleid and \
                mydb.users.userid={id};"
        result = self.dal.get_one(sql)
        return result

    def check_mail(self,mail):
        sql = f"select * from mydb.users where email='{mail}'"
        check = self.dal.get_one(sql)
        if check != None:
            raise ValueError("That mail already exists, please try again")
        return check

    def new_user(self,user):
        sql = f"insert into mydb.users (fname, lname, email, password, roleid) values ( '{user.firstname}', '{user.lastname}','{user.mail}','{user.password}',2)"
        adding = self.dal.new_param(sql)
        return adding
    
    def update_user(self,fname, lname, mail, password, userid):
        sql = f"update mydb.users set fname='{fname}', lname='{lname}', email='{mail}', password='{password}' where userid={userid}"
        update = self.dal.update(sql)
        return update
    
    def delete_person(self,id):
        sql = f"delete from mydb.users where userid={id}"
        delete = self.dal.delete(sql)
        return delete
    
    def close(self):
        self.dal.log_out()