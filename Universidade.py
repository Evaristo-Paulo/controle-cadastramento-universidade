from Departamento import Departamento, Funcionario


class Universidade:
    def __init__(self, nome: str):
        self._nome = nome
        self._departamentos: list[Departamento] = [] # --check-untyped-

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def departamentos(self) -> list[Departamento]:
        return self._departamentos
    
    def adicionar_departamento(self, codigo_departamento: str) -> bool:
        novo_departamento = Departamento(codigo_departamento)
        self._departamentos.append(novo_departamento)
        return True
    
    def buscar_departamento(self, pesquisa) -> Departamento | None:
        for departamento in self._departamentos:
            if departamento.codigo == pesquisa:
                return departamento
        return None
    
    def listar_departamentos(self):
        for departamento in self._departamentos:
            departamento.exibir()

    def listar_departamentos_respectivos_funcionarios(self):
        for departamento in self._departamentos:
            print(' - Departamento:')
            departamento.exibir()
            print('        - Funcionário:')
            for funcionario in departamento.funcionarios:
                funcionario.exibir()

    def buscar_funcionario(self, pesquisa) -> Funcionario | None:
        for departamento in self._departamentos:
            for funcionario in departamento.funcionarios:
                if funcionario.nome == pesquisa:
                    return funcionario
        return None
    
    def listar_funcionarios(self, filtro=None):
        if filtro is None:
            for departamento in self._departamentos:
                for funcionario in departamento.funcionarios:
                    funcionario.exibir()
        else:
            for departamento in self._departamentos:
                for funcionario in departamento.funcionarios:
                    if funcionario.tipo == filtro:
                        funcionario.exibir()


