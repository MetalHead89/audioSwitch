""" Класс объекта микшер """

import alsaaudio  # pip install pyalsaaudio


class Mixer:
    """
    control - объект в alsamixer, над которым необходимо получить управление
    cardindex - индекс звуковой карты в alsamixer
    """

    def __init__(self, sound_card_index):
        """ Инициализация микшера """

        # Инициализация фронтального выхода
        self.alsa_mixer_speaker = alsaaudio.Mixer(control='Front', cardindex=sound_card_index)
        # Инициализация выхода для наушников
        self.alsa_mixer_headphone = alsaaudio.Mixer(control='Headphone', cardindex=sound_card_index)
        self.turn_on_speaker()  # Переключить вывод звука на фронтальный выход

    def turn_on_speaker(self):
        """ Переключает вывод звука на фронтальный выход """

        self.alsa_mixer_speaker.setvolume(100)  # Поднимает фронтального выхода до 100
        self.alsa_mixer_headphone.setvolume(0)  # Убавляет громкость выхода наушников до 0

    def turn_on_headphone(self):  # Переключает громкость на выход наушников
        """ Переключает вывод звуку на выход для наушников """
        self.alsa_mixer_speaker.setvolume(0)  # Убавляет громкость фронтального выхода до 0
        self.alsa_mixer_headphone.setvolume(100)  # Поднимает громкость выхода наушников до 100
