from .memory import Memory
from .crime_type import CrimeType

class Simulation:
    def __init__(self, criminal):
        self.criminal = criminal
        self.memories = []

    def add_memory(self, memory):
        self.memories.append(memory)

    def run_simulation(self):
        print(f"Running simulation for {self.criminal.name}")
        for memory in self.memories:
            print(f"Simulating: {memory}")
