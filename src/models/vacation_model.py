class Vacation:
    def __init__(self,vacationid, countryid, description, since, through, price, folder):
        self.vacationid = vacationid
        self.countryid = countryid
        self.description = description
        self.since = since
        self.through =through
        self.price = price
        self.folder = folder
        if int(price)<=0 or int(price)>10000:
            raise ValueError("Your trip must cost between 1$ and 10000$")
    
    def display (self):
        print(f"Vacation ID: {self.vacationid}, country: {self.countryid}, description: {self.description}, since: {self.since}, until: {self.through}, price: {self.price}, folder: {self.folder}")

    @staticmethod 
    def dictionary_to_Vacation(dictionary):
        vacation = Vacation(dictionary["vacationId"], dictionary["country"], dictionary["description"], dictionary["since"], dictionary["through"], dictionary["price"], dictionary["folderName"])
        return vacation

    @staticmethod 
    def dictionaries_for_Vacations(list_of_dictionaries):
        vacations = [] 
        for item in list_of_dictionaries:
            vacation = Vacation.dictionary_to_Vacation(item)
            vacations.append(vacation)         
        return vacations
