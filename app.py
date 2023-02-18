from flask import Flask
import keyboard
from os import path
from kettle import ElectricKettle
import db

app = Flask(__name__)
basedir = path.abspath(path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    path.join(basedir, 'kettle_states.db')

# создаем чайник
kettle = ElectricKettle()

def main():
    # запишем в базу данных начальное состояние чайника
    db.create_state(kettle)
    print(f'\nТекущая температура: {kettle.get_temperature()} °C\n')
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
    # запишем в базу данных состояние чайника после нагревания
    db.create_state(kettle)
    kettle.cooling()


if __name__ == '__main__':
    main()