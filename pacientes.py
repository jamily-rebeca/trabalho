import json
from datetime import datetime

class Paciente:
    def __init__(self, id_paciente, nome, idade, fone, cpf):
        self.set_id_paciente(id_paciente)
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_fone(fone)
        self.set_cpf(cpf)

    def set_id_paciente(self, id_paciente:int):
        self.id_paciente = id_paciente

    def get_id_paciente(self):
        return self.id_paciente

    def set_nome(self, nome:str):
        if nome:
            self.nome = nome
        else:
            raise ValueError ("informe o nome do paciente")

    def get_nome(self):
        return self.nome

    def set_fone(self, fone:str):
        if fone:
            self.fone = fone
        else:
            raise ValueError

    def get_fone(self):
        return self.fone

    def set_cpf(self, cpf:str):
        if cpf:
            self.cpf = cpf
        else:
            raise ValueError ("informe o cpf do paciente")

    def get_cpf(self):
        return self.cpf    

    def set_idade(self, idade:int):
        if idade >= 0:
            self.idade = idade

    def get_idade(self):
        return self.idade


    def __str__(self):
        return f"{self.get_id_paciente()} - {self.get_nome()} - {self.get_idade()} - {self.get_cpf()} - {self.get_fone()}"


class Pacientes_CRUD:
    objetos_pacientes = []
    @classmethod
    def abrir(cls):
        cls.objetos_pacientes: list[Paciente] = []
        try:
            with open("pacientes.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    p = Paciente(obj["id_paciente"], obj["nome"], obj["idade"], obj["fone"], obj["cpf"])
                    cls.objetos_pacientes.append(p)
        except FileNotFoundError:
            pass


    @classmethod
    def salvar(cls):
        with open("pacientes.json", mode="w") as arquivo:
            json.dump(cls.objetos_pacientes, arquivo, default = vars)


    @classmethod
    def inserir(cls, obj:Paciente):#eu vou receber todos os atributos com exceção do id_cliente. Então eu crio um
        cls.abrir()#eu poderia criar um random.radint para criar um id_cliente pouco provável  de se repetir, mas n
        x=0
        for y in cls.objetos_pacientes:
            if y.id_paciente > x:
                x = y.id_paciente
        obj.id_paciente = x + 1
        cls.objetos_pacientes.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        for obj in cls.objetos_pacientes:
            print(obj)

    @classmethod
    def listar_id_paciente(cls, id_paciente):
        if id_paciente:
            cls.abrir()
            for obj in cls.objetos_pacientes:
                if id_paciente == obj.id_paciente:
                    print(obj)
        else:
            raise ValueError("preencher este campo")

    @classmethod
    def atualizar(cls, p:Paciente):#nesse objeto o cliente me fornecerá o id_cliente de usuário e os demais atributos serão para a troca
        cls.abrir()
        for x in cls.objetos_pacientes:
            if p.id_paciente == x.id_paciente:
                x.nome = p.nome
                x.idade = p.idade
                x.fone = p.fone
                x.cpf = p.cpf
                cls.salvar() 

    @classmethod
    def excluir(cls, id_paciente):
        if id_paciente:
            cls.abrir()
            for obj in cls.objetos_pacientes:
                if id_paciente == obj.id_paciente:
                    cls.objetos_pacientes.remove(obj)
                    cls.salvar()