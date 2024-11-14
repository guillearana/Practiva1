def crear_clave(mensaje, clave):
    # Repite la clave hasta que su longitud sea al menos igual a la longitud del mensaje
    mensaje_clave = clave
    while len(mensaje_clave) < len(mensaje):
        mensaje_clave += clave
    # Corta la clave para que tenga la misma longitud que el mensaje
    mensaje_clave = mensaje_clave[:len(mensaje)]
    return mensaje_clave

def obtener_posicion(letra):
    # Convierte la letra a una posición en el alfabeto (A=0, B=1, ..., Z=25)
    return ord(letra.upper()) - ord('A')

def letra_cifrada(posicion):
    # Convierte una posición en el alfabeto a su letra correspondiente
    return chr(posicion + ord('A'))

def cifrar_vigenere(texto_claro, clave):
    texto_claro = texto_claro.upper()
    clave = clave.upper()
    texto_cifrado = []
    
    # Iterar sobre el texto claro y la clave
    for i, letra in enumerate(texto_claro):
        pos_texto = obtener_posicion(letra)
        pos_clave = obtener_posicion(clave[i])
        
        # Cálculo del cifrado
        pos_cifrada = (pos_texto + pos_clave) % 26
        texto_cifrado.append(letra_cifrada(pos_cifrada))
    
    # Unir el texto cifrado
    return ''.join(texto_cifrado)

def descifrar_vigenere(texto_cifrado, clave):
    texto_cifrado = texto_cifrado.upper()
    clave = clave.upper()
    texto_descifrado = []
    
    # Iterar sobre el texto cifrado y la clave
    for i, letra in enumerate(texto_cifrado):
        pos_cifrado = obtener_posicion(letra)
        pos_clave = obtener_posicion(clave[i])
        
        # Cálculo del descifrado
        pos_descifrada = (pos_cifrado - pos_clave) % 26
        texto_descifrado.append(letra_cifrada(pos_descifrada))
    
    # Unir el texto descifrado
    return ''.join(texto_descifrado)

# Ejecución del programa
if __name__ == '__main__':
    mensaje = input("Escribe un mensaje: ")
    clave = input("Escribe la clave: ")
    
    # Generar clave extendida
    clave_ajustada = crear_clave(mensaje, clave)
    
    # Cifrar el mensaje
    texto_cifrado = cifrar_vigenere(mensaje, clave_ajustada)
    print("Texto cifrado:", texto_cifrado)
    
    # Descifrar el mensaje cifrado
    texto_descifrado = descifrar_vigenere(texto_cifrado, clave_ajustada)
    print("Texto descifrado:", texto_descifrado)
