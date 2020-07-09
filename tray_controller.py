from PyQt5 import QtGui
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction, qApp


class TrayController:

    def __init__(self, mix):
        self.speaker_icon = '/home/metalhead/Документы/Programs/audioSwitch/images/speaker.png'
        self.headphone_icon = '/home/metalhead/Документы/Programs/audioSwitch/images/headphones.png'
        self.mix = mix
        self.state = 'Front'
        self.tray_icon = QSystemTrayIcon(QtGui.QIcon(self.speaker_icon))
        self.tray_icon.setToolTip('Audio Switch - fast switching sound output')
        self.tray_icon.activated.connect(self.switch_output)

        self.menu = QMenu()
        self.exit_action = QAction("Exit")
        self.exit_action.triggered.connect(qApp.quit)
        self.menu.addAction(self.exit_action)

        self.tray_icon.setContextMenu(self.menu)

        self.tray_icon.show()

    def switch_output(self):
        if self.state == 'Front':
            self.mix.turn_on_headphone()
            self.state = 'Headphones'
            self.tray_icon.setIcon(QtGui.QIcon(self.headphone_icon))
        else:
            self.mix.turn_on_speaker()
            self.state = 'Front'
            self.tray_icon.setIcon(QtGui.QIcon(self.speaker_icon))
