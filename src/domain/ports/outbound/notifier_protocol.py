from abc import ABC, abstractmethod
from src.domain.value_object.phone import Phone

class NotifyByCellPhone(ABC):
    @abstractmethod
    def send_message(self, message: str, number: str):
        pass

class NotifybyEmail(ABC):
    @abstractmethod
    def send_message(self, message: str, email: str):
        pass