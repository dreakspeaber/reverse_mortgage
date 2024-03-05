


class Property:
    MIN_PROPERTY_VALUE = 10000

    def __init__(self,value:int) -> None:
        self.value:int = value
        self._errors: None|list = None 



    def is_valid(self) -> bool:
        if self.value < Property.MIN_PROPERTY_VALUE:
            self._errors['value'] = f"Property value must be greater than  {Property.MIN_PROPERTY_VALUE}."
            return False
        return True


    def errors(self) -> None|list:
        return self._errors


    def get_value(self) -> int:
        return self.value