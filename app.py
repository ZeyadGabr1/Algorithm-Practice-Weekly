from main_functions import Calculator

class App:

    @staticmethod
    def take_numbers():
        """Take From User Two Float Numbers And Return It"""

        #code

        while True:

            try:
                num1 = float(input("Enter The First Number : "))
                num2 = float(input("Enter The Second Number : "))

                return num1, num2
            
            except ValueError as v:
                print("Error: Enter Only Numbers Please")
                
    @classmethod
    def run(cls):

        """Program startup and control function"""

        #code

        while True:

            print("Options: ")
            print("-" * 25)

            print("1. Add ")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")
            print("-" * 25)

            choice = input("Enter Your Choice From The Options (1 - 5): ")

            if choice == "5":
                print("Exit Calculator.. Have A Good Day")
                break

            elif choice in ["1", "2", "3", "4"]:

                all_oprations = {"1" : Calculator.add,
                                 "2" : Calculator.subtract,
                                 "3" : Calculator.multiplication,
                                 "4" : Calculator.divide}
                
                num1, num2 = cls.take_numbers()
                
                print("*" * 20)
                reslut = all_oprations[choice](num1, num2)
                print(f"The Reslut = {reslut:.1f}")
                print("*" * 20)

            else:
                print(f"Error: Invalid Option :  '{choice}' ")



if __name__ == "__main__":
    App.run()