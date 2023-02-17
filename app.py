# Написать класс, который описывает электрический чайник с кнопкой включения и функцией автоматического выключения. 

# Поведение должно соответствовать реальному электрочайнику.

# Создать консольную программу, в которой при запуске можно "налить воды в чайник" и запустить его. 

# Другие параметры:

# - Количество воды задаётся  числом с плавующей точкой от 0 до 1.0;
# - Время закипания - 10 секунд;
# - Выводить сообщения при смене состояния (вкл, выкл, вскипел, остановлен);
# - Если чайник включен, выводить температуру чайника каждую секунду;
# - В любой момент пользователь может нажать кнопку, чтобы отключить чайник, в этом случае, программа завершится;

import time, keyboard

BOILING_TEMPERATURE = 100
AMBIENT_TEMPERATURE = 20

class ElectricKettle:
    def __init__(self):
        self.boiling_time = 10
        self.temperature = AMBIENT_TEMPERATURE
        self.max_water_amount = 1.0
        self.is_on = False
        self.water_amount = 0

    def __str__(self):
        return f'''Характеристики чайника:
                Количество воды: {self.water_amount} л
                Время закипания: {self.boiling_time} сек
                Текущая температура: {self.temperature} °C
                Режим: {'включен' if self.is_on else 'выключен'}
                '''

    def turn_on(self):
        self.is_on = True
        print('Чайник включен')

    def turn_off(self):
        self.is_on = False
        print('Чайник выключен')

    def boil(self):
        # температура линейно увеличивается c temperature до BOILING_TEMPERATURE
        print('Чайник нагревается')
        step = (BOILING_TEMPERATURE - AMBIENT_TEMPERATURE) / self.boiling_time
        for temperature in range(AMBIENT_TEMPERATURE, BOILING_TEMPERATURE, int(step)):
            self.temperature = temperature
            print(f'Температура: {self.temperature}')
            time.sleep(1)
            if keyboard.is_pressed('p'):
                self.turn_off()
                print(self)
                self.cool()
                print(self)
                exit()
        self.temperature = temperature = BOILING_TEMPERATURE
        print('Чайник вскипел')

    def cool(self):
        # температура линейно уменьшается c temperature до BOILING_TEMPERATURE
        step = (BOILING_TEMPERATURE - AMBIENT_TEMPERATURE) / self.boiling_time
        for temperature in reversed(range(AMBIENT_TEMPERATURE, BOILING_TEMPERATURE, int(step))):
            self.temperature = temperature
            print(f'Температура: {self.temperature}')
            time.sleep(1)
        self.temperature = temperature = self.temperature
        print('Чайник остыл')

    def get_is_on(self):
        return self.is_on

    def get_temperature(self):
        return self.temperature

    def get_water_amount(self):
        return self.water_amount

    def get_boiling_time(self):
        return self.boiling_time

    def set_water_amount(self, water_amount):
        # проверяем, что вода не превышает максимально возможное кол-во
        if water_amount > self.max_water_amount:
            print(f'Воды в чайнике не может быть больше {self.max_water_amount} л, лишняя вода пролилась')
        self.water_amount = water_amount

    def set_boiling_time(self, boiling_time):
        self.boiling_time = boiling_time

    def set_temperature(self, temperature):
        self.temperature = temperature

    def set_is_on(self, is_on):
        self.is_on = is_on


def main():
    # создаем чайник
    kettle = ElectricKettle()
    print(kettle)
    # наливаем воду
    try:
        water_amount = float(input('Налейте воду (введите кол-во воды): '))
    except ValueError:
        print('Введено некорректное значение, вода не налита')
        return
    kettle.set_water_amount(water_amount)
    print(kettle)
    print('Нажмите "P" (Power) для включения/выключения чайника')
    keyboard.wait('p')
    # включаем чайник
    kettle.turn_on()
    print(kettle)
    # нагреваем воду
    kettle.boil()
    print(kettle)
    # выключаем чайник
    kettle.turn_off()
    print(kettle)
    # чайник остывает
    kettle.cool()
    print(kettle)


if __name__ == '__main__':
    main()