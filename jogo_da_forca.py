import random

class jogo_da_forca():

    def __init__(self, jogos_ganhos = 0, jogos_perdidos = 0, letras_certas = [], letras_erradas = []):
        print('Bem vindo ao jogo \n')
        self.jogos_ganhos = jogos_ganhos
        self.jogos_perdidos = jogos_perdidos
        self.jogos_total = self.jogos_ganhos + self.jogos_perdidos
        self.letras_certas = letras_certas
        self.letras_erradas = letras_erradas

    def novo_jogo(self, palavras):
        '''Recebe um iterável "palavras" com as possíveis palavras a serem sorteadas para o jogo e dá procedimento ao mesmo.'''
        
        palavra = random.choice(palavras).upper()

        while True:
            self.desenha_forca()
            print('\n')
            self.descreve_letras(palavra)
            print('\n')
            self.lista_certas()
            print('\n')
            self.lista_erradas()
            print('\n')

            while True:
                palpite = input('Insira um palpite: ')
                if palpite.upper() in self.letras_certas or palpite.upper() in self.letras_erradas:
                    print('Letra já utilizada!')
                    continue
                if palpite.isalpha() and len(palpite) == 1:
                    break
                print('Erro! Insira UMA letra (apenas caracteres SEM acento).')
            
            if palpite.upper() in palavra:
                self.letras_certas.append(palpite.upper())
                print('A letra ' + palpite.upper() + ' faz parte da palavra!')
            else:
                self.letras_erradas.append(palpite.upper())
                print('Infelizmente, a letra ' + palpite.upper() + ' NÃO faz parte da palavra!')
            if len(self.letras_erradas) == 6 or len(set(self.letras_certas)) == len(set(palavra)):
                self.desenha_forca()
                print('\n')
                self.descreve_letras(palavra)
                print('\n')
                self.lista_certas()
                print('\n')
                self.lista_erradas()
                print('\n')
                print('FIM DE JOGO! QUE PENA, VOCÊ PERDEU!') if len(self.letras_erradas) == 6 else print('FIM DE JOGO! PARABÉNS, VOCÊ GANHOU!')
                print('A palavra era: ' + palavra.upper())
                break
                
        return

    def desenha_forca(self):
        total_erradas = len(self.letras_erradas)
        forcas  =    {  0   :   '--+----+\n' 
                                '  |    |\n' 
                                '       |\n' 
                                '       |\n' 
                                '       |\n' 
                                '       |\n' 
                                '  _____|__',
                        1   :  '--+----+\n'
                               '  |    |\n' 
                               '  0    |\n' 
                               '       |\n' 
                               '       |\n' 
                               '       |\n' 
                               '  _____|__',
                        2   :  '--+----+\n'
                               '  |    |\n' 
                               '  0    |\n' 
                               '  |    |\n' 
                               '       |\n' 
                               '       |\n' 
                               '  _____|__',
                        3   :  '--+----+\n'
                               '  |    |\n' 
                               '  0    |\n' 
                              ' /|    |\n' 
                               '       |\n' 
                               '       |\n' 
                               '  _____|__',
                        4   :  '--+----+\n'
                               '  |    |\n' 
                               '  0    |\n' 
                              ' /|\   |\n' 
                               '       |\n' 
                               '       |\n' 
                               '  _____|__',
                        5   :  '--+----+\n'
                               '  |    |\n' 
                               '  0    |\n' 
                              ' /|\   |\n' 
                              ' /     |\n' 
                               '       |\n' 
                               '  _____|__',
                        6   :  '--+----+\n'
                               '  |    |\n' 
                               '  0    |\n' 
                              ' /|\   |\n' 
                              ' / \   |\n' 
                               '       |\n' 
                               '  _____|__',         
                    }
        
        print(forcas[total_erradas])

        return

    def descreve_letras(self, palavra):
        
        espacos = ['_']*len(palavra)
        letras = self.letras_certas

        for indice, letra in enumerate(palavra):
            if letra in letras:
                espacos[indice] = letra

        print('Enigma: ' + ' '.join(espacos))

        return
    
    def lista_certas(self):
        
        print('Letras certas: ' + ', '.join(self.letras_certas))

        return

    def lista_erradas(self):

        print('Letras erradas: ' + ', '.join(self.letras_erradas))

        return

def main():

    palavras = ['alpha', 'beta', 'omega','delta', 'zeta', 'epsilon', 'phi', 'csi', 'sigma', 'rho']
    
    Jogo01 = jogo_da_forca()
    Jogo01.novo_jogo(palavras)
    
    return

if __name__ == "__main__":
    main()