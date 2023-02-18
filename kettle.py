import time, keyboard
from config import *

class ElectricKettle:
    def __init__(self):
        self.boiling_time = BOILING_TIME
        self.temperature = AMBIENT_TEMPERATURE
        self.max_water_amount = MAX_WATER_AMOUNT
        self.min_water_amount = MIN_WATER_AMOUNT
        self.water_amount = INITIAL_WATER_AMOUNT
        self.is_on = False

    def __str__(self):
        return  f"Характеристики чайника:\n" \
                f"Допустимый объем воды в чайнике: от {self.min_water_amount} до {self.max_water_amount} л\n" \
                f"Время закипания: {self.boiling_time} сек\n\n" \
                f"Текущее состояние:\n" \
                f"Количество воды: {self.water_amount} л\n" \
                f"Текущая температура: {self.temperature} °C\n" \
                f"Режим: {'включен' if self.is_on else 'выключен'}\n" \

    def turn_on(self):
        self.is_on = True
        print('Чайник включен')
        keyboard.add_hotkey('p', self.turn_off)
        self.boil()

    def turn_off(self):
        keyboard.remove_all_hotkeys()
        self.is_on = False
        print('Чайник выключен')
        self.cool()

    def boil(self):
        print('Чайник нагревается')
        # температура линейно увеличивается c AMBIENT_TEMPERATURE до BOILING_TEMPERATURE
        step = (BOILING_TEMPERATURE - AMBIENT_TEMPERATURE) / self.boiling_time
        for temperature in range(AMBIENT_TEMPERATURE, BOILING_TEMPERATURE + 1, int(step)):
            if self.is_on is False:
                time.sleep((self.temperature - AMBIENT_TEMPERATURE) / step + 1)
                return
            self.set_temperature(temperature)
            time.sleep(1)
        print(f'Чайник вскипел, температура: {self.temperature} °C')
        self.turn_off()

    def cool(self):
        print('Чайник остывает')
        start_temperature = self.temperature
        if start_temperature != AMBIENT_TEMPERATURE:
            # температура линейно уменьшается c start_temperature до AMBIENT_TEMPERATURE
            step = (BOILING_TEMPERATURE - AMBIENT_TEMPERATURE) / self.boiling_time
            for temperature in reversed(range(AMBIENT_TEMPERATURE, start_temperature, int(step))):
                self.set_temperature(temperature)
                time.sleep(1)
        print(f'Чайник остыл, температура: {self.temperature} °C')

    def set_water_amount(self, water_amount):
        # проверяем, что объем воды лежит в нужном диапазоне
        if water_amount > self.max_water_amount:
            print(f'Воды в чайнике не может быть больше {self.max_water_amount} л, лишняя вода пролилась')
            self.water_amount = self.max_water_amount
            return
        elif water_amount <= self.min_water_amount:
            print(f'Введено некорректное значение, вода не налита')
            exit()
        self.water_amount = water_amount
        print(f'Новый объем воды в чайнике: {self.water_amount} л')

    def set_temperature(self, temperature):
        self.temperature = temperature
        print(f'Текущая температура: {self.temperature} °C')