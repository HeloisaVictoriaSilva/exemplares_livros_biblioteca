class Exemplar:
    def __init__(self, id_Exemplar: int):
        self.__id_Exemplar = id_Exemplar
        self.__status = 0
        self.__qtde_Emprestimos = 0

    #get e set
    @property
    def id_Exemplar(self):
        return self.__id_Exemplar
    
    @property
    def qtde_Emprestimo(self):
        return self.__qtde_Emprestimos
    
    @qtde_Emprestimo.setter
    def qtde_Emprestimo(self, qtde_Emprestimo):
        self.__qtde_Emprestimos = qtde_Emprestimo
    
    @property
    def status(self):
        return self.__status
    
    @status.setter
    def status(self, status):
        self.__status = status

    # metodos
    # def exemplar(self, id_Exemplar):
    #     self.__status = 0
    #     self.__qtde_Emprestimos = 0
    
    def registrar_emprestimo(self) -> bool:
        if self.__status in (1,2):
            self.__qtde_Emprestimos += 1
            self.__status = 3
            return True
        else:
            return False
        
    def registrar_devolucao(self) -> bool:
        if self.__status == 3 :
            if self.__qtde_Emprestimos >= 100:
                self.__status = 5
                self.__qtde_Emprestimos = 0
                return True
            else: 
                self.__status = 1
                return True
        else:
            return False
        
    def alterar_status(self, status) -> bool:
        status_Anterior = self.__status
        if self.__status in (0,2):
            self.__status = 1
        elif self.__status == 1 and status in (2,5,9):
            self.__status = status
        elif self.__status == 3 and status == 4:
            self.__status = status
        elif self.__status == 5 and status in (1,2):
            self.__status = status
        return status_Anterior != self.__status


if __name__ == "__main__":
    #print("--- Demonstração Fiel ao Diagrama ---")
    livro = Exemplar(id_Exemplar=777)
    
    print(f"Criado o ID: {livro.id_Exemplar}, Status: {livro.status}, Empréstimos: {livro.qtde_Emprestimo}")

    livro.alterar_Status(9)
    print(f"Após alterar o status do ID: {livro.id_Exemplar}, Status: {livro.status}, Empréstimos: {livro.qtde_Emprestimo}")

    sucesso = livro.registrar_Emprestimo()
    print(f"Empréstimo bem-sucedido: {sucesso}")
    print(f"Após empréstimo o ID: {livro.id_Exemplar}, Status: {livro.status}, Empréstimos: {livro.qtde_Emprestimo}")