from .people import People
from .property import Property


class ReverseMortgageManager:
    MAX_CAP = 1000000

    def __init__(self, people: People, prop: Property) -> None:
        self.people = people
        self.prop = prop
        self._errors: list = {}
        self.principal_limit:int = 0


    def is_valid(self) -> bool:
        if not self.people.is_valid():
            self._errors.update(self.people.errors())
        if not self.prop.is_valid():
            self._errors.update(self.prop.errors())   

        return True if self.errors is {} else False
        

    def get_errors(self) -> list | None:
        return self._errors
    

    def get_max_cap(self) -> int:
        return ReverseMortgageManager.MAX_CAP if self.prop.get_value() > ReverseMortgageManager.MAX_CAP else self.prop.get_value() 

    def get_pl_factor(self) -> dict:
        return {
            'max_cap': self.get_max_cap(),
            'max_claim': self.people.get_max_claim(),
        }
    

    






    