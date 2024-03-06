from logging_helper import log_method



class Property:
    MIN_PROPERTY_VALUE = 10000

    @log_method
    def __init__(self,value:int) -> None:
        self.value:int = value
        self._errors: list = {} 


    @log_method
    def is_valid(self) -> bool:
        if self.value < Property.MIN_PROPERTY_VALUE:
            self._errors['value'] = f"Property value must be greater than  {Property.MIN_PROPERTY_VALUE}."
            return False
        return True


    @log_method
    def errors(self) -> list:
        return self._errors


    @log_method
    def get_value(self) -> int:
        return self.value