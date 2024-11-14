import pickle
import os

class OlympicEdition:
    def __init__(self, games, year, season, city):
        self.games = games
        self.year = year
        self.season = season
        self.city = city

    def __str__(self):
        return f"{self.games} ({self.year}, {self.season}) - {self.city}"

class OlympicBinaryManager:

    def __init__(self, binary_file="olympics.bin", xml_file="olimpiadas.xml"):
        self.binary_file = binary_file
        self.xml_file = xml_file
        self.olympics = self.load_olympics_from_binary() if os.path.exists(self.binary_file) else []

        self.run()

    def run(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Crear fichero serializable de olimpiadas")
            print("2. Añadir edición olímpica")
            print("3. Buscar olimpiadas por sede")
            print("4. Eliminar edición olímpica")
            print("5. Salir")
            option = input("Opción: ")

            if option == "1":
                self.create_serializable_olympics()
            elif option == "2":
                self.add_olympic_edition()
            elif option == "3":
                self.search_olympics_by_city()
            elif option == "4":
                self.remove_olympic_edition()
            elif option == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")

    # 1. Crear fichero serializable de olimpiadas
    def create_serializable_olympics(self):
        try:
            olympics_data = self.load_olympics_from_xml()
            self.olympics = [OlympicEdition(games, year, season, city) for games, year, season, city in olympics_data]
            self.save_to_binary()

            print("Fichero serializable de olimpiadas creado exitosamente.")
        except Exception as e:
            print(f"Error al crear el archivo serializable de olimpiadas: {e}")

    # 2. Añadir edición olímpica
    def add_olympic_edition(self):
        print("\nIntroduzca la nueva edición olímpica:")
        games = input("Juegos: ")
        year = input("Año: ")
        season = input("Temporada (Summer/Winter): ")
        city = input("Ciudad: ")

        olympic_edition = OlympicEdition(games, year, season, city)
        self.olympics.append(olympic_edition)
        self.save_to_binary()

        print(f"Edición olímpica {olympic_edition} añadida con éxito.")

    # 3. Buscar olimpiadas por sede
    def search_olympics_by_city(self):
        city_search = input("Introduce la ciudad a buscar: ").lower()

        found_olympics = [olympic for olympic in self.olympics if city_search in olympic.city.lower()]

        if found_olympics:
            print("\nOlimpiadas encontradas:")
            for olympic in found_olympics:
                print(olympic)
        else:
            print("No se encontraron olimpiadas en esa sede.")

    # 4. Eliminar edición olímpica
    def remove_olympic_edition(self):
        year = input("Introduce el año de la edición olímpica a eliminar: ")
        season = input("Introduce la temporada (Summer/Winter): ")

        olympic_to_remove = None
        for olympic in self.olympics:
            if olympic.year == year and olympic.season.lower() == season.lower():
                olympic_to_remove = olympic
                break

        if olympic_to_remove:
            self.olympics.remove(olympic_to_remove)
            self.save_to_binary()
            print(f"Edición olímpica {olympic_to_remove} eliminada con éxito.")
        else:
            print("No se encontró una edición olímpica con ese año y temporada.")

    # Guardar la lista de olimpiadas en un archivo binario
    def save_to_binary(self):
        try:
            with open(self.binary_file, 'wb') as file:
                pickle.dump(self.olympics, file)
        except Exception as e:
            print(f"Error al guardar el archivo binario: {e}")

    # Cargar las olimpiadas desde el archivo binario
    def load_olympics_from_binary(self):
        try:
            with open(self.binary_file, 'rb') as file:
                return pickle.load(file)
        except Exception as e:
            print(f"Error al cargar el archivo binario: {e}")
            return []

    # Cargar las olimpiadas desde el archivo XML
    def load_olympics_from_xml(self):
        olympics_data = []
        try:
            import xml.etree.ElementTree as ET

            tree = ET.parse(self.xml_file)
            root = tree.getroot()

            for olympiad in root.findall('olimpiada'):
                games = olympiad.find('juegos').text
                year = olympiad.get('year')
                season = olympiad.find('temporada').text
                city = olympiad.find('ciudad').text
                olympics_data.append((games, year, season, city))

            return olympics_data
        except Exception as e:
            print(f"Error al cargar el archivo XML de olimpiadas: {e}")
            return []

# Ejecutar el programa
if __name__ == "__main__":
    OlympicBinaryManager()
