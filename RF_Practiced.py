x = "Register your details"
print(x.upper())
details = input("Enter your name: ")
last_name = input("Enter your surname: ")
id_number = input("Enter your ID:" )
department = input("Which department do you work for? ")
year_start = input("Enter year started working in " + department )
year_end = input("Enter year you last worked in " + department )
expiriance = int(year_end) - int(year_start)

print("**************************")

print("BELOW CONFIRM YOUR DETAILS")

print("Name: " + details)
print("Surname: " + last_name)
print("ID: " + str( id_number))
print("Department: "+ department)
print("Expirience: " + str(expiriance))


