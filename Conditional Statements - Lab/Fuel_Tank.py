type_of_fuel = (input())
fuel_in_tank = float(input())

if type_of_fuel == "Diesel" or type_of_fuel == "Gas" or type_of_fuel == "Gasoline":
    if fuel_in_tank >= 25:
        print("You have enough "+ str.lower(type_of_fuel) +".")
    elif fuel_in_tank < 25:
        print("Fill your tank with " + str.lower(type_of_fuel) +"!")
else:
    print("Invalid fuel!")
