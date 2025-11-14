class Flowershop:
    min_florists = 1
    max_florists = 4
    def __init__(self, florists):
        if not isinstance(florists, list):
            raise ValueError (f"The names of a florist or florists need to be provided in a list.")
        if len(florists) < self.min_florists:
            raise ValueError (f"The shop needs to have at least {self.min_florists} florist.")
        if len(florists) > self.max_florists:
            raise ValueError (f"The shop needs to have at most {self.max_florists} florists.")
        self.florists = florists
