# Assignment 2 Question 2 (50%)
# Python Code From A Flowchart
# COMP 10001 - 000223441 | Michael Blair Statement Of Authorship 
# I michael blair, 000223441, certify that this work is my own effort and that i have no allowed anyone
# else to copy from it.
# Assume the user answer inputed at the keyboard will either be yes or no
# Test input: 1st trace: string 'YES' (without quotations). 
#             2nd trace: string 'NO' (without quotations),string  'YES' (without quotations)
#             3rd trace: string 'NO' (without quotations),string  'NO' (without quotations),string 'YES' (withoutquotations)
#             4th trace: string 'NO' (without quotations),string  'NO' (without quotations),string 'NO' (withoutquotations),string 'NO'
# (withoutquotations)


print("\tThe Phone Is Ringing")       
# Message signals the start of the program and is the first display message printed to user       

answer = input("\tYour cell phone rings...Are you asleep? (Yes/No)\n")
# Assignment expression of ans to user input 
# Tab display message 4 spaces to the right, and print the input message prompt to user, input will be printed on a new line.
 
if answer.lower() == "yes": 
# Condition check: to see if user input in all lower case, in response to ''Are You Asleep?''
# was equivalent to string 'yes'
    
    message = "You Are Asleep! You did not answer the phone due to being fast asleep (incapacitated)"
     # Yes answer string response, in response to Are you asleep? question stored in 'message' variable, to be returned at the end of the program

elif answer.lower() == "no":
    # Condition check: to see if user input in all lower case, in response to ''Are You Asleep?''
    # was equivalent to string 'no'
    answer = input("\tYour Mom is calling, will you answer Mom? (Yes/No)\n") 
    # Tab display message 4 spaces to the right, and print the input message prompt to user, input will be printed on a new line.

    if answer.lower() == "yes":   
    # Condition check to see if user input in all lower case, in response to ''Will You Answer Mom?''
    #  was equivalent to string 'yes'
    
        message = "You answered your Mom, who needs you to pick her up."
        # Yes answer string response, in response to mom  question stored in 'message' variable, to be returned at the end of the program

    elif answer.lower() == "no":
        # Condition check to see if user input in all lower case, in response to ''Will You Answer Mom?''
        #  was equivalent to string 'no'.
        answer = input("\tIs it Morning? (Yes/No)\n")
        # Tab display message 4 spaces to the right, and print the input message prompt to user, input will be printed on a new line.

        if answer.lower() == "yes":
            # Condition check to see if user input in all lower case, in response to 'Is it now morning?'
            #  was equivalent to string 'yes"
            message= "It's the morning, so you don't answer your phone."
            # Assignment statement of the above string, stored in message, in response
            # to user entering a yes response, to be output at the end of the program
            

        elif answer.lower() == "no":
            # Condition check to see if user input in all lower case, in response to ''Is it morning?''
            #  was equivalent to string 'no'.
            message= "Its not morning, so you answer your phone."
            # Assignment statement of the above string, stored in message, in response
            # to user entering a no response to be output at the end of the program

print(message)
#final message output to user at the end
#program ends here
