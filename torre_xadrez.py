# só para ser mais prático por que vai ser printada a matriz várias vezes
#  para ser visualizado o progresso
lista_de_inimigos = []


def print_da_matriz():
    for linha_idx in range(8):
        for coluna_idx in range(8):
            if matriz[linha_idx][coluna_idx] in lista_de_inimigos:
                print(f"* ", end=" ")
            else:
                print(f"{matriz[linha_idx][coluna_idx]}", end=" ")

        print()


lista_de_numeros = ["1", "2", "3", "4", "5", "6", "7", "8"]
lista_de_letras = ["a", "b", "c", "d", "e", "f", "g", "h"]

# - * - inimigo
# - + - torre ~

matriz = []
for linha_idx in range(8):
    linha = []
    for coluna_idx in range(8):
        print(
            f"{lista_de_letras[linha_idx]}{lista_de_numeros[coluna_idx]}", end=' ')
        value_linha = lista_de_letras[linha_idx]
        value_coluna = lista_de_numeros[coluna_idx]
        coordenada = f"{value_linha}{value_coluna}"
        linha.append(coordenada)
    matriz.append(linha)
    print("|")

torre = input("escolha a coordenada da torre : ").strip()
# validando se a coordenada da torre existe nas coordenadas do nosso tabuleiro
torre = list(torre)
if len(torre) == 2:
    if torre[0] in lista_de_letras and torre[1] in lista_de_numeros:
        print("coordenada valida")
        torre = "".join(torre)
        coordenada_Torre_in = True
    else:
        print("coordenada invalida")
        exit()
else:
    print("coordenada invalida")
    exit()


# trocando a coordenada correspodente à da torre que o usuario escolheu pelo simbolo '+'
for linha_idx in range(8):
    for coluna_idx in range(8):
        if matriz[linha_idx][coluna_idx] == torre and coordenada_Torre_in:
            matriz[linha_idx][coluna_idx] = "+ "

# pritando de novo as coordenadas do tabuleiro , só que agora vai ser mostrado o simbolo
# + no lugar da coordenada da torre
print_da_matriz()


n_inimigos = int(input("quantos inimigos você quer posicionar ? :"))
# tabuleiro 8x8 são 64 peças , mas apenas 63 disponiveis para alocar inimigos
# por que um desses espaços já está ocupado pela torre
if n_inimigos > 63:
    print("número de inimigos maior que espaços disponiveis(63 espaços disponiveis)")
    exit()
for numero in range(n_inimigos):
    posicao = input(f"qual a posicao do {numero+1} inimigo ? :")
    # validando a posicao do inimigo :
    posicao = list(posicao)
    if len(posicao) == 2:
        if posicao[0] in lista_de_letras and posicao[1] in lista_de_numeros:
            # caso o usuário sem querer coloque o lugar que um inimigo ocupa em cima do lugar da torre
            posicao = "".join(posicao)
            if posicao == torre:
                print(
                    f"dois corpos não ocupam o mesmo espaços , o inimigo não pode ficar no lugar da sua torre")
            else:
                if posicao not in lista_de_inimigos:
                    # essa condicional vai servir para evitar que se coloque o mesmo inimigo duas vezes
                    posicao = "".join(posicao)
                    lista_de_inimigos.append(posicao)
                else:
                    print("oops,você já digitou esse inimigo")
        else:
            # posicao não está nas coordenadas disponíveis
            print("coordenada não pertence à nenhuma das especificadas")

    else:
        # caso não for valida irá apenas ser avisado no console :
        print(f"posicao {"".join(posicao)} não existe no tabuleiro")

# mostrando ao usuário aonde estão os seus inimigos :
print_da_matriz()


torre = list(torre)


def contabilizando_pecas_comiveis(lista_de_inimigos):
    inimigos_esq = []
    inimigos_dir = []
    inimigos_cima = []
    inimigos_baixo = []
    for linha_idx in range(8):
        # contadora guardando o número de inimigos na linha atual e na coluna_atual
        for coluna_idx in range(8):
            coordenada = matriz[linha_idx][coluna_idx]
            # não tem como a coordenada do inimigo ser igual à coordenada da torre por que já tratamos este erro lá emcima
            if coordenada in lista_de_inimigos:
                coordenada_parts = list(coordenada)
                if coordenada_parts[0] == torre[0]:
                    # mesma letra / mesma linha que a torre
                    if coordenada_parts[1] < torre[1]:
                        # então está a esquerda da torre , por que o seu número é menor que o número da torre
                        if coordenada not in inimigos_esq:
                            # assim só vai deixar ter um inimigo comivel à esquerda , não pulando peças
                            inimigos_esq.append(coordenada)
                    if coordenada_parts[1] > torre[1]:
                        # então está a direita da torre , por que o seu número é maior que o número da torre
                        if coordenada not in inimigos_dir:
                            # assim só vai deixar ter um inimigo comivel à direita , não pulando peças
                            inimigos_dir.append(coordenada)
                if coordenada_parts[1] == torre[1]:
                    # mesmo número / mesma coluna que a torre
                    if coordenada_parts[0] < torre[0]:
                        # se a letra for menor que a letra da torre então está acima da torre
                        if coordenada not in inimigos_cima:
                            # assim só pode ter um inimigo comivel acima da torre
                            inimigos_cima.append(coordenada)
                    if coordenada_parts[0] > torre[0]:
                        # então está abaixo da torre , por que a sua letra é maior que a letra da torre
                        if coordenada not in inimigos_baixo:
                            # assim só pode ter um inimigo comivel abaixo da torre
                            inimigos_baixo.append(coordenada)

    inimigos_na_linha = len(inimigos_esq)+len(inimigos_dir)
    inimigos_na_coluna = len(inimigos_cima) + len(inimigos_baixo)
    return inimigos_na_linha, inimigos_na_coluna


inimigos_na_linha, inimigos_na_coluna = contabilizando_pecas_comiveis(
    lista_de_inimigos)
inimigos_no_tabuleiro_list = [inimigos_na_linha, inimigos_na_coluna]
inimigos_no_tabuleiro_num = sum(inimigos_no_tabuleiro_list)
print(
    f"a torre posicionada na coordenada {torre} pode comer {inimigos_no_tabuleiro_num} peças")
