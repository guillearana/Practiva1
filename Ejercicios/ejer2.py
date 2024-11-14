import csv

class OlympicDataManager:

    def __init__(self, athletes_file='athlete_events.csv', olympics_file='olimpiadas.csv'):
        self.athletes_file = athletes_file
        self.olympics_file = olympics_file
        self.run()

    def run(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Generar fichero csv de olimpiadas")
            print("2. Buscar deportista")
            print("3. Buscar deportistas por deporte y olimpiada")
            print("4. Añadir deportista")
            print("5. Salir")
            option = input("Opción: ")

            if option == "1":
                self.generate_olympics_csv()
            elif option == "2":
                self.search_athlete()
            elif option == "3":
                self.search_athletes_by_sport_and_olympics()
            elif option == "4":
                self.add_athlete()
            elif option == "5":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")

    # 1. Generar fichero CSV de olimpiadas
    def generate_olympics_csv(self):
        olympics_data = set()

        try:
            with open(self.athletes_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    olympics_data.add((row['Games'], row['Year'], row['Season'], row['City']))

            with open(self.olympics_file, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Games', 'Year', 'Season', 'City'])  # Escribimos el encabezado
                for olympic in olympics_data:
                    writer.writerow(olympic)

            print("Fichero 'olimpiadas.csv' generado exitosamente.")
        except FileNotFoundError:
            print(f"El archivo {self.athletes_file} no existe.")
        except Exception as e:
            print(f"Error al generar el archivo de olimpiadas: {e}")

    # 2. Buscar deportista por nombre
    def search_athlete(self):
        name_search = input("Ingrese el nombre del deportista a buscar: ").lower()

        found = False
        try:
            with open(self.athletes_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if name_search in row['Name'].lower():
                        if not found:
                            print(f"\nDatos de {row['Name']}:")
                        print(f"  - Nombre: {row['Name']}")
                        print(f"  - Sexo: {row['Sex']}")
                        print(f"  - Altura: {row['Height']} cm")
                        print(f"  - Peso: {row['Weight']} kg")
                        print(f"  - Año: {row['Year']}")
                        print(f"  - Deporte: {row['Sport']}")
                        print(f"  - Evento: {row['Event']}")
                        print(f"  - Medalla: {row['Medal']}")
                        found = True

            if not found:
                print("No se encontró ningún deportista con ese nombre.")
        except FileNotFoundError:
            print(f"El archivo {self.athletes_file} no existe.")
        except Exception as e:
            print(f"Error al buscar al deportista: {e}")

    # 3. Buscar deportistas por deporte y olimpiada
    def search_athletes_by_sport_and_olympics(self):
        sport = input("Ingrese el deporte: ").title()
        year = input("Ingrese el año de la olimpiada: ")
        season = input("Ingrese la temporada (Summer/Winter): ").capitalize()

        found = False
        try:
            with open(self.athletes_file, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row['Sport'] == sport and row['Year'] == year and row['Season'] == season:
                        if not found:
                            print(f"\nDetalles de la olimpiada {row['Games']} en {row['City']}:")
                            print(f"Deporte: {sport}")
                            found = True
                        print(f"  - Nombre: {row['Name']}")
                        print(f"  - Evento: {row['Event']}")
                        print(f"  - Medalla: {row['Medal']}")

            if not found:
                print("No se encontró ningún deportista para esa olimpiada y deporte.")
        except FileNotFoundError:
            print(f"El archivo {self.athletes_file} no existe.")
        except Exception as e:
            print(f"Error al buscar deportistas: {e}")

    # 4. Añadir deportista
    def add_athlete(self):
        name = input("Ingrese el nombre del deportista: ")
        sex = input("Ingrese el sexo (M/F): ")
        height = input("Ingrese la altura (en cm): ")
        weight = input("Ingrese el peso (en kg): ")
        year = input("Ingrese el año de la olimpiada: ")
        sport = input("Ingrese el deporte: ")
        event = input("Ingrese el evento: ")
        medal = input("Ingrese la medalla (Gold, Silver, Bronze o None): ")

        try:
            with open(self.athletes_file, mode='a', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow([name, sex, height, weight, year, sport, event, medal])
            print("Deportista añadido exitosamente.")
        except Exception as e:
            print(f"Error al añadir el deportista: {e}")

# Ejecutar el programa
if __name__ == "__main__":
    OlympicDataManager()
