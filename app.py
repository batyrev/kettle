import keyboard
from kettle import ElectricKettle
from config import AMBIENT_TEMPERATURE

def main():
    # создаем чайник
    kettle = ElectricKettle()
    print(f'\nТекущая температура: {AMBIENT_TEMPERATURE} °C\n')
    print(kettle)
    # наливаем воду
    try:
        water_amount = float(input(f'Налейте воду (введите объем в литрах): '))
    except ValueError:
        print('Введено некорректное значение, вода не налита')
        return
    kettle.set_water_amount(water_amount)
    print('Нажмите "P" (Power) для включения/выключения чайника')
    keyboard.wait('p')
    # включаем чайник
    kettle.turn_on()
    # нагреваем воду
    kettle.boil()
    # выключаем чайник
    kettle.turn_off()
    # чайник остывает
    kettle.cool()


if __name__ == '__main__':
    main()