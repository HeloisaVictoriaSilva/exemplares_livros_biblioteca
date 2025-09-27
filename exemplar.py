class Exemplar:
    def __init__(self, id_Exemplar, status, qtde_Emprestimo):
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
    def exemplar(self, id_Exemplar):
        self.__status = 0
        self.__qtde_Emprestimos = 0
    
    def registrar_Empretimo(self) -> bool:
        if self.__status in (1,2):
        #== 1 or self.__status == 2:
            self.__qtde_Emprestimos += 1
            self.__status = 3
            return True
        else:
            return False
        
    def registar_Devolucao(self) -> bool:
        if self.__status == 3 :
            if self.__qtde_Emprestimos >= 100:
                self.__status = 5
                self.__qtde_Emprestimos = 0
            else: 
                self.__status = 1
                return True
        # elif self.__status == 3 and self.__qtde_Emprestimos < 100:
        #     self.__status = 1
        else:
            return False
        
    def alterar_Status(self, status) -> bool:
        status_Anterior = self.__status
        if self.__status in (0,2):
        #== 0 or self.__status == 2:
            self.__status = 1
            return True
        elif self.__status == 1 and status in (2,5,9):
            self.__status = status
            return True
        elif self.__status == 3 and status == 4:
            self.__status = status
            return True
        elif self.__status == 5 and status in (1,2):
            self.__status = status
            return True
        if status_Anterior != self.__status:
            return self.__status
        else:
            return ''
