"""Exo design patterns (slide 84) : un exemple par famille de patterns."""
from abc import ABC, abstractmethod


# ------------------------------------------------------------ CREATIONAL
class Singleton:
    """Une seule instance partagee (ex : config)."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


class Button(ABC):
    @abstractmethod
    def render(self): ...


class WindowsButton(Button):
    def render(self): return "Windows button"


class MacButton(Button):
    def render(self): return "macOS button"


class ButtonFactory:
    """Factory : le client demande un type, pas une classe concrete."""
    @staticmethod
    def create(os_name):
        return {"windows": WindowsButton, "macos": MacButton}[os_name]()


class PizzaBuilder:
    """Builder : construction pas a pas, interface fluide."""
    def __init__(self):
        self._p = {"size": "M", "toppings": []}

    def size(self, s): self._p["size"] = s; return self
    def topping(self, t): self._p["toppings"].append(t); return self
    def build(self): return dict(self._p)


# ------------------------------------------------------------ STRUCTURAL
class EuropeanSocket:
    def voltage(self): return 230


class USPlug:
    def needs(self): return 110


class SocketAdapter:
    """Adapter : fait cohabiter deux interfaces incompatibles."""
    def __init__(self, socket): self.socket = socket
    def voltage(self): return self.socket.voltage() / 2.09  # transformateur


class Coffee:
    def cost(self): return 2.0


class MilkDecorator:
    """Decorator : ajoute un comportement sans heriter."""
    def __init__(self, coffee): self.coffee = coffee
    def cost(self): return self.coffee.cost() + 0.5


class SubsystemA:
    def run(self): return "A"


class SubsystemB:
    def run(self): return "B"


class Facade:
    """Facade : un point d'entree simple vers plusieurs sous-systemes."""
    def __init__(self): self.a, self.b = SubsystemA(), SubsystemB()
    def operate(self): return self.a.run() + self.b.run()


# ------------------------------------------------------------ BEHAVIORAL
class Subject:
    """Observer : notifie les abonnes quand l'etat change."""
    def __init__(self): self._obs = []
    def attach(self, fn): self._obs.append(fn)
    def set_state(self, v):
        for fn in self._obs:
            fn(v)


class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount): ...


class Card(PaymentStrategy):
    def pay(self, amount): return f"{amount} EUR par carte"


class Cash(PaymentStrategy):
    def pay(self, amount): return f"{amount} EUR en especes"


class Checkout:
    """Strategy : l'algorithme de paiement est interchangeable."""
    def __init__(self, strategy): self.strategy = strategy
    def pay(self, amount): return self.strategy.pay(amount)


class DataMiner(ABC):
    """Template Method : squelette fixe, etapes variables."""
    def mine(self):
        return [self.open(), self.parse(), self.close()]

    def open(self): return "open"
    @abstractmethod
    def parse(self): ...
    def close(self): return "close"


class CsvMiner(DataMiner):
    def parse(self): return "parse csv"


if __name__ == "__main__":
    assert Singleton() is Singleton()
    assert ButtonFactory.create("macos").render() == "macOS button"
    assert PizzaBuilder().size("L").topping("ham").build() == {"size": "L", "toppings": ["ham"]}
    assert MilkDecorator(Coffee()).cost() == 2.5
    assert Facade().operate() == "AB"
    got = []
    s = Subject(); s.attach(got.append); s.set_state(42)
    assert got == [42]
    assert Checkout(Card()).pay(10) == "10 EUR par carte"
    assert CsvMiner().mine() == ["open", "parse csv", "close"]
    print("Tous les patterns fonctionnent.")
