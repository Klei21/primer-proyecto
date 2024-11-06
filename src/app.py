from datetime import *
from facade.user_Facade import *
from facade.vacation_Facade import *
userfacade = UserFacade()
vacationfacad = VacationFacade()
try:
    def start():
        print("What's your first action:\n \
                        1.log in\n\
                        2.create a new user\n ")
        action = int(input("What do you want to do?  "))
        if action==1:
            mail = input("Enter your mail: ")
            password = input("Enter your password: ")
            person = userfacade.log_in(mail,password)
            user = User.dictionary_to_User(person)
            user.display()
            next_action(user)
            
        elif action == 2:
            fn = input("Please enter your first name: ")
            ln = input("Please enter your last name: ")
            mail = input("Please enter your mail: ")
            check = userfacade.check_mail(mail)
            password = input("Please enter your password: ")
            person = User(None, fn, ln, mail, password)
            userId = userfacade.insert_person(person)
            user = userfacade.get_one_person(userId)
            user.display()
            next_action(user)

        else:
            print("Please enter a valid option")
            start()

    def next_action(user):
        val = int(input("What's your next action: \n\
                            1.Get your information\n\
                            2.Get everyone's inforation\n\
                            3.Update Your User\n\
                            4.Delete your user\n\
                            5.Create a vacation\n\
                            6.See your vacations\n\
                            7.See everyone's vacation\n\
                            8.Upadate your vacation\n\
                            9.delete your vacation\n\
                            10.Link an existing vacation to your account\n\
                            0.Log out\n"))
        if val==1:
                user.display()
                next_action(user)
        elif val==2:
            users = userfacade.get_all_persons()
            for useri in users:
                    useri.display()
            next_action(user)
        elif val==3:
                print(f"Past last name: {user.firstname}")
                fn = input("Enter new first name: ")
                print(f"Past last name: {user.lastname}")
                ln = input("Enter new last name: ")
                print(f"Your mail was: {user.mail}")
                mail = input("Enter new mail: ")
                print(f"Your last password was: {user.password}")
                password = input("Enter your new password: ")
                if fn=="" or ln=="" or mail=="" or password=="":
                    raise ValueError("There cannot be a blank parameter")
                userfacade.update_person(fn, ln, mail, password, user.userid)
                user = userfacade.get_one_person(user.userid)
                user.display()
                next_action(user)
        elif val==4:
                print("Remember to delete the vacation first!!!")
                vvacation = vacationfacad.check_vacationId(user)
                if len(vvacation)!=0:
                    print("You have active vacations, delete them first")
                    next_action(user)
                ver = int(input("Press 1 to delete the profile or 0 to cancel."))
                if ver == 1:
                    print(userfacade.delete_person(user.userid))
                    print("The deletion is complete!")
                    start()
                elif ver == 0:
                    pass
                else:
                    print("There was an error, please start again")
                next_action(user)
        elif val==5:
                copt = int(input("Which of the next countries:\n\
                                    1.Aregtina\n\
                                    2.Brazil\n\
                                    3.England\n\
                                    0.Other\n"))
                if copt == 0:
                    print("Please contact client service \
                        via whatsapp: ######## or mail: #####@###")
                desc = input("Enter the description of your vacation: ")
                since = input("Since what date (yyyy-MM-DD): ")
                exit_date = datetime.strptime(since, "%Y-%m-%d")
                till = input("Enter the date of return (yyyy-MM-DD): ")
                return_date = datetime.strptime(till, "%Y-%m-%d")
                if return_date < exit_date:
                      raise ValueError("The return date cannot be before the exit one")
                price = int(input("Enter the cost of the vacation: "))
                folder = input("Enter the name of the folder: ")
                vac = Vacation(None, copt, desc, exit_date, return_date, price, folder)
                print("This is your vacation ID: ",vacationfacad.insert_vacation(vac, user))
                next_action(user)
        elif val==6:
                vacation = vacationfacad.get_one_Vacation(user)
                for item in vacation:
                    item.display()
                next_action(user)
        elif val==7:
                vacation= vacationfacad.get_all_vacations()
                for vac in vacation:
                    vac.display()
                    print()
                next_action(user)
        elif val==8:
                vacation = vacationfacad.get_one_Vacation(user)
                for item in vacation:
                    item.display()
                vId = int(input("Please enter the vacation ID: "))
                copt = int(input("What is the new destination:\n\
                                    1.Aregtina\n\
                                    2.Brazil\n\
                                    3.England\n\
                                    0.Other\n"))
                if copt == 0:
                    print("Please contact client service \
                        via whatsapp: ######## or mail: #####@###")
                    start()
                desc = input("Enter the description of your vacation: ")
                since = datetime(input("New starting date (%Y-%m-%d): "))
                exit_date = datetime.strptime(since, "%Y-%m-%d")
                till = datetime(input("Untill (%Y-%m-%d): "))
                return_date = datetime.strptime(till, "%Y-%m-%d")
                if return_date < exit_date:
                      raise ValueError("The return date cannot be before the exit one")
                price = input("Enter the new cost of the vacation: ")
                folder = input("Enter the new name of the folder: ")
                print("This is your vacation ID: ",vacationfacad.update_Vacation(copt,desc,exit_date,return_date,price,folder, vId))
                next_action(user)
        elif val==9:
                vacation = vacationfacad.get_one_Vacation(user)
                for item in vacation:
                    item.display()
                vid = int(input("Which vacation ID:"))

                print("We just want to confirm")
                validation = int(input("Are you sure you want to delet the vacation?:\n\
                                1.Accept\n\
                                2.Cancel\n "))
                if validation==1:
                    vacationfacad.delete_vacation(user,vid)
                elif validation == 2:
                    pass
                else:
                    print("An error has ocurred please try again")
                next_action(user)
        elif val==10:
            vacation= vacationfacad.get_all_vacations()
            for vac in vacation:
                vac.display()
                print()
            vid = int(input("What's the vacation ID: "))
            vacationfacad.link_Vacation(vid, user)
            next_action(user)
        elif val==0:
                print("We expect to see you again soon!!!")
                vacationfacad.close()
                
        else:
                print("There has been an error, please atart again")
                next_action(user) 
    start()
except ValueError as err:
      print(err)
      start()
except FileNotFoundError as err:
      print(err)
      start()
except TypeError as err:
      print(err)
      start()
except Exception as err:
      print(err)
      start()
