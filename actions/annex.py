import os
from environments import River


def annex_habitat(arboretum):
    os.system('cls' if os.name == 'nt' else 'clear')
    print("1. River")
    print("2. Swamp")
    print("3. Coastline")
    print("4. Grassland")

    choice = input("Choose your habitat > ")

# Add other biomes

    if choice == "1":
        river = River()

        arboretum.annex_river(river)
        print(arboretum.rivers[0].id)
    if choice == "2":
        pass
