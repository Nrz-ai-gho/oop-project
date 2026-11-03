class Phone:
    def __init__(self, brand, price, battery=100):
        self.brand = brand
        self.price = price
        self.battery = battery
        
            
    def info(self):
        print(f"Brand: {self.brand}, Price: {self.price}, Battery: {self.battery}")

    def call(self, minutes):
        battery_consumption = minutes * 1
        if self.battery >= battery_consumption:
            self.battery -= battery_consumption
            print(f"calling for {minutes} minutes. Battery left: {self.battery}%")
        else:
            print("Not enough battery to make the call.")
            
class SmartPhone(Phone):
    def __init__(self, brand, price, battery=100, os = None):
        super().__init__(brand, price, battery)
        self.os = os
        
    def info(self):
            super().info()
            print(f"Operating System: {self.os}")    
    
    def install_app(self, name):
        print(f"Install : {name}")
            

phone1 = SmartPhone('Samsung', 15000, 100, 'Android')
phone1.install_app("Instagramm")
phone2 = SmartPhone('Apple', 20000,100, 'iOS')
phone2.install_app('Telegramm')
phone3 = SmartPhone('Xiaomi', 18000, 100, 'Xiaomi HyperOS')
phone3.install_app('SnapChat')

phone1.info()
phone2.info()
phone3.info()

phone1.call(30)
phone2.call(30)
phone3.call(30)

