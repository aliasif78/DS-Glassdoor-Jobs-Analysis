import re

# Extracts numerical values from a Salary entry
def extract_salary(entry):

    # Step 1 : Use regular expression to find all integers in the entry
    salaryBounds = re.findall(r'\d+', entry)
    
    # Step 2 : Find the Best Approximate Salary
    bestEstimate = ((int(salaryBounds[0]) + int(salaryBounds[-1])) / 2) * 1000

    # Step 3 : Check for Missing Entry
    if (bestEstimate == 1000):
        return -1
    
    return bestEstimate


# Extracts numerical values from a Employee Number entry
def extract_employeeNumber(entry):

    # Step 1 : Check for Max Entry & Unknown Entry
    if (entry == '10000+ Employees'):
        return '10000+'
    
    if (entry == 'Not Specified'):
        return 'Not Specified'

    # Step 2 : Use regular expression to find all integers in the entry
    number = re.findall(r'\d+', entry)
    
    # Step 3 : Find the Best Approximate
    bestEstimate = (int(number[0]) + int(number[1])) / 2
    
    return int(bestEstimate)


# To extract City & Country
def extractCityCountry(entry):

    # Step 1 : Check for Remote Jobs
    if (entry == 'Remote'):
        return ['Remote', 'Remote']

    # Step 2 : Extract City & Country
    temp = entry.split(',')

    # Step 3 : Check for Country not specified
    if (len(temp) == 1):
        return [temp[0], 'Not Specified']

    return temp