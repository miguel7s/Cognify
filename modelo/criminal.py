class Criminal:
    def __init__(self, name, crime_type):
        self.name = name
        self.crime_type = crime_type

    def __str__(self):
        return f"Criminal: {self.name}, Crime Type: {self.crime_type}"
