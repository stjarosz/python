import os

# System call
os.system("")

# Class of different styles
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

palavra = "TESTE"
jogadas = ["","","","","",""]
tentativa = ""
n=0
acertou = False

while n<6 and not acertou:
    # resetando as variáveis auxiliares para uma nova tentativa
    corretas = [style.BLACK,style.BLACK,style.BLACK,style.BLACK,style.BLACK]
    palavra_aux = [palavra[0],palavra[1],palavra[2],palavra[3],palavra[4]]
    
    print(style.WHITE+"")
    while len(tentativa) != 5:
        tentativa = input().upper()

    # comecamos supondo que a palavra esta correta
    acertou = True
    for i in range(5):
        # comeco procurando letras na posicao CORRETA!
        if tentativa[i] == palavra_aux[i]:
            corretas[i] = style.GREEN
            palavra_aux[i] = "";
        else:
            # achou uma letra que nao corresponde a posicao, entao nao acertou
            acertou = False            
            
    # precisa ser em 2 lacos diferentes porque a ordem IMPORTA
    if not acertou:
        for i in range(5):
            if corretas[i] == style.BLACK:
                for j in range(5):
                    # as posicoes que ja se sabe que possuem letras corretas nao serao
                    # mais acessadas e entao a apagaremos para evitar a repeticao
                    #if corretas[j] != style.GREEN:
                       # achou a letra e temos certeza que nao esta na posicao correta
                       if (tentativa[i] == palavra_aux[j]):
                           # agora queremos garantir que se a quantidade correta de letras
                           # repetidas exceder as da palavra secreta nao serao sinalizadas
                           corretas[i] = style.YELLOW
                           palavra_aux[j] = "";
                           break
                                
    for i in range(5):
        jogadas[n] = jogadas[n]+corretas[i]+tentativa[i]        
    print(jogadas[n])
    tentativa = ""
    n += 1
    
output = style.WHITE
if (acertou):
    output = output + str(n)
else:
    output = output + "X"
output = output + "/6"
print(output)
