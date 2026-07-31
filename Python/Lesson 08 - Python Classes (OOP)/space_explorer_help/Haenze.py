###SPACECRAFT EXAMPLE####

# class Spacecraft():
#     # Step 1: Define a class named Spacecraft with an initializer that accepts: name, fuel level, & fuel efficiency
   
#     def __init__(self, name: str, fuel_level: float, fuel_efficiency: float):
#           pass

    
#     # Step 2: Create methods to: Add fuel, Calculate the fuel required for a given distance, Check if enough fuel is available to travel that distance, & Launch the spacecraft and deduct fuel if successful
    
#     def add_fuel(self, amount: float) -> None:
#           pass

#     def required_fuel(self, amount: float) -> float:
#           pass

#     def available_fuel(self, distance: float) -> bool:
#           pass

#     def launch(self, distance: float) -> None:
#          pass











####Planet in-class example

#Define a class Planet with an initializer that sets:
    #name: planet’s name
    #coordinates: the x, y, z coordinates of the planet
    #danger: difficulty of completing missions
    #resources: reward value
    #atmosphere: descriptive text



import random

class Planet():

    def __init__(self, name: str, coordinates: tuple[float,float,float], danger: float, resources: float, atmosphere: bool):
         self.name = name
         self.coordinates = coordinates
         self.danger = danger
         self.resources = resources
         self.atmosphere = atmosphere


    def __str__(self) -> str:
        # when you print out a planet object, what do you want it to look like?
        # return that string
        return f"{self.name} is a {self.atmosphere} planet with coordinates {self.coordinates}, danger level {self.danger}, and has {self.resources} resources."

    
    def __sub__(self, other) -> float:
        # calculate the distance between this planet object (self) and another planet object (other)
        if not isinstance(other, Planet):
            raise TypeError("Must only subtract planets.")

        x1, y1, z1 = self.coordinates
        x2, y2, z2 = other.coordinates

        return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5


#Code to check if str and sub methods are working correctly
if __name__ == "__main__":
    earth = Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")
    mars = Planet("Mars", (227.9, 0.0, 1.0), 1, 20, "Thin")
    print(earth-mars)  # Should print the distance between Earth and Mars
        

    def can_do_mission(self) -> bool:
        # can the player do anymore missions here?
        pass

    def record_mission(self, player_name: str) -> None:
        # record when a player has done missions here
        pass

    def mission_success(self) -> tuple[str, float]:
        # calculate a mission's outcome
        # should return a mission status and the number of resources gathered
        pass


# Planet("Earth", (149.6, 0.0, 0.0), 0, 0, "Earth-like")
# Planet("Mars", (227.9,   0.0,    1.0), 1, 20, "Thin")
# Planet("Jupiter", (778.5,  50.0,   12.0), 3, 40, "Gas Giant")
# Planet("Saturn", (1434.0, -80.0,  -20.0), 2, 35, "Gas Giant")
# Planet("Uranus", (2871.0,  30.0,   40.0), 2, 45, "Icy")
# Planet("Neptune", (4495.0, -25.0,   70.0), 4, 50, "Icy")
# Planet("Pluto", (5906.0, 120.0,  -90.0), 5, 60, "Frozen")
# Planet("Eris", (10100.0, 200.0, -130.0), 4, 55, "Frozen")
# Planet("Kepler-22b", (600000.0,  0.0,   0.0), 3, 70, "Earth-like")
# Planet("Proxima b", (402080.0, 30.0,  10.0), 5, 80, "Unknown")


