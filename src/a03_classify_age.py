def classify_age(age):
    
    #Classifies the age into different categories.
    
    if not isinstance(age, int) or age < 0:
        return "Invalid age"
    elif age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 65:
        return "Adult"
    else:
        return "Elder"
