#def get_numbers_from_user():
#    num1, num2 = map(int, input("please enter two numbers\n" ).split())
#    num1, num2 = input("please enter two numbers\n" ).split()
#    num1, num2 = int(num1), int(num2)
    while (True):
        try:
            num1 = int(input("please enter the first number\n" ))
            break
        except ValueError:
            print("please enter an integer number")
            
    while True:
        try:
            num2 = int(input("please enter the second number\n" ))
            break
        except ValueError:
            print("please enter an integer number")
    
    mult = num1 * num2
    print(mult)

get_numbers_from_user()

def check_input_is_numeric(number):
    if(type(number) == int or float):
        return True
    else:
        return False
    
  
