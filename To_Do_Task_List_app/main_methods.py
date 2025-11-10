import datetime
from file_manger import  FileManger
from encrypt_decrypt import Encrypt_Decrypt


class To_do_tasks:

    data = FileManger.load_data()


    @classmethod
    def show_tasks(cls):

        if cls.data:
            print("-" * 15)
            print("Tasks :")
            print("-" * 25)


            for key, val in cls.data.items():

                print(f"Task Name : {key}")

                for key, value in val.items():

                    print(f"{key} :  {Encrypt_Decrypt.decrypt_text(value)}")

                print("-"* 25)


        else:
            print("-" * 15)
            print("No Tasks Found")
            print("-" * 15)


    @classmethod
    def take_task_data(cls):

        while True:

            task_name = input("Enter Task Name  (Enter 'e' To Exit):  ").lower()

            if task_name == 'e':
                break

            elif len(task_name) < 4:
                print("Error : The Task name Is too short")

            else:

                task_information = input("Enter Any Information About The Task : ")
                status = input("Enter Task Status : ")

                task_date = str(f"{datetime.datetime.now().ctime()}")

                

                cls.add_task(task_name, task_information, status, task_date)

                break


                
    @classmethod
    def take_task_name(cls):

        while True:

            task_name = input("Enter Task Name (Enter 'e' To Close): ").lower()

            if task_name == "e":
                return False
            
            elif task_name in cls.data:
                print("Task Alredy Found!")

            else:
                return task_name

    @classmethod
    def add_task(cls, task_name, task_information, status, task_date):
        secure_information = Encrypt_Decrypt.encrypt_text(task_information)
        secure_status = Encrypt_Decrypt.encrypt_text(status)
        secure_date = Encrypt_Decrypt.encrypt_text(task_date)


        cls.data[task_name] = {"Infromations" : secure_information,
                                 "Status" : secure_status,
                                 "date" : secure_date}
        

        FileManger.save_data(cls.data)
        print("Task Added Done ✅")



    @classmethod
    def remove_task(cls):   
        while True:
        
            task_name = cls.take_task_name()

            if task_name == False:
                break

            if task_name in cls.data:
                
                user_confirmation = cls.confirmation_to_remove_task()

                if user_confirmation == False:
                    pass

                else:

                    cls.data.pop(task_name)
                    FileManger.save_data(cls.data)
                    print(f"Task '{task_name}' Removed Done ✅")
                    break

            else:
                print("-" * 15)
                print("Task Not Found In Tasks ")
                print("-" * 15)
                break

    @staticmethod
    def confirmation_to_remove_task(task_name):
        
        choice = input(f"Are You Sure To Remove The Task '{task_name}'  (Y / N): ").lower()

        if choice == "y":
            return True
        
        else:
            return False


    @classmethod
    def edit_task(cls):

        while True:

            task_name = cls.take_task_name()

            if task_name == False:
                break

            elif task_name not in cls.data:
                print("Task Not Found")


            else:

                print("*" * 25)
                print("1. Edit Task Information")
                print("2. Edit Task status ")
                print("3. Exit")
                print("*" * 25)
                edit_choice = input("Options To Edit (1 - 3): ")

                if edit_choice == "1":

                    new_information = input("Enter The New Information About The Task : ")
                    print("Task information Changed Done ✅")

                    secure_new_information = Encrypt_Decrypt.encrypt_text(new_information)

                    cls.data[task_name]["Infromations"] = secure_new_information
                    FileManger.save_data(cls.data)
                    

                elif edit_choice == "2":
                    
                    new_task_status = input("Enter Task Status : ")
                    print("Task Status Changed Done ✅")

                    secure_new_task_status = Encrypt_Decrypt.encrypt_text(new_task_status)

                    cls.data[task_name]["Status"] = secure_new_task_status
                    FileManger.save_data(cls.data)

                else:
                    break




    @classmethod
    def download_tasks(cls):

        print("Download Your Tasks In Csv File...")

        task_names = []
        task_informations = []
        task_status = []
        tasks_date = []

        for key, val in cls.data.items():

            task_names.append(key)

            task_informations.append(Encrypt_Decrypt.decrypt_text(val['Infromations']))
            task_status.append(Encrypt_Decrypt.decrypt_text(val['Status']))
            tasks_date.append(Encrypt_Decrypt.decrypt_text(val["date"]))

        tasks_data = {"Task Name" : [name for name in task_names],
                      "Task Infromation" : [information for information in task_informations],
                      "Task Date" : [date for date in tasks_date]}
        
        while True:

            file_name = input("Enter The File Name:  ")

            reslut = FileManger.create_csv_file(tasks_data, file_name)

            if reslut == False:
                print("File Alredy Found")

            else:
                print("File Created Done ✅")
                break
            

            



def main_menu():

    while True:
        print("*" * 45)
        print("     Welcome In To Do List App  👋👋")
        print("*" * 45)

        print("Options: ")
        print("-" * 25)
        print("1. Show My Tasks  2. Add New Task ")
        print( )
        print("3. Remove Task   4. Edit Task")
        print( )
        print("5. Download My Tasks   6. Close")
        print( )

        choice = input("Enter your choice From Options (1 - 6) : ")

        

        if choice == "1":
            To_do_tasks.show_tasks()

        elif choice == "2":
            To_do_tasks.take_task_data()

        elif choice == "3":
            To_do_tasks.remove_task()

        elif choice == "4":
            To_do_tasks.edit_task()

        elif choice == "5":
            To_do_tasks.download_tasks()





main_menu()