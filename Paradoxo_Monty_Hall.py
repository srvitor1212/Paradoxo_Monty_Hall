

import random


VITORIAS = 0
DERROTAS = 0


def GerarPortas():
    class Porta():
        def __init__(self,  nome="porta", 
                            premiada=False, 
                            valida=True,
                            escolhida=False ):
            self.nome = nome
            self.premiada = premiada
            self.valida = valida
            self.escolhida = escolhida

    portaSorteada = random.randint(0,2)
    portas = []

    for i in range(3):  # 3 portas, índice de 0 a 2
        if i != portaSorteada:
            porta = Porta(nome=f"Porta nr {i+1}", premiada=False)
        else:
            porta = Porta(nome=f"Porta nr {i+1}", premiada=True)
        portas.append(porta)

    return portas


def MostrarPortas(portas):
    ind = 0
    print(f'\n==== Portas da rodada ====')
    for p in portas:
        print(f"idx[{ind}] - {p.nome}, premiada={p.premiada}, escolhida={p.escolhida}")
        ind+=1


def UmaRodada(opcao=1):
    global VITORIAS
    global DERROTAS

    portas = list(GerarPortas())
    escolha = (random.randint(0,2))
    portas[escolha].escolhida = True
    
    #MostrarPortas(portas)

    if opcao == 1:
        if portas[escolha].premiada == True:
            VITORIAS += 1
        else:
            DERROTAS += 1
    else:
        #Remove a porta que não é a escolhida nem a premiada
        for p in portas:
            if p.premiada == False and p.escolhida == False:
                p.valida = False
                break

        #Escolha outra porta que não seja a mesma, nem a que foi removida
        idxPorta = 0
        for p in portas:
            if p.valida:
                if p.escolhida:
                    p.escolhida = False
                else:
                    p.escolhida = True
                    escolha = idxPorta
            idxPorta += 1

        #Verifica vitória
        if portas[escolha].premiada == True:
            VITORIAS += 1
        else:
            DERROTAS += 1


def MostraPlacar():
    taxaVitoria = (VITORIAS / (VITORIAS+DERROTAS)) * 100
    print(f"Venceu {VITORIAS} de {VITORIAS+DERROTAS} jogadas! \n{taxaVitoria} % de vitória")


# -------------------------------------
print("Paradoxo de Monty Hall")
print(  f"O problema foi apresentado no programa de televisão Let’s Make a Deal nos Estados Unidos."
        f"O paradoxo de Monty Hall considera que existem três portas, atrás de uma existe um prêmio e, atrás"
        f" das outras duas não existe nada. Na primeira etapa uma pessoa escolhe uma porta (esta ainda não é aberta),"
        f" após isso uma outra porta (que não foi a escolhida) é aberta e é revelado que não contém nada. Neste momento,"
        f" se tem 2 duas portas fechadas (uma porta contem o prêmio e a outra porta não contem nada). Então, após esta "
        f"etapa temos duas portas fechadas e a pessoa tem a possibilidade de manter a sua escolha inicial ou pode optar "
        f"em trocar de porta. Então, a pergunta é:"
        f"A melhor opção seria ficar com a porta inicialmente escolhida ou trocar para a porta que sobrou?")

print("====================================================================")
print("O jogador escolhe uma porta e mantém essa escolha até o fim do jogo")
qtdRodadas = range(1000000)
for i in qtdRodadas:
    UmaRodada(1)
MostraPlacar()

print("\n")
print("====================================================================")
print("O jogador escolhe uma porta, o programa retira uma porta sem prêmio e o jogar então troca de porta")
VITORIAS = 0
DERROTAS = 0
for i in qtdRodadas:
    UmaRodada(2)
MostraPlacar()
