"""
создайте класс `Car`, наследник `Vehicle`
"""
from hw_2 import base
from hw_2.engine import Engine
class Car(base.Vehicle):
    def __init__(self, weight, fuel, fuel_consumption, engine=None):
        super().__init__(weight, fuel, fuel_consumption)
        self.engine = engine
    def set_engine(self, engine: Engine):
        try:
            if isinstance(engine, Engine):
                if not isinstance(engine.volume, (int, float)) or not isinstance(engine.pistons, int):
                    raise TypeError()
                self.engine = engine
                return self.engine
            else:
                raise TypeError()
        except TypeError as t:
            return 'ошибка в типе данных'


