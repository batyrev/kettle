from flask import Flask
import keyboard
from os import path
from kettle import ElectricKettle
from config import logging
import db

app = Flask(__name__)
basedir = path.abspath(path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    path.join(basedir, 'kettle_states.db')

def main():
    # создаем (берем в руки) чайник
    kettle = ElectricKettle()
    logging.info("Чайник в руках")
    logging.info(kettle)
    db.create_state(kettle)
    # наливаем воду
    try:
        water_amount = float(input(f'Налейте воду (введите объем в литрах): '))
    except ValueError:
        logging.error('Введено некорректное значение, вода не налита')
        return
    water_amount = kettle.get_water_amount() + water_amount
    kettle.set_water_amount(water_amount)
    db.create_state(kettle)
    print('Нажмите "P" (Power) для включения/выключения чайника')
    keyboard.wait('p')
    # включаем чайник
    kettle.turn_on()
    db.create_state(kettle)
    keyboard.add_hotkey('p', kettle.turn_off)
    kettle.boil()
    db.create_state(kettle)
    kettle.cooling()
    db.create_state(kettle)


if __name__ == '__main__':
    main()