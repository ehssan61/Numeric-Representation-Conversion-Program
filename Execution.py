from Binary import Binary
from Ternary import Ternary
from Quaternary import Quaternary
from Octal import Octal
from Decimal import Decimal
from Duodecimal import Duodecimal
from Hexadecimal import Hexadecimal
from Vigesimal import Vigesimal
from Octodecimal import Octodecimal

class Execution:
    
    def main():
        while True:
            print()
            print("Welcome To The Numeric Representation Conversions")
            
            # Get user input for the number to be converted
            num = input("Enter the number you want to convert or 'q' to exit: ")
            
            if num =='q':
                break

            # Get user input for the base of the number
            # set the value to out of range number to loop running
            base_from = 0
            while base_from not in [2, 3, 4, 8, 10, 12, 16, 18, 20]:
                try:
                    base_from = int(input("Enter the base of the number you entered: "))
                    if base_from <= 0:
                        raise ValueError("Base cannot be negative or zero.")
                except ValueError:
                    print("Invalid input! Please enter a positive integer between 2 and 20.")
                else:
                    if base_from not in [2, 3, 4, 8, 10, 12, 16, 18, 20]:
                        print("Your base is not in range! Please choose base 2, 3, 4, 8, 10, 12, 16, 18, or 20.")
            
            base_to = 0
            while base_to not in [2, 3, 4, 8, 10, 12, 16, 18, 20]:
                try:
                    base_to = int(input("Enter the base you want to convert to: "))
                    if base_to <= 0:
                        raise ValueError("Base cannot be negative or zero.")
                except ValueError:
                    print("Invalid input! Please enter a positive integer between 2 and 20.")
                else:
                    if base_to not in [2, 3, 4, 8, 10, 12, 16, 18, 20]:
                        print("Your base is not in range! Please choose base 2, 3, 4, 8, 10, 12, 16, 18, or 20.")

            # Check which number class to use based on the base of the input number
            if base_from == 2:
                num_class = Binary(num)
            elif base_from == 3:
                num_class = Ternary(num)
            elif base_from == 4:
                num_class = Quaternary(num)
            elif base_from == 8:
                num_class = Octal(num)
            elif base_from == 10:
                num_class = Decimal(num)
            elif base_from == 12:
                num = str(num)
                num_class = Duodecimal(num)
            elif base_from == 16:
                num = str(num)
                num_class = Hexadecimal(num)
            elif base_from == 18:
                num = str(num)
                num_class = Octodecimal(num)
            elif base_from == 20:
                num = str(num)
                num_class = Vigesimal(num)

            ## Convert the number to the desired base and handle any errors
            try:
                result = num_class.convert_base(base_to)
            except ValueError as e:
                print(e)
            else:
                print("The equivalent number", num, "in base",base_to, "is", result)
                print()
            
if __name__ == "__main__":
    Execution.main()