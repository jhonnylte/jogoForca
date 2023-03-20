import random

lista = ['abelha', 'Alemanha', 'árvore', 'alegre', 'atadura', 'bexiga', 'bateria', 'boliche', 'beterraba','comércio', 'caixa','chapéu', 'colírio', 'colete', 'cimento','dente', 'dormitório', 'domesticar', 'diarista','fogueira', 'felicidade', 'formidável', 'frutífero', 'formigueiro']

def palavraAleatoria():
    valor = random.randint(0, len(lista)-1) # Pega um valor aletório de 0 até a última posição da lista de palavras
    return lista[valor]# Volta a palavra que está na posição do número aleatório
#palavraAleatoria()