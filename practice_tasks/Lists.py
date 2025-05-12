from variables_data_types import animals
Sensors = ["Humidity sensor","Motion sensor", "Temperature sensor"]         #This is a list of sensors
print(Sensors)                                                              # Prints all the values of the list

print(Sensors[1])                                                           #The first index is 0, this allows you to access the values reffering to the index number

print(Sensors[0:2])                                                         #Range index - You can specify a range of indexes by specifying where to start and where to end the range.
                                                                            #The search starts at index 0 (included) and ends at index 2 (not included)
Sensors.insert(3,"Survaillance Cameras")                                    #The method insert() adds an item at the specified index

print(Sensors)                                                              #append() has the same function but adds the item to the end of the list

print(len(Sensors))                                                         #len() determines how many items are on the list
print(f" The {Sensors[1]} has been triggered, the lion {animals["Lion"]["animal_name"]} has escaped")m