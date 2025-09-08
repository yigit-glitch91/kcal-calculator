print("\nWelcome to calorie calculator!!\n")

gender = input("Your gender(Male/Female): ").lower()
weight = float(input("Your weight: "))
height = float(input("Your height: "))
age = float(input("Your age: "))

if(gender == "male"):{
    print("Your metabolism speed is: " + str(66.5 + (13.75 * weight) + (5 * height) - (6.77 * age)) + " kcal")
}
    
elif(gender == "female"):{
    print("Your metabolism speed is:  " + str(655.1 + (9.56 * weight) + (1.85 * height) - (4.67 * age)) + " kcal")
}
    
else:{
    print("Something is wrong. Please try again...")
}


