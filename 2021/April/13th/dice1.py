from cs50 import get_int

lookuptable = []

def calcnum(dice, total):
    # Make lookuptable global
    global lookuptable

    # Check if there is only one dice and check if it is possible
    if dice == 1:
        if total > 6 or total < 1:
            return 0
        else:
            return 1
       
    # Check if the dice and total can be found in the lookup table
    for item in lookuptable:
        if item[0] == dice and item[1] == total:
            return item[2]
    
    # If not found in lookup table calculate using calcnum
    output = 0
    for i in range(6):
        # Add output of using dice - 1 dice and getting a total of total minus the count
        # minus 1 (because the cound starts from 0)
        output += calcnum(dice - 1, total - i - 1)
    
    # Add to lookup table and already checked if in lookup table
    lookuptable.append([dice, total, output])
    
    # Output the output
    return output

# Try for the case where there is an keyword interruption
try:
    # Get dice and total
    dice = get_int("Dice: ")
    total = get_int("Total: ")

    # Print the output
    print(f"Possible combinations: {str(calcnum(dice, total))}")
except KeyboardInterrupt:
    exit()