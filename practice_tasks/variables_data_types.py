class Sensor():
    def __init__(self, sensor_id, type, location):
        self.sensor_id = sensor_id
        self.type = type
        self.location = location


animals = {
    "Lion": {"animal_name": "Simba","cage": "Lions 1", "temperature": 27},
    "Elephant": {"animal_name": "Titan","cage":"Elephants 1", "temperature": 30}, 
     "Snake": {"animal_name": "Venom" , "cage": "Snakes 3", "temperature": 15}
}


humidity_sensor1 = Sensor(1, 'humidity', 'Lions 1')
print(humidity_sensor1.location)

    