class Motorcycle:
    is_engine_on = False
    is_headlight_on = False
    make = None
    model = None
    is_driving = False

    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return (f'{self.make} {self.model} with engine '
                f'{"on" if self.is_engine_on else "off"} and headlight '
                f'{"on" if self.is_headlight_on else "off"}')

    def turn_engine_on(self):
        print('Turning engine on')
        self.is_engine_on = True
    
    def turn_engine_off(self):
        print('Turning engine off')
        if self.is_driving:
            print('You tried to turn the engine off while driving, '
                  'and crashed')
            return

        self.is_engine_on = False
    
    def turn_headlight_on(self):
        print('Turning headlights on')
        self.is_headlight_on = True
    
    def turn_headlight_off(self):
        print('Turning headlights off')
        self.is_headlight_on = False
    
    def start_driving(self):
        if not self.is_engine_on:
            print("You can't drive without turning the engine on!")
            return
        
        print('Starting to drive')
        self.is_driving = True
    
    def stop_driving(self):
        print('Stopping')
        self.is_driving = False
    
    def lean(self, direction):
        if not self.is_driving:
            print('You leaned while not driving, and crashed!')
            return
        
        print(f'Leaning {direction}')
    
    def turn_handlebars(self, direction):
        print(f'Turning handlebars {direction}')
    
    def turn(self, direction):
        if direction == 'left':
            self.turn_handlebars('right')
            self.lean('left')
        elif direction == 'right':
            self.turn_handlebars('left')
            self.lean('right')
        else:
            print("Didn't understand that direction")


class Car:
    is_engine_on = False
    is_headlight_on = False
    make = None
    model = None
    is_driving = False

    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def __repr__(self):
        return (f'{self.make} {self.model} with engine '
                f'{"on" if self.is_engine_on else "off"} and headlight '
                f'{"on" if self.is_headlight_on else "off"}')

    def turn_engine_on(self):
        print('Turning engine on')
        self.is_engine_on = True
    
    def turn_engine_off(self):
        print('Turning engine off')
        if self.is_driving:
            print('You tried to turn the engine off while driving, '
                  'and crashed')
            return

        self.is_engine_on = False
    
    def turn_headlight_on(self):
        print('Turning headlights on')
        self.is_headlight_on = True
    
    def turn_headlight_off(self):
        print('Turning headlights off')
        self.is_headlight_on = False
    
    def start_driving(self):
        if not self.is_engine_on:
            print("You can't drive without turning the engine on!")
            return
        
        print('Starting to drive')
        self.is_driving = True
    
    def stop_driving(self):
        print('Stopping')
        self.is_driving = False
    
    def turn_steering_wheel(self, direction):
        print(f'Turning steering wheel {direction}')
    
    def turn(self, direction):
        if direction in ['left', 'right']:
            self.turn_steering_wheel(direction)
        else:
            print("Didn't understand that direction")