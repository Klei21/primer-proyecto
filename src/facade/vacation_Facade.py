from logic.vacation_logic import * 

class VacationFacade:
    def __init__(self):
        self.logic = vacation_logic() 

    def check_vacationId(self,user):
        vid = self.logic.check_vacationId(user)
        return vid

    def get_all_vacations(self):
        vacations = self.logic.get_all_vacations()
        travels = Vacation.dictionaries_for_Vacations(vacations)
        return travels 
    
    def insert_vacation(self,vacation, user):
        vacationId = self.logic.new_vacation(vacation, user)
        return vacationId 

    def update_Vacation(self, countryid, description, since, through, price, folder, vacationid):
        row_count = self.logic.update_vacation(countryid, description, since, through, price, folder, vacationid)
        return row_count

    def get_one_Vacation(self, user):
        vacation = self.logic.get_one_vacation(user)
        if len(vacation) ==1:
            travel = Vacation.dictionary_to_Vacation(vacation)
        elif len(vacation) >=2:
            travel = Vacation.dictionaries_for_Vacations(vacation)
        return travel 

    def link_Vacation(self, vid,user):
        self.get_one_Vacation(user)
        conector = self.logic.link_vacation(vid,user)

    def delete_vacation(self, id, vid):
        row_count = self.logic.delete_vacation(id, vid)
        return row_count
        
    def close(self):
        self.logic.close()