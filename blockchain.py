from bloco import Bloco

class Blockchain:
    def __init__(self):
        self.cadeia = [self.criar_bloco_genesis()]
        
    def print_cadeia(self):
        for bloco in self.cadeia:
            print(f"Índice: {bloco.indice}")
            print(f"Timestamp: {bloco.timestamp}")
            print(f"Dados: {bloco.dados}")
            print(f"Hash Anterior: {bloco.hash_anterior}")
            print(f"Nonce: {bloco.nonce}")
            print(f"Hash: {bloco.hash}")
            print("--------")

    def criar_bloco_genesis(self):
        bloco = Bloco(0, "Bloco Gênesis", "000")
        bloco.minerar_bloco()
        return bloco
    
    def adicionar_bloco(self, bloco: Bloco): 
        ultimo_bloco = self.cadeia[-1]
        bloco.hash_anterior = ultimo_bloco.hash
        
        if bloco.indice != ultimo_bloco.indice + 1:
            return 0
            
        if not bloco.pow():
            return 0
        
        self.cadeia.append(bloco)
        return 1
            
    def validar_cadeia(self):
        for i in range(1, len(self.cadeia)):
            bloco_atual = self.cadeia[i]
            bloco_anterior = self.cadeia[i - 1]

            # Verifica se o hash do bloco é válido
            if bloco_atual.hash != bloco_atual.calcular_hash():
                return False

            # Verifica se o hash anterior bate com o hash do bloco anterior
            if bloco_atual.hash_anterior != bloco_anterior.hash:
                return False

            # Verifica proof-of-work
            if not bloco_atual.pow():
                return False
            
        return True
