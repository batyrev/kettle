# Написать класс, который описывает электрический чайник с кнопкой включения и функцией автоматического выключения. 

# Поведение должно соответствовать реальному электрочайнику.

# Создать консольную программу, в которой при запуске можно "налить воды в чайник" и запустить его. 

# Другие параметры:

# - Количество воды задаётся  числом с плавующей точкой от 0 до 1.0;
# - Время закипания - 10 секунд;
# - Выводить сообщения при смене состояния (вкл, выкл, вскипел, остановлен);
# - Если чайник включен, выводить температуру чайника каждую секунду;
# - В любой момент пользователь может нажать кнопку, чтобы отключить чайник, в этом случае, программа завершится;

import time

class ElectricKettle:
    def __init__(self, water_amount, boiling_time):
        self.water_amount = water_amount
        self.boiling_time = boiling_time
        self.temperature = 0
        self.is_on = False

    def __str__(self):
        return f'Water amount: {self.water_amount}\nBoiling time: {self.boiling_time}\nTemperature: {self.temperature}\nIs on: {self.is_on}'

    def turn_on(self):
        self.is_on = True
        print('Kettle is on')

    def turn_off(self):
        self.is_on = False
        print('Kettle is off')

    def boil(self):
        self.temperature = 100
        print('Kettle is boiling')

    def stop(self):
        self.temperature = 0
        print('Kettle is stopped')

    def get_temperature(self):
        return self.temperature

    def get_water_amount(self):
        return self.water_amount

    def get_boiling_time(self):
        return self.boiling_time

    def set_water_amount(self, water_amount):
        self.water_amount = water_amount

    def set_boiling_time(self, boiling_time):
        self.boiling_time = boiling_time

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_is_on(self, is_on):
        self.is_on = is_on


def main():
    water_amount = float(input('Enter water amount: '))
    boiling_time = int(input('Enter boiling time: '))
    kettle = ElectricKettle(water_amount, boiling_time)
    kettle.turn_on()
    kettle.boil()
    print(kettle)
    print('Kettle is boiling...')
    time.sleep(kettle.get_boiling_time())
    kettle.stop()
    print(kettle)
    kettle.turn_off()
    print(kettle)


if __name__ == '__main__':
    main()