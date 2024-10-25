print("ET0735(DevOps for AIoT - Lab2 - Introduction to Python)")
# Function to display the main menu
def main():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    tempList=get_user_input()
    average = calc_average(tempList)
    min_max = find_min_max(tempList)
    
    print(f"The average is: {average}")
    print(f"The minimum and maximum temperatures are: {min_max[0]} and {min_max[1]}")


# Function to get user input (returns a list of floats)
def get_user_input():
    print("get_user_input")
    inputByUser = input()
    splitInput = inputByUser.split(",")
    tempList = [float(temp.strip()) for temp in splitInput]
    return tempList  

# Function to calculate the average of a list
def calc_average(tempList):
    print("calc_average")
    return sum(tempList)/len(tempList)  

# Function to find the minimum and maximum in a list (returns [min_temp, max_temp])
def find_min_max(tempList):
    print("find_min_max")
    minTemp=min(tempList)
    maxTemp=max(tempList)
    return [minTemp, maxTemp] 





if __name__ == "__main__":
 main()
