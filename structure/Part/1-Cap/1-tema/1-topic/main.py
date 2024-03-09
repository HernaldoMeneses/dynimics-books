class Topico:
    def __init__(self, tema, tese, def_tese, solution, brain_storm, frases, tab, img):
        self.tema = tema
        self.tese = tese
        self.def_tese = def_tese
        self.solution = solution
        self.brain_storm = brain_storm
        self.frases = frases
        self.tab = tab
        self.img = img

    def definir_tema(self, new_tema):
        self.tema = new_tema

    def definir_tese(self, new_tese):
        self.tese = new_tese
    
    def definir_def_tese(self, new_def_tese):
        self.def_tese = new_def_tese
    
    def definir_solution(self, new_solution):
        self.solution = new_solution
    
    def definir_brain_srotm(self, new_brain_srotm):
        self.brain_storm = new_brain_srotm

    def definir_frases(self, new_frases):
        self.frases = new_frases
    
    def definir_tab(self, new_tab):
        self.tab = new_tab
    
    def definir_img(self, new_img):
        self.img = new_img

    def imprimir_informacoes(self):
        print(f"\nTema - : {self.tema}")
        print(f"\n\tTese - : {self.tese}")
        print(f"\n\tDefence - : {self.def_tese}")
        print(f"\n\tSolution - : {self.solution}")
        print(f"\nBrain_Storm - : {self.brain_storm}\n")
        
        cout=1
        for i in (self.frases):
            print(f"Frase - : {cout} {i}")
            cout = cout +1

        print(f"\nTab - :")
        print(f"\n{self.tab}\n")

        plt.imshow(img_)
        plt.show()

#_____________________________________________________________________/

def read_file(file_):
    # Nome do arquivo
    nome_arquivo = file_

    # Tente abrir o arquivo para leitura
    try:
        with open(nome_arquivo, 'r') as arquivo:
            # Leia o conteúdo do arquivo e armazene-o em uma variável
            conteudo = arquivo.read()

            # Exiba o conteúdo lido (opcional)
            #print("Conteúdo do arquivo:")
            #print(conteudo)
            return conteudo

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

#_____________________________________________________________________/

def read_lines_file(file_line_read):
    # Nome do arquivo
    nome_arquivo = file_line_read

    # Lista para armazenar as linhas do arquivo
    list_lines = []
    # Tente abrir o arquivo para leitura
    try:
        with open(nome_arquivo, 'r') as arquivo:
            # Leia as linhas do arquivo e armazene-as na lista
            #list_lines = arquivo.readlines()
            list_lines = [linha.strip() for linha in arquivo.readlines()]
            
        return list_lines

    except FileNotFoundError:
        print(f"O arquivo '{nome_arquivo}' não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


#_____________________________________________________________________/



file_ = 'data\\1-tema.txt'
tema_ = read_file(file_)
file_ = 'data\\2-tese.txt'
tese_ = read_file(file_)
file_ = 'data\\3-def_tese.txt'
def_tese_ = read_file(file_)
file_ = 'data\\4-solution.txt'
solution_ = read_file(file_)
file_ = 'data\\5-brain_storm.txt'
brain_storm_ = read_lines_file(file_)
file_ = 'data\\6-frases.txt'
frases_ = read_lines_file(file_)

import pandas as pd
file_ = 'data\\7-Pasta1.xlsx'
tab_ = pd.read_excel(file_)

import matplotlib.pyplot as plt 
import matplotlib.image as mpimg
file_ = 'data\\8-img1.jpg'
img_ = mpimg.imread(file_)


topic1 = Topico(
    tema=tema_, 
    tese=tese_, 
    def_tese=def_tese_, 
    solution=solution_, 
    brain_storm=brain_storm_,
    frases=frases_,
    tab=tab_,
    img=img_)
topic1.imprimir_informacoes()
