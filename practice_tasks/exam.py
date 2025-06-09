#Event driven system


cage_quality_channel = []
security_channel = []
animal_condition =[]
class Event:
    def __init__(self, name):
        self.name = name
    

class Sensor:
    def __init__(self, name, sensor_type, location):
        self.name = name
        self.sensor_type = sensor_type
        self.location = location

class Employees:
    def __init__(self, name, id_number, role):
        self.name = name
        self.id_number = id_number
        self.role = role

def dispatch():
    if Event == g

zookeper1 = Employees('Kraiven', 1, 'zookeper1')
guard1 = Employees('John', 2, 'guard1')  
vet1 = Employees('Anna', 3, 'vet1')

feed_animals = Event('feed the animals')
animal_sick = Event('check the animal condition')
clean_the_cage = Event('clean the elephants cage 1')

Motion_sensor = Sensor('motion', 'motion_sensor', 'entrance')
Temperature_sensor = Sensor('temperature_check','temperature_sensor', 'Lions cage 1')
Survailance_camera = Sensor('Cams', 'survailance_camera', 'elephants cage 1')


