from abc import ABC, abstractmethod


class Phone(ABC):
    def __init__(self, model, number):
        self.model = model
        self.number = number


class CallPhone(Phone):
    @abstractmethod
    def call(self, other_number):
        pass


class MessagePhone(Phone):
    @abstractmethod
    def send_message(self, other_number, text):
        pass


class PhotoPhone(Phone):
    @abstractmethod
    def take_photo(self):
        pass


class GamePhone(Phone):
    @abstractmethod
    def play_game(self, game):
        pass


class BasicPhone(CallPhone, MessagePhone):
    def call(self, other_number):
        print(f"Calling {other_number} from {self.number}")

    def send_message(self, other_number, text):
        print(f"Sending '{text}' to {other_number} from {self.number}")


class CameraPhone(BasicPhone, PhotoPhone):
    def take_photo(self):
        print(f"Taking a photo with {self.model}")


class SmartPhone(CameraPhone, GamePhone):
    def play_game(self, game):
        print(f"Playing {game} on {self.model}")


basic_phone = BasicPhone("BasicPhone", "123456789")
basic_phone.call("987654321")
basic_phone.send_message("987654321", "Hello")

camera_phone = CameraPhone("CameraPhone", "987654321")
camera_phone.take_photo()

smart_phone = SmartPhone("SmartPhone", "555555555")
smart_phone.play_game("Angry Birds")
