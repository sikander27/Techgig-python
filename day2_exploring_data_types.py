# For this challenge, you need to read a line from stdin and check whether it is of type integer, float or string.
# If input is-
#     Integer print 'This input is of type Integer.' to the stdout
#     Float print 'This input is of type Float.' to the stdout
#     String print 'This input is of type string.' to the stdout
#     else print 'This is something else.' to the stdout.

##################################Solution################################################################


def main():
    user_input = input()
    try:
        data_type = type(eval(user_input))
        if data_type == int:
            print("This input is of type Integer.")
        elif data_type == float:
            print("This input is of type Float.")
        else:
            print("This is something else.")
    except:
        print("This input is of type string.")
   

 # Write code here 

main()

