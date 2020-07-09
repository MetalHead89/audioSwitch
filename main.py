"""
Для работы программы необходим PyQt5.
Установить его можно командой sudo apt-get install python3-pyqt5 pyqt5-dev-tools

Если при запуске появляется ошибка:
qt.qpa.plugin: Could not find the Qt platform plugin "xcb" in ""
This application failed to start because no Qt platform plugin could be initialized. Reinstalling
the application may fix this problem.
В этом случае необходимо запустить программу в режиме дебага для выявления зависимостей. В терминале выполняем:
$ QT_DEBUG_PLUGINS=1
$ venv/bin/python main.py

В моём случае вывод был такой:
QFactoryLoader::QFactoryLoader() checking directory path "/usr/bin/platforms" ...
qt.qpa.plugin: Could not find the Qt platform plugin "xcb" in ""
This application failed to start because no Qt platform plugin could be initialized.
Reinstalling the application may fix this problem.

Как видно, ошибка появляется после того, как программа не может найти необходимый каталог "/usr/bin/platforms"
Для того чтобы исправить я создал символическую ссылку, указывающую на верный каталог "usr/lib/qt/plugins/platforms/",
следующей командой:
$ sudo ln -sf /usr/lib/qt/plugins/platforms/ /usr/bin/

После этого всё запустилось
"""
#!/bin/bash
import sys
from PyQt5 import QtWidgets
import mixer
import config
from tray_controller import TrayController

if __name__ == '__main__':
    mix = mixer.Mixer(config.SOUND_CARD_INDEX)  # Создание объекта микшер для нужной звуковой карты

    app = QtWidgets.QApplication(sys.argv)
    program = TrayController(mix)
    sys.exit(app.exec_())
