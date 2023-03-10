import logging
# настройки логирования
file_log = logging.FileHandler('logging.log', encoding='utf-8')
console_out = logging.StreamHandler()
logging.basicConfig(format = u'%(levelname)-8s [%(asctime)s] %(message)s',
                    level = logging.DEBUG,
                    handlers=(file_log, console_out))

# температура кипения воды
BOILING_TEMPERATURE = 100
# температура окружающей среды
AMBIENT_TEMPERATURE = 20

# время в секундах, за которое вода закипит
BOILING_TIME = 10
# максимальное количество воды в чайнике
MAX_WATER_AMOUNT = 1.0
# минимальное количество воды в чайнике
MIN_WATER_AMOUNT = 0.0
# начальное количество воды в чайнике
INITIAL_WATER_AMOUNT = 0.0
