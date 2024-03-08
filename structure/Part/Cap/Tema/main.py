class Topico:
    def __init__(self, tema, tese, solution, brain_storm, frases):
        self.tema = tema
        self.tese = tese
        self.solution = solution
        self.brain_storm = brain_storm
        self.frases = frases

    def definir_tema(self, new_tema):
        self.tema = new_tema

    def definir_tese(self, new_tese):
        self.tese = new_tese
    
    def definir_solution(self, new_solution):
        self.solution = new_solution
    
    def definir_brain_srotm(self, new_brain_srotm):
        self.brain_storm = new_brain_srotm

    def definir_brain_srotm(self, new_frases):
        self.frases = new_frases

    def imprimir_informacoes(self):
        print(f"\nTema: {self.tema},\n\tTese: {self.tese}")
        print(f"\t\tSolution: {self.solution}")
        print(f"\nBrain_Storm: {self.brain_storm}\n")
        cout =1
        for i in (self.frases):
            print(f"Frase: {cout} {i}")
            cout = cout +1

# Exemplo de uso da classe
tema_ = 'Tema - Titulo Abordado'
tese_ = 'Tese - O que afirma?'
solution_ = 'Solution - Desfecho Aplicado'
brain_storm_ = [
    'Word1',
    'word2',
    'word3']
frases_ = [
    'frase1','frase2']
tablelas =  {
    'Campo1': ['registe1', 'registe2', 'registe3', 'registe4'],
    'Campo2': [1, 2, 3, 4],
    'Campo3': ['registe1', 'registe2', 'registe3', 'registe4']
}

topic1 = Topico(
    tema=tema_, 
    tese=tese_, 
    solution=solution_, 
    brain_storm=brain_storm_,
    frases=frases_)
topic1.imprimir_informacoes()