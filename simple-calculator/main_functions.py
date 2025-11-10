class Calculator:

    @staticmethod
    def add(first_num : float, second_num : float):

        """Take Two Numbers And Return The Sum"""

        #code

        return first_num + second_num
    


    @staticmethod
    def subtract(first_num : float, second_num : float):
        
        """Take Two Numbers And Return The remainder of the subtract"""

        #code

        return first_num - second_num
    
    @staticmethod
    def divide(first_num : float, second_num : float):

        """Take Two Numbers And Return The remainder of the division"""

        #code

        if second_num == 0:
            raise ZeroDivisionError  # if second number is 0 make a ZeroDivisionError
        
        return first_num / second_num
    

    @staticmethod
    def multiplication(first_num : float, second_num : float):

        """Take Two Numbers And Return Reslut of multiplication"""
        #code

        return first_num * second_num
    
    


            