import os
import shutil

class FileSystemManager:

    def __init__(self):
        self.run()

    def run(self):
        while True:
            print("\nSeleccione una opción:")
            print("1. Crear un directorio")
            print("2. Listar un directorio")
            print("3. Copiar un archivo")
            print("4. Mover un archivo")
            print("5. Eliminar un archivo/directorio")
            print("6. Salir")
            option = input("Opción: ")

            if option == "1":
                self.create_directory()
            elif option == "2":
                self.list_directory()
            elif option == "3":
                self.copy_file()
            elif option == "4":
                self.move_file()
            elif option == "5":
                self.delete_file_or_directory()
            elif option == "6":
                print("Saliendo del programa...")
                break
            else:
                print("Opción no válida.")

    # Método para crear un directorio
    def create_directory(self):
        parent_dir = input("Ingrese la ruta del directorio: ")
        new_dir = input("Ingrese el nombre del nuevo directorio: ")
        path = os.path.join(parent_dir, new_dir)

        try:
            os.makedirs(path)
            print("Directorio creado exitosamente.")
        except FileExistsError:
            print("El directorio ya existe.")
        except Exception as e:
            print(f"No se pudo crear el directorio: {e}")

    # Método para listar el contenido de un directorio
    def list_directory(self):
        dir_path = input("Ingrese la ruta del directorio a listar: ")
        if os.path.isdir(dir_path):
            print(f"Contenido de {dir_path}:")
            for entry in os.listdir(dir_path):
                entry_path = os.path.join(dir_path, entry)
                if os.path.isdir(entry_path):
                    print(f"[DIRECTORIO] {entry}")
                else:
                    print(f"[ARCHIVO] {entry}")
        else:
            print("El directorio no existe o la ruta no es válida.")

    # Método para copiar un archivo
    def copy_file(self):
        original_path = input("Ingrese la ruta del archivo original: ")
        destination_path = input("Ingrese la ruta de destino: ")

        if os.path.isfile(original_path):
            try:
                shutil.copy(original_path, destination_path)
                print("Archivo copiado exitosamente.")
            except Exception as e:
                print(f"Error al copiar el archivo: {e}")
        else:
            print("El archivo original no existe.")

    # Método para mover un archivo
    def move_file(self):
        original_path = input("Ingrese la ruta del archivo a mover: ")
        destination_path = input("Ingrese la ruta de destino: ")

        if os.path.isfile(original_path):
            try:
                shutil.move(original_path, destination_path)
                print("Archivo movido exitosamente.")
            except Exception as e:
                print(f"Error al mover el archivo: {e}")
        else:
            print("El archivo no existe.")

    # Método para eliminar un archivo o directorio
    def delete_file_or_directory(self):
        path = input("Ingrese la ruta del archivo o directorio a eliminar: ")

        if os.path.exists(path):
            try:
                if os.path.isdir(path):
                    # Verificar si el directorio está vacío
                    if not os.listdir(path):
                        os.rmdir(path)
                        print("Directorio eliminado exitosamente.")
                    else:
                        print("El directorio no está vacío. No se puede eliminar.")
                else:
                    os.remove(path)
                    print("Archivo eliminado exitosamente.")
            except Exception as e:
                print(f"No se pudo eliminar: {e}")
        else:
            print("El archivo o directorio no existe.")

# Ejecutar el programa
if __name__ == "__main__":
    FileSystemManager()
