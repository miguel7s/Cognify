class ConfigSingleton:
    _instance = None

    @staticmethod
    def get_instance():
        if ConfigSingleton._instance is None:
            ConfigSingleton._instance = ConfigSingleton()
        return ConfigSingleton._instance

    def __init__(self):
        if ConfigSingleton._instance is not None:
            raise Exception("This class is a singleton!")
        self.settings = {"simulation_speed": "fast"}

    def __str__(self):
        return f"Config Settings: {self.settings}"
