# Importamos deque de collections, que es como una lista pero más eficiente para agregar y quitar cosas por ambos extremos
from collections import deque

# Clase base Dispositivo, para todo tipo de dispositivo (PC, Tablet, etc.)
class Dispositivo:
    # Inicializamos el dispositivo con sus datos básicos
    def __init__(self, serial, marca, precio):
        self.serial = serial       # Número de serie
        self.marca = marca         # Marca del dispositivo
        self.precio = precio       # Precio
        self.disponible = True     # Por defecto, está disponible para ser prestado
        self.nombre_estudiante = None  # Si está prestado, aquí guardamos el nombre del estudiante

    # Método para prestar el dispositivo
    def prestar(self, nombre_estudiante):
        if self.disponible:  # Si está disponible para préstamo
            self.disponible = False  # Lo marcamos como no disponible
            self.nombre_estudiante = nombre_estudiante  # Guardamos el nombre del que lo toma
            return f"Prestado a {nombre_estudiante}"  # Retornamos el mensaje de préstamo
        return "No disponible"  # Si no está disponible, devolvemos este mensaje

    # Método para devolver el dispositivo
    def devolver(self):
        if not self.disponible:  # Si está prestado
            self.disponible = True  # Lo marcamos como disponible otra vez
            self.nombre_estudiante = None  # Limpiamos el nombre del estudiante
            return "Devuelto"  # Retornamos mensaje de devolución
        return "Ya disponible"  # Si ya estaba disponible, devolvemos este mensaje

    # Método para mostrar la info del dispositivo en un formato bonito
    def __str__(self):
        estado = "Disponible" if self.disponible else f"Prestado a {self.nombre_estudiante}"  # Si está prestado o no
        return f"Serial: {self.serial}, Marca: {self.marca}, Precio: {self.precio}, {estado}"

# Clase que hereda de Dispositivo, para las PCs
class PC(Dispositivo):
    # Inicializamos una PC con sus características extra (ram, disco duro)
    def __init__(self, serial, marca, precio, ram, disco_duro):
        super().__init__(serial, marca, precio)  # Llamamos al constructor de Dispositivo
        self.ram = ram  # Memoria RAM
        self.disco_duro = disco_duro  # Capacidad del disco duro

    # Mostramos la info de la PC incluyendo ram y disco duro
    def __str__(self):
        return super().__str__() + f", RAM: {self.ram}, Disco Duro: {self.disco_duro}"

# Clase que hereda de Dispositivo, para las Tablets
class Tablet(Dispositivo):
    # Inicializamos una Tablet con su tamaño
    def __init__(self, serial, marca, precio, tamano):
        super().__init__(serial, marca, precio)  # Llamamos al constructor de Dispositivo
        self.tamano = tamano  # Tamaño de la tablet

    # Mostramos la info de la tablet con su tamaño
    def __str__(self):
        return super().__str__() + f", Tamaño: {self.tamano}"

# Clase para gestionar el inventario de dispositivos
class Inventario:
    # Inicializamos el inventario, usando deque para guardar los dispositivos
    def __init__(self):
        self.dispositivos = deque()  # Aquí guardamos todos los dispositivos

    # Método para agregar un dispositivo al inventario
    def agregar_dispositivo(self, dispositivo):
        self.dispositivos.append(dispositivo)  # Lo agregamos al final de la cola

    # Método para listar todos los dispositivos del inventario
    def listar_dispositivos(self):
        if not self.dispositivos:  # Si no hay dispositivos, decimos que no hay nada
            return "No hay dispositivos."  
        resultado = ""  # Para guardar la info de todos los dispositivos
        for d in self.dispositivos:  # Recorremos todos los dispositivos
            resultado += str(d) + "\n"  # Agregamos cada uno a la lista de resultados
        return resultado.strip()  # Retornamos todo sin el salto de línea al final

    # Método para buscar un dispositivo por su serial
    def buscar_dispositivo(self, serial):
        for d in self.dispositivos:  # Recorremos todos los dispositivos
            if d.serial == serial:  # Si encontramos el dispositivo por el serial
                return d  # Lo retornamos
        return None  # Si no lo encontramos, devolvemos None

    # Método para prestar un dispositivo a un estudiante
    def prestar_dispositivo(self, serial, nombre_estudiante):
        dispositivo = self.buscar_dispositivo(serial)  # Buscamos el dispositivo
        if dispositivo:  # Si lo encontramos
            return dispositivo.prestar(nombre_estudiante)  # Llamamos al método de prestar
        return "No encontrado"  # Si no lo encontramos, decimos que no se encuentra

    # Método para devolver un dispositivo
    def devolver_dispositivo(self, serial):
        dispositivo = self.buscar_dispositivo(serial)  # Buscamos el dispositivo
        if dispositivo:  # Si lo encontramos
            return dispositivo.devolver()  # Llamamos al método de devolver
        return "No encontrado"  # Si no lo encontramos, decimos que no se encuentra
