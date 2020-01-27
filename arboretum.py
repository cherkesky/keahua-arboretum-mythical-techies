import os
from environments import River
from animals import RiverDolphin


class Arboretum:
    def __init__(self, name, address, avail_animals, avail_plants, avail_habitats):
        self.name = name
        self.address = address
        self.avail_animals = avail_animals
        self.avail_plants = avail_plants
        self.avail_habitats = avail_habitats
        self.habitats_dict = {habitat: [] for habitat in avail_habitats}

    @property
    def rivers(self):
        return self.__rivers

    def annex_river(self, river):
        self.__rivers.append(river)

    @property
    def grasslands(self):
        return self.__grasslands

    def annex_grassland(self, grassland):
        self.__grasslands.append(grassland)

    @property
    def mountains(self):
        return self.__mountains

    def annex_mountain(self, mountain):
        self.__mountains.append(mountain)

    @property
    def swamps(self):
        return self.__swamps

    def annex_swamp(self, swamp):
        self.__swamps.append(swamp)

    @property
    def forests(self):
        return self.__forests

    def annex_forest(self, forest):
        self.__forests.append(forest)

    @property
    def coastlines(self):
        return self.__coastlines

    def annex_coastline(self, coastline):
        self.__coastlines.append(coastline)

    def annex_habitat(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        for habitat in self.avail_habitats:
            print(f"{self.avail_habitats.index(habitat) + 1}. {habitat}")

        choice = input("Choose your habitat > ")

    # Add other biomes

        if choice == "5":
            habitat = River()

        if choice == "2":
            pass

        self.habitats_dict[type(habitat).__name__].append(habitat)
        print(self.habitats_dict[type(habitat).__name__][0].id)

    def release_animal(self, choice):
        if choice == "1":
            gecko = Gecko()
            habitats_arr = [forest for forest in self.habitats_dict["Forest"]]

        if choice == "2":
            dolphin = RiverDolphin()
            habitats_arr = [river for river in self.habitats_dict["River"]] + [coastline for coastline in self.habitats_dict["Coastline"]]

        if choice == "3":
            goose = Goose()
            habitats_arr = [grassland for grassland in self.habitats_dict["Grassland"]]

        if choice == "4":
            kikakapu = Kikakapu()
            habitats_arr = [river for river in self.habitats_dict["River"]] + [swamp for swamp in self.habitats_dict["Swamp"]]

        if choice == "5":
            pueo = Pueo()
            habitats_arr = [grassland for grassland in self.habitats_dict["Grassland"]] + [forest for forest in self.habitats_dict["Forest"]]

        if choice == "6":
            ulae = Ulae()
            habitats_arr = [coastline for coastline in self.habitats_dict["Coastline"]]

        if choice == "7":
            opeapea = Opeapea()
            habitats_arr = [forest for forest in self.habitats_dict["Forest"]] + [mountain for mountain in self.habitats_dict["Mountain"]]

        if choice == "8":
            spider = Spider()
            habitats_arr = [swamp for swamp in self.habitats_dict["Swamp"]]

        for i, v in enumerate(habitats_arr):
            print(f'{i + 1}. {type(v).__name__} {v.id}')

        print("Release the animal into which biome?")
        choice = input("> ")
        print(habitats_arr[int(choice)-1].id)

        animal_to_add = habitats_arr[int(choice)-1]
        class_animal_to_add = self.habitats_dict[type(animal_to_add).__name__]
        object_class_animal_to_add = class_animal_to_add[class_animal_to_add.index(animal_to_add)]
        print(dir(object_class_animal_to_add))

        if len(object_class_animal_to_add.animals) < object_class_animal_to_add.animal_limit: 
            object_class_animal_to_add.animals.append(animal_to_add)
            print(f"You have added an animal to {class_animal_to_add} {object_class_animal_to_add}")
        else:
            print("That habitat is already at it's max for animals. Please choose another habitat")

        print(class_animal_to_add[class_animal_to_add.index(animal_to_add)].animals)