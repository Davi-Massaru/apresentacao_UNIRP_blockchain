from bloco import Bloco
from blockchain import Blockchain

class Minerador:
    def __init__(self, nome, blockchain: Blockchain):
        self.nome = nome
        self.blockchain = blockchain
        self.pontos = 0

    def receber_bloco(self, bloco: Bloco):
        bloco.minerar_bloco()
    
    def validar_bloco(self, bloco: Bloco):
        hashb_bloco = bloco.hash
        retorno_pow = bloco.pow()
        hashb_bloco_recalculo = bloco.hash
        
        return retorno_pow and (hashb_bloco == hashb_bloco_recalculo)