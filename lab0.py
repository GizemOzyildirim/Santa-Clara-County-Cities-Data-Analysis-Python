# Lab 0: Review CIS 41A
# Name: Gizem Ozyilririm

import csv


class Cities:

    """
    A class that helps manage and look up information about cities in Santa Clara County.
    It manages to find information about city populations, 
    
    """
     
    def __init__(self, filename):
        """
        Initializes the Cities object by loading city data from a specified CSV file.
        
        Args:
            filename (str): The path to the CSV file containing city data.
        """
        self.cities = {}
        # Read city data from file
        try:
            with open(filename, 'r') as file:
                for line in file:
                    fields = line.strip().split(',')
                    name = fields[0].strip()
                    population = int(fields[1].strip())
                    area = float(fields[2].strip())
                    self.cities[name.lower()] = {"name": name, "population": population, "area": area}
        except FileNotFoundError as e:
            print(f"Error: The file '{filename}' does not exist. {e}")
            raise SystemExit(1)

    def lookup(self, name):
        """
        Displays the population and area of a city by name.
        
        Args:
            name (str): The name of the city to look up.
        """
        city = self.cities.get(name.lower())
        if city:
            print(f"{city['name']}: {city['population']:,d}, {city['area']} sq mi")
        else:
            print(f"{name} is not in Santa Clara County")

    def sortName(self):
        """
        Prints the list of cities sorted alphabetically by name.
        """
        for name in sorted(self.cities.keys()):
            print(self.cities[name]['name'])

    def sortPopulation(self):
        """
        Prints the list of cities sorted by population in descending order.
        """
        def get_population(city):
            return city['population']
        
        sorted_population = sorted(self.cities.values(), key=get_population, reverse=True)
        for city in sorted_population:
            print(f"{city['name']} {city['population']:,d}")

    def densityHiLo(self):
        """
        Prints the cities with the highest and lowest population density.
        """
        densities = [(city['population'] / city['area'], city['name']) for city in self.cities.values()]
        high_density = max(densities)
        low_density = min(densities)
        print(f"Lowest: {low_density[1]} at {low_density[0]:.2f} persons/sq mi")
        print(f"Highest: {high_density[1]} at {high_density[0]:.2f} persons/sq mi")
        
def main():
    """
    Main function to execute script logic.
    
    """
    c = Cities('scc.csv')
    for i in range(3):
        name = input("Enter city name: ").title()
        c.lookup(name)
    print()
    c.sortName()
    print()
    c.sortPopulation()
    print()
    c.densityHiLo()
    print()


main()