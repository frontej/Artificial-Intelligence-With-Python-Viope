#This exercise tests out the default values of parameters. Create a program which has a main function and a subfunction called tester. The main function prompts user for an input "Write something (quit ends): " and sends this input to the subfunction as a parameter.
#Define the subfunction tester so that it has one parameter called "givenstring", which has the default value "Too short". If the user input is less than 10 characters, the program uses the default value and if 10 or more, it prints the usergiven input. If the user inputs "quit", the program is terminated.

def main():
    while True:
        userinput = input("Write something (quit ends): ")
        if(userinput == "quit"):
            break
        else:
            if(tester(userinput)):
                print("X spotted!")
            else:
                if((len(userinput) > 10)):
                    print(userinput)

def tester(givenstring="Too short"):
    if(len(givenstring) < 10):
        print("Too short")
        return False
    else:
        for i in givenstring:
            if i == "X":
                print(givenstring)
                return True
        else:
            return False

if __name__ == "__main__":
    main()
  
