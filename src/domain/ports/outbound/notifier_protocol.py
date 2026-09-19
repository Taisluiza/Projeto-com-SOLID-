from abc import ABC, abstractmethod
from src.domain.value_object.phone import Phone
from src.domain.value_object.email import Email

class NotifyByCellPhone(ABC):
    @abstractmethod
    def send_message(self, message: str, number: str):
        pass

class NotifybyEmail(ABC):
    @abstractmethod
    def send_message(self, message: str, email: str):
        pass


