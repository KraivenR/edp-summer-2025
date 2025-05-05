from variables_data_types import animals

a = "escaped from the cage"
b = "10 degrees celcius"
c = "cage is dirty"

print(f"The Lion {animals["Lion"]["animal_name"]}" +" " + a)
print(f"The  {animals["Snake"]["cage"]}" +" " + c)
print(f"The temperature from {animals["Elephant"]["cage"]} cage decreased from {animals["Elephant"]["temperature"]} to " + b)






