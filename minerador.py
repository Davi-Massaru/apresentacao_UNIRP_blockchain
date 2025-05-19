from bloco import Bloco
from blockchain import Blockchain

class Minerador:
    def __init__(self, nome, blockchain: Blockchain):
        self.nome = nome
        self.blockchain = blockchain
        self.pontos = 0

    def receber_bloco(self, bloco: Bloco):
        bloco.minerar_bloco()

        if bloco.pow():
            if  self.blockchain.adicionar_bloco(bloco) == 1:
                self.pontos += 1
                print(f"✅ {self.nome} minerou e adicionou o bloco {bloco.indice}! Pontos: {self.pontos}")

