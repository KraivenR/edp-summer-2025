Sensors = [
    {"type": "Humidity_sensor", "location":"Lions_cage", "sensor_ID":"1"},
    {"type": "Temperature_sensor", "location":"Elephants_cage", "sensor_ID":"2"},
    {"type": "Motion_sensor", "location":"Elephants_ cage", "sensor_ID":"3"}, 
    {"type": "Survailance_Camera", "location":"Entrance", "sensor_ID":"4"}
]

employees = {
    "E1":{"name":"John","Job_title":"Guard"}, 
    "E2":{"name":"Kraiven","Job_title":"Manager"}, 
    "E3":{"name":"Hannah","Job_title":"Zookeeper"}, 
    "E4":{"name":"George","Job_title":"Veterinarian"},
    "E5":{"name":"Nina","Job_title":"Technician" }

}

for sensor in Sensors:                                                                                                     #This is a loop that goes though each sensor on the list
    if sensor["type"] in "Humidity_sensor":                                                                                #This is the if statement, tha checks what sensor was triggered a nd who will attend
        for employee in employees.values():                                                                                #This is a loop that goes though each employee on the dictionary, we used the function values() to get just the value in the dictionary  
          for employee in employees.values():                                                                                 
            if employee["Job_title"] in ["Zookeeper", "Manager", "Veterinarian"]:                                          #Another if statement used to check what employee is resposible for the sensor triggered
                print("The manager was warn, dispatched the Zookeeper and Veterinarian to check on the animals.")          #Displays a message of the employee responding
                                                                                                                           #Indentation here is super important, it shows the program what code belongs together, and shows that the statements are in a loop.
    elif sensor["type"] in "Motion_sensor":
        for employee in employees.values():
            if employee["Job_title"] in ["Guard"]:
                print("ALERT MOTION SENSOR HAS BEEN TRIGGERED, POTENTIAL ESCAPE!!!, Guard dispatched")