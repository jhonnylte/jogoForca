from banco import palavraAleatoria
from IPython.display import clear_output

niveisForca = ['________\n|      |\n|\n|\n|\n|', 
               '________\n|      |\n|      O\n|\n|\n|', 
               '________\n|      |\n|      O\n|      |\n|\n|',
               '________\n|      |\n|      O\n|     /|\n|\n|',
               '________\n|      |\n|      O\n|     /|\ \n|\n|',
               '________\n|      |\n|      O\n|     /|\ \n|     /  \n|',
               '________\n|      |\n|      O\n|     /|\ \n|     / \ \n|'
              ]


class Forca:
    def __init__(self, resposta):
        self.resposta = resposta
        self.chances = 6
        self.palavra = ['_']*len(resposta)
        self.letrasUsadas = []
        self.totalMatchs = 0 # Total de letras descobertas
    def mostrar(self):
        if self.chances >= 0:
            print(niveisForca[6-self.chances])
            resultado = ''
            print(resultado.join(self.palavra)) # string.join(itr) pega todos os elementos do itr e insere na str.    
    def jogar(self):
        if self.totalMatchs < len(self.resposta): # Se o total de letras acertadas for menor que o tamanho da resposta
            if self.chances > 0: ####
                self.mostrar()
                print('Escolha uma letra: ')
                tentativa = input()
                if (len(tentativa)>1) or (len(tentativa)<1):
                    clear_output()
                    print('Quantidade de caracteres inválida! Digite apenas um:')
                    return self.jogar()
                elif self.letrasUsadas.count(tentativa.lower()) == 0: # Caso a letra não tenham sido tentada ainda
                        self.letrasUsadas.append(tentativa.lower()) # Registra que ela foi usada
                        matchs = 0 # Comparação entre letra tentada e letras da resposta, cada vez que for =, dá 1 match
                        for i in range(len(self.resposta)):
                            if self.resposta[i].lower() == tentativa.lower():
                                self.palavra[i] = tentativa.lower() 
                                matchs += 1
                                self.totalMatchs += 1
                        if matchs == 0:
                            clear_output()
                            print('A resposta não contém: '+tentativa.lower())
                            self.chances -= 1
                            if self.chances < 0:
                                print('Game over!')
                            else:
                                print('Chances: '+str(self.chances))
                                return self.jogar()
                        clear_output()
                        return self.jogar()
                else:
                    clear_output()
                    print('A letra já foi usada anteriormente!')
                    return self.jogar()
            print(niveisForca[6])
            resultado = ''
            print(resultado.join(self.palavra))
            print('Game over!')
            print('A resposta era: '+self.resposta)
        else:
            clear_output()
            self.mostrar()
            print('Você acertou!')


Forca(palavraAleatoria()).jogar()
