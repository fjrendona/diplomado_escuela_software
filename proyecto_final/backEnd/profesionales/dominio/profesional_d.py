import json


class profesional:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre

    def __repr__(self):
        return f"profesional(id: {self.id}, nombre: {self.nombre})"

    def to_json(self):
        return json.dumps(self, default=lambda self: self.__dict__)
