from Funcionario import Funcionario


class Departamento:
    def __init__(self, codigo: str):
        self._codigo = codigo
        self._funcionarios: list[Funcionario] = [] 

    @property
    def codigo(self) -> str:
        return self._codigo
    
    @property
    def funcionarios(self) -> list[Funcionario]:
        return self._funcionarios

    def adicionar_funcionario(self, funcionario: Funcionario) -> bool:
        self._funcionarios.append(funcionario)
        return True
    
    def exibir(self):
        print(f'    - {self._codigo}')

