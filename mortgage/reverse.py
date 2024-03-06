from .people import People
from .property import Property
from logging_helper import log_method

class ReverseMortgageManager:
    MAX_CAP = 1000000
    INDEX_MARGIN = 2.5
    MARGIN_LIST = [
        0, 0.5, 1, 2, 3, 4, 5, 6, 7, 8, 9
    ]

    @log_method
    def __init__(self, age: int, property_value: int) -> None:
        self.people = People(age=age)
        self.prop = Property(value=property_value)
        self._errors: list = {}
        self.principal_limit:int = 0


    @log_method
    def is_valid(self) -> bool:
        if not self.people.is_valid():
            self._errors.update(self.people.errors())
        if not self.prop.is_valid():
            self._errors.update(self.prop.errors())   

        return True if self._errors == {} else False
        

    @log_method
    def errors(self) -> list | None:
        return self._errors
    

    @log_method
    def get_max_cap(self) -> int:
        return ReverseMortgageManager.MAX_CAP if self.prop.get_value() > ReverseMortgageManager.MAX_CAP else self.prop.get_value() 

    @log_method
    def get_principal_limit(self) -> list:
        data = {}
        max_claim = self.people.get_max_claim() - ReverseMortgageManager.INDEX_MARGIN
        max_cap = self.get_max_cap()
        for margin in ReverseMortgageManager.MARGIN_LIST:
            data[margin] = max_cap * (max_claim - margin) 
        return data
    








    