class GPS:
    def __init__(self, ubicacion):
        self.ubicacion = ubicacion

    def mostrar_ubicacion(self):
        return f"Ubicación: {self.ubicacion}"