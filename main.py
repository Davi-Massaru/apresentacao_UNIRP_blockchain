import threading
from typing import List
from blockchain import Blockchain
from bloco import Bloco
from minerador import Minerador
import time
import random

# Inicia a blockchain
blockchain = Blockchain()
blockchain.lock = threading.Lock()  # Lock para sincronizar acesso à blockchain

# Cria os mineradores e associa a blockchain a eles
mineradores = [
    Minerador("Massaru", blockchain),
    Minerador("Valéria", blockchain),
    Minerador("Lucimar", blockchain)
]

def competir_por_bloco(dados):
    with blockchain.lock:
        indice = len(blockchain.cadeia)
        hash_anterior = blockchain.cadeia[-1].hash

    bloco_base = Bloco(indice, dados, hash_anterior)

    vencedor = None
    vencedor_lock = threading.Lock()
    threads = []

    def tentar_minera(minerador: Minerador, mineradores: List[Minerador]):
        nonlocal vencedor
        time.sleep(random.uniform(0, 0.1))
        bloco_copia = Bloco(bloco_base.indice, bloco_base.dados, bloco_base.hash_anterior)
        bloco_copia.nonce = 0
        
        minerador.receber_bloco(bloco_copia)
        
        aprovacao = 0
        quantidade_mineradores = len(mineradores)
        for m in mineradores:
            if m.validar_bloco(bloco_copia):
                    aprovacao += 1
                    
        if aprovacao >= (quantidade_mineradores /2):     
            blockchain.adicionar_bloco(bloco_copia)
        
        with vencedor_lock:
            if vencedor is None and blockchain.cadeia[-1].indice == bloco_copia.indice:
                vencedor = minerador
                vencedor.pontos += 1
                print(f"Venceu: {minerador.nome} HASH: {bloco_copia.hash} NONCE: {bloco_copia.nonce} " )
                print(f"✅ {vencedor.nome} minerou e adicionou o bloco {bloco_copia.indice}! Pontos: {vencedor.pontos}")

    for m in mineradores:
        t = threading.Thread(target=tentar_minera, args=(m,mineradores))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()     

if __name__ == "__main__":
    print("🚀 Blockchain iniciada. Digite informações para minerar novos blocos.")
    try:
        while True:
            dados = input("\nDigite os dados do novo bloco (ou 'sair' para encerrar): ")
            if dados.lower() == 'sair':
                break

            competir_por_bloco(dados)

            print("\n📊 Pontuação dos mineradores:")
            for minerador in mineradores:
                print(f" - {minerador.nome}: {minerador.pontos} ponto(s)")

            print("\n🔗 Blockchain atual:")
            blockchain.print_cadeia()

            print(f"🔗 Tamanho atual da blockchain: {len(blockchain.cadeia)} blocos")
            print("Blockchain válida?", blockchain.validar_cadeia())

    except KeyboardInterrupt:
        print("\n⛔ Encerrado pelo usuário.")
