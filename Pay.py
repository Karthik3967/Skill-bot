from abc import ABC, abstractmethod
class Pay(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
class UPI(Pay):
    def pay(self,amount):
        print(f"paid : {amount} via UPI")
upi=UPI()
upi.pay(100)

