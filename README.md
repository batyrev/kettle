﻿# kettle

Класс, который описывает электрический чайник с кнопкой включения и функцией автоматического выключения.

Поведение должно соответствовать реальному электрочайнику.

Создать консольную программу, в которой при запуске можно "налить воды в чайник" и запустить его.

Другие параметры:

- Количество воды задаётся  числом с плавующей точкой от 0 до 1.0;
- Время закипания - 10 секунд;
- Выводить сообщения при смене состояния (вкл, выкл, вскипел, остановлен);
- Если чайник включен, выводить температуру чайника каждую секунду;
- В любой момент пользователь может нажать кнопку, чтобы отключить чайник, в этом случае, программа завершится;

Дополнительно:

- логирование в файл
- документирование кода (комментарии)
- задать параметры чайника в файле конфигурации (время кипения, температура выклюения, количество воды не 1, а например, 2 и тд)
- писать все сообщения по дате в SQLite
- сделать его на Flask и задокументировать

Для работы нужно установить Python 3.7 и выше, SQLite3 а также библиотеки из файла requirements.txt, инициализировать БД (init_db.py)
