# Por segurança da empresa e dos servidores foi
# removido a API usada neste projeto

import requests
import json
import os

class Recibo:
    def __init__(self, matricula):
        self.matricula = matricula

    def buscar_dados(self):
        url = ""
        request = requests.get(url)
        return request.json()