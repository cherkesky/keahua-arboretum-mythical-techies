from .habitat import Habitat
from interfaces import Identifiable


class Grassland(Habitat, Identifiable):

    def __init__(self):
        Habitat.__init__(self)
        Identifiable.__init__(self)
        self.plant_limit = 15
        self.animal_limit = 22

    def add_animal(self, animal):
        try:
            if animal.terrestrial:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError("Cannot add non-terrestrial animals to a grassland")

    def add_plant(self, plant):
        # try:
        #     if plant.freshwater:
        #         self.plants.append(plant)
        # except AttributeError:
        #     raise AttributeError("Cannot add plants that require non-fresh water to a grassland biome")
        self.plants.append(plant)