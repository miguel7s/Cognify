from modelo.memory import Memory
from modelo.simulation import Simulation
from modelo.crime_type import CrimeType

class Controlador:
    def __init__(self):
        self.criminal = None
        self.simulation = None

    def crear_criminal(self, name, crime_type):
        self.criminal = Criminal(name, crime_type)
        self.simulation = Simulation(self.criminal)
        print(f"Created {self.criminal}")

    def crear_recuerdo(self):
        if self.criminal is None:
            print("No criminal selected.")
            return

        if self.criminal.crime_type == CrimeType.VIOLENT:
            memory = Memory("Experience as a victim")
        elif self.criminal.crime_type == CrimeType.FINANCIAL:
            memory = Memory("Consequences of financial crimes")
        elif self.criminal.crime_type == CrimeType.HATE:
            memory = Memory("Understanding diversity and respect")

        self.simulation.add_memory(memory)
        print(f"Memory added: {memory}")

    def iniciar_simulacion(self):
        if self.simulation:
            self.simulation.run_simulation()
        else:
            print("Simulation not initialized.")
