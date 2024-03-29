from logging_helper import log_method


class People:
    MIN_AGE = 62
    MAX_CLAIM_DICT = {
        62 : 38,
        70 : 50,
        80 : 60,
        90 : 80 
    }

    @log_method
    def __init__(self, age:int) -> None:
        self.age : int = age
        self.max_claim:int = 0
        self._errors : list = {}
        

    @log_method
    def is_valid(self) -> bool:
        if self.age < People.MIN_AGE:
            self._errors['min_age'] = f"Minimum age to avail the feature is {People.MIN_AGE} years"
            return False
        return True
    

    @log_method
    def errors(self) -> list:
        return self._errors
    
    @log_method
    def get_max_claim(self) -> int:
        # returns the maximum claim percentage as a function of age
        if self._errors != {}:return self.max_claim
        curr_age_band = 0
        for age_band,claim in People.MAX_CLAIM_DICT.items():
            if self.age >=age_band and curr_age_band < age_band:
                self.max_claim, curr_age_band = claim, age_band

        return self.max_claim


    