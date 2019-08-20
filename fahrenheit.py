#Program that converts Celsius to Fahrenheit
#Michael Doan

check = 1
while check == 1:
    userTemperature = int(input("Please enter your temperature in Celsius: "))
    userTemperature = userTemperature * 1.8 + 32
    print("Your temperature in Fahrenheit is ", userTemperature)
    endProgram = input("Are you satisfied(y/n)? ")
    if endProgram == "y":
        print("Thank you for using this program")
        check = 0
    elif endProgram == "n":
                print("Okay")
                
    
    
