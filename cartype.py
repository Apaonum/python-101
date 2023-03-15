class Cartype:
    # Attribute
    cartype = 'Answer the questions for generate cartype'
    # Constructor
    def __init__(self, engine_type,fuel_type, sunroof_type, wheel_type):
        #print('Show this message when Instance was built')
        self.engine_type = engine_type
        self.fuel_type = fuel_type
        self.sunroof_type = sunroof_type
        self.wheel_type = wheel_type

    # Method
    def type_check(self):
        if self.engine_type == 'Diesel' and self.fuel_type == 'Diesel' and self.sunroof_type == 'No' and self.wheel_type == '2WD':
            print('Car Type is A')
        

if __name__== "__main__":
    cartype01 = Cartype('Diesel', 'Diesel', 'No', '2WD')
    print(cartype01.type_check())