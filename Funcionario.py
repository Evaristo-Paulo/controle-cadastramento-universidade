class Funcionario:
    def __init__(self, nome: str, tipo: str):
        self._nome = nome
        self._tipo = tipo

    @property
    def tipo(self) -> str:
        return self._tipo
    
    @property
    def nome(self) -> str:
        return self._nome
    
    def exibir(self):
        print(f'            - {self._nome} ({self._tipo})')
