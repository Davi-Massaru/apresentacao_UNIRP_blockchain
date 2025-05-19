import hashlib
import time

class Bloco:
    def __init__(self, indice, dados, hash_anterior):
        self.indice = indice
        self.timestamp = time.time()
        self.dados = dados
        self.hash_anterior = hash_anterior
        self.nonce = 0
        self.hash = self.calcular_hash()

    def calcular_hash(self):
        conteudo = (
            str(self.indice) +
            str(self.timestamp) +
            str(self.dados) +
            str(self.hash_anterior) +
            str(self.nonce)
        )
        return hashlib.sha256(conteudo.encode()).hexdigest()
    
    def pow(self):
        self.hash = self.calcular_hash()
        inicia_com_000 = (self.hash.startswith("000"))
        multiplo_de_2 = (self.nonce % 2 == 0)
        
        return inicia_com_000 and multiplo_de_2
    
    def minerar_bloco(self):
        print(f"Minerando bloco {self.indice}...")
        while True:
            self.hash = self.calcular_hash()
            if self.pow():
                print(f"Bloco {self.indice} minerado com nonce {self.nonce}: {self.hash}")
                break
            self.nonce += 1
