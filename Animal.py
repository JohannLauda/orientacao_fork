class Animal:
    def __init__(self, numero_de_patas: int):
        self.numero_de_patas = numero_de_patas
        
    def fazer_barulho(self) -> str:
        self.barulho = "Eu sou um animal"
        return self.barulho
        
class Cachorro(Animal):
    def __init__(self, numero_de_patas: int, cor: str) -> str:
        super().__init__(numero_de_patas)
        self.cor = cor
        
    def fazer_barulho(self) -> str:
        self.auau = "AU AU !!!!"
        return self.auau
        

    

    