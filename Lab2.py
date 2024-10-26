print("ET0735(DevOps for AIoT - Lab2 - Introduction to Python)")
# Function to display the main menu
def main():
    print("display_main_menu")
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
    tempList=get_user_input()
    average = calc_average(tempList)
    min_max = find_min_max(tempList)
    sortedTemp = sort_temperature(tempList)
    median = calc_median_temperature(tempList)
    
    print(f"The average is: {average}")
    print(f"The minimum and maximum temperatures are: {min_max[0]} and {min_max[1]} respectively")
    print(f"The sorted temperatures are: {sortedTemp}")
    print(f"The median temperature is: {median}")


# Function to get user input (returns a list of floats)
def get_user_input():
    inputByUser = input()
    splitInput = inputByUser.split(",")
    tempList = [float(temp.strip()) for temp in splitInput]
    return tempList  

# Function to calculate the average of a list
def calc_average(tempList):
    return sum(tempList)/len(tempList)  

# Function to find the minimum and maximum in a list (returns [min_temp, max_temp])
def find_min_max(tempList):
    minTemp=min(tempList)
    maxTemp=max(tempList)
    return [minTemp, maxTemp] 

# Function to sort the temperature list in ascending order
def sort_temperature(tempList):
    
    return sorted(tempList) 

# Function to calculate the median of the temperature list
def calc_median_temperature(tempList):
    print("calc_median_temperature")
    sortedTempList = sorted(tempList)
    lengthOfTempList = len(tempList)
    if lengthOfTempList % 2 == 1:  # Odd number
        return sortedTempList[lengthOfTempList // 2]
    else:  # Even number
        mid1 = sortedTempList[lengthOfTempList // 2 - 1]
        mid2 = sortedTempList[lengthOfTempList // 2]
        return (mid1 + mid2) / 2
    
    






if __name__ == "__main__":
 main()
