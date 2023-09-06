import json
class Aplicante:
    def __init__(self, name, dpi, datebirth, adress):
        self.name = name
        self.dpi = dpi
        self.dathebirth = datebirth
        self.adress = adress
        
    @classmethod
    def from_json(cls, json_str):
        atributos = json.loads(json.str)
        return cls(atributos["name"], atributos["dpi"], atributos["datebirth"], atributos["adress"])