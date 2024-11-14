import csv
import xml.etree.ElementTree as ET
import xml.sax

class OlympicXMLManager:

    def __init__(self, olympics_csv='olimpiadas.csv', athletes_csv='athlete_events.csv'):
        self.olympics_csv = olympics_csv
        self.athletes_csv = athletes_csv
        self.run()

    def run(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Crear fichero XML de olimpiadas")
            print("2. Crear fichero XML de deportistas")
            print("3. Listado de olimpiadas")
            print("4. Salir")
            option = input("Opción: ")

            if option == "1":
                self.create_olympics_xml()
            elif option == "2":
                self.create_athletes_xml()
            elif option == "3":
                self.list_olympics()
            elif option == "4":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")

    # 1. Crear fichero XML de olimpiadas
    def create_olympics_xml(self):
        olympics_data = []

        try:
            with open(self.olympics_csv, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    olympics_data.append((row['Games'], row['Year'], row['Season'], row['City']))

            # Ordenar las olimpiadas por año y temporada
            olympics_data.sort(key=lambda x: (x[1], x[2] == "Winter", x[2]))

            # Crear el archivo XML
            root = ET.Element("olimpiadas")

            for olympic in olympics_data:
                olympiada = ET.SubElement(root, "olimpiada", year=olympic[1])
                ET.SubElement(olympiada, "juegos").text = olympic[0]
                ET.SubElement(olympiada, "temporada").text = olympic[2]
                ET.SubElement(olympiada, "ciudad").text = olympic[3]

            tree = ET.ElementTree(root)
            tree.write("olimpiadas.xml", encoding="utf-8", xml_declaration=True)

            print("Fichero 'olimpiadas.xml' creado exitosamente.")
        except FileNotFoundError:
            print(f"El archivo {self.olympics_csv} no existe.")
        except Exception as e:
            print(f"Error al crear el archivo XML de olimpiadas: {e}")

    # 2. Crear fichero XML de deportistas
    def create_athletes_xml(self):
        try:
            with open(self.athletes_csv, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)

                root = ET.Element("deportistas")

                for row in reader:
                    deportista = ET.SubElement(root, "deportista", id=row['ID'])
                    ET.SubElement(deportista, "nombre").text = row['Name']
                    ET.SubElement(deportista, "sexo").text = row['Sex']
                    ET.SubElement(deportista, "altura").text = row['Height']
                    ET.SubElement(deportista, "peso").text = row['Weight']

                    participaciones = ET.SubElement(deportista, "participaciones")

                    deporte = ET.SubElement(participaciones, "deporte", nombre=row['Sport'])
                    participacion = ET.SubElement(deporte, "participación", edad=row['Age'])
                    ET.SubElement(participacion, "equipo", abbr=row['NOC']).text = row['Team']
                    ET.SubElement(participacion, "juegos").text = f"{row['Games']} - {row['City']}"
                    ET.SubElement(participacion, "evento").text = row['Event']
                    ET.SubElement(participacion, "medalla").text = row['Medal']

                tree = ET.ElementTree(root)
                tree.write("deportistas.xml", encoding="utf-8", xml_declaration=True)

            print("Fichero 'deportistas.xml' creado exitosamente.")
        except FileNotFoundError:
            print(f"El archivo {self.athletes_csv} no existe.")
        except Exception as e:
            print(f"Error al crear el archivo XML de deportistas: {e}")

    # 3. Listado de olimpiadas usando SAX
    def list_olympics(self):
        try:
            handler = OlympicHandler()
            xml.sax.parse("olimpiadas.xml", handler)
        except FileNotFoundError:
            print("El archivo 'olimpiadas.xml' no existe.")
        except Exception as e:
            print(f"Error al listar las olimpiadas: {e}")

# SAX handler para parsear el archivo olimpiadas.xml
class OlympicHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_data = ""
        self.games = ""
        self.year = ""

    def startElement(self, name, attrs):
        self.current_data = name
        if name == "olimpiada":
            self.year = attrs['year']

    def endElement(self, name):
        if name == "olimpiada":
            print(f"Juegos: {self.games} | Año: {self.year}")
        self.current_data = ""

    def characters(self, content):
        if self.current_data == "juegos":
            self.games = content.strip()

# Ejecutar el programa
if __name__ == "__main__":
    OlympicXMLManager()
