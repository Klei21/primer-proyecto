from utils.dal import *
from models.vacation_model import *

class vacation_logic:
    def __init__(self):
        self.dal = DAL()
    
    def check_vacationId(self, user):
        sql = f"select vactionId from mydb.likes where travelerid = {user.userid}"
        result = self.dal.get_one(sql)
        return result

    def new_vacation(self, vacation, user):
        sql = f"insert into mydb.vacations (countryid, description, since, through, price, folderName) values ( {vacation.countryid}, '{vacation.description}','{vacation.since}','{vacation.through}',{vacation.price},'{vacation.folder}')"
        adding = self.dal.new_param(sql)
        linked = self.link_vacation(adding,user)
        return adding
    
    def link_vacation(self, vid, user):
        sql = f"insert into mydb.likes (vactionId, travelerId) values ({vid}, {user.userid});"
        link = self.dal.new_param(sql)
        return link

    def update_vacation(self,countryid, description, since, through, price, folder, vId):
        sql = f"update mydb.vacations set countryid={countryid}, description='{description}', since='{since}', through='{through}', price={price}, folderName='{folder}' where vactionId ={vId}"
        update = self.dal.update(sql)
        return update
    
    def delete_vacation(self,user,vid):
        sql = f"delete from mydb.likes where travelerid={user.userid} and vactionId={vid}"
        delete = self.dal.delete(sql)
        return delete
    
    def get_one_vacation(self, user):
        sql = f"SELECT vacationId, country, description, since, through, price, folderName FROM mydb.countries, mydb.vacations, mydb.likes\
                where mydb.vacations.vacationId = mydb.likes.vactionId and mydb.vacations.countryId = mydb.countries.countryId and mydb.likes.travelerId = {user.userid} order by since asc"
        result = self.dal.get_one(sql)
        return result

    def get_all_vacations(self):
        sql = "SELECT vacationId, country, description, since, through, price, folderName FROM mydb.countries, mydb.vacations\
                where  mydb.vacations.countryId = mydb.countries.countryId order by since asc"
        table = self.dal.get_table(sql)
        return table
    
    def close(self):
        self.dal.log_out()

#  vacationId = (SELECT MAX(vacationId) FROM mydb.vacations) and