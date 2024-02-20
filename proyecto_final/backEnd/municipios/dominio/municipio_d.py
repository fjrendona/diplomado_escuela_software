import json


class municipio:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __repr__(self):
        return f"municipio(id: {self.id}, nombre: {self.nombre})"

    def to_json(self):
        return json.dumps(self, default=lambda self: self.__dict__)