class course:
    def __init__(self, title, code, unit, is_requisite):
        self.title = title
        self.code = code
        self.unit = unit
        self.is_requisite = is_requisite

    def requisite(self):
        if self.is_requisite:
            return "You have to pass this Course before you register for next one"
        else:
            return "You are free to register for the next course"
