# Statement Of Authorship - Michael L. Blair - TheBlairWizardProject
# This function will calculate & display the users avg of the two inputs in miles per gallon.

def mpg(numMiles,numGallons):
    mpg = numMiles / numGallons
    return(mpg)
x = int(input("Number of miles: "))
y = int(input("Number of gallons"))

print("Miles per gallon: ",mpg(x,y))
