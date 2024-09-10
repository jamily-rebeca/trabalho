import json
from datetime import datetime


class Cliente:
    def __init__(self, id, nome, email, fone, nasc:datetime):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_nasc(nasc)

    def set_id(self, id:int):

        self.id = id


    def get_id(self):
        return self.id

    def set_nome(self, nome:str):
        if nome:
            self.nome = nome
        else:
            raise ValueError

    def get_nome(self):
        return self.nome

    def set_email(self, email:str):
        if email:
            self.email = email
        else:
            raise ValueError

    def get_email(self):
        return self.email

    def set_fone(self, fone:str):
        if fone:
            self.fone = fone
        else:
            raise ValueError

    def get_fone(self):
        return self.fone

    def set_nasc(self, nasc:datetime):
        today = datetime.now()
        if nasc > today:
            raise ValueError("informe uma data válida")
        if nasc <= today:
            self.nasc = nasc

    def get_nasc(self):
        time = datetime.strftime(self.nasc, "%d/%m/%Y")
        return time

    def __str__(self):
        return f"{self.get_id()} - {self.get_nome()} - {self.get_email()} - {self.get_fone()} - {self.get_nasc()}"


class Clientes:
    objetos = []
    @classmethod
    def abrir(cls):
        cls.objetos: list[Cliente] = []
        try:
            with open("clientes.json", mode="r") as arquivo:   # r - read
                texto = json.load(arquivo)
                for obj in texto:   
                    c = Cliente(obj["id"], obj["nome"], obj["email"], obj["fone"], datetime.fromisoformat(obj["nasc"]))
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @staticmethod
    def modo(obj):
        if isinstance(obj, datetime):
            return datetime.isoformat(obj)
        return vars(obj)

    @classmethod
    def salvar(cls):
        with open("clientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default = Clientes.modo)

    @classmethod
    def inserir(cls, obj:Cliente):#eu vou receber todos os atributos com exceção do id. Então eu crio um
        cls.abrir()#eu poderia criar um random.radint para criar um id pouco provável  de se repetir, mas n
        x=0
        for y in cls.objetos:
            if y.id > x:
                x = y.id
        obj.id = x + 1
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        for obj in cls.objetos:
            print(obj)

    @classmethod
    def listar_id(cls, id):
        if id:
            cls.abrir()
            for obj in cls.objetos:
                if id == obj.id:
                    print(obj)
        else:
            raise ValueError("preencher este campo")

    @classmethod
    def aniv(cls, mes:int):
        cls.abrir()
        # aniversariantes = []
        for obj in cls.objetos:
            if mes == obj.nasc.month: 
                # aniversariantes.append(obj)
                print(obj.nome)



    @classmethod
    def atualizar(cls, c:Cliente):#nesse objeto o cliente me fornecerá o id de usuário e os demais atributos serão para a troca
        cls.abrir()
        for x in cls.objetos:
            if c.id == x.id:
                x.nome = c.nome
                x.email = c.email
                x.fone = c.fone
                cls.salvar() 

    @classmethod
    def excluir(cls, id):
        if id:
            cls.abrir()
            for obj in cls.objetos:
                if id == obj.id:
                    cls.objetos.remove(obj)
                    cls.salvar()

class UI:
    @staticmethod
    def menu():
        print("1 - inserir cliente\n2 - excluir cliente\n3 - atualizar dados\n4 - listar usuários\n5 - listar meus dados\n6 - aniversariantes\n7 - sair")
        x = int(input("digite um comando: "))
        if x >= 1 and x <=6:
            return x
        else:
            raise ValueError ("informe um comando válido")

    @staticmethod
    def main():
        x = UI.menu()
        if x == 1:
            UI.inserir()
        if x == 2:
            UI.excluir()
        if x == 3:
            UI.atualizar()
        if x == 4:
            UI.listar()
        if x == 5:
            UI.listar_id()
        if x == 6:
            UI.aniversariantes()

        print("fim")

    @staticmethod
    def inserir():

        nome = input("digite o nome do usuário: ")
        email = input("digite o email do usuário: ")
        fone = input("digite o telefone do usuário: ")
        nascimento_str = input("digite a data de nascimento do cliente no formato dd/mm/aaaa: ")

        nasc = datetime.strptime(nascimento_str, "%d/%m/%Y")

        obj = Cliente(0, nome, email, fone, nasc)

        Clientes.inserir(obj)

    @staticmethod
    def excluir():
        id = int(input("digite o id do usuário que desejas excluir: "))

        Clientes.excluir(id)

    @staticmethod
    def atualizar():
        id = int(input("digite o id do usuário que terá seus dados modificados: "))
        nome = input("digite o novo nome do usuário: ")
        email = input("digite o novo email do usuário: ")
        fone = input("digite o novo telefone do usuário: ")
        nascimento_str = input("digite a data de nascimento do cliente no formato dd/mm/aaaa: ")


        nasc = datetime.strptime(nascimento_str, "%d/%m/%Y")

        c = Cliente(id, nome, email, fone, nasc)

        Clientes.atualizar(c)

    @staticmethod
    def listar():
        Clientes.listar()

    @staticmethod
    def listar_id():
        id = int(input("digite seu id: "))
        Clientes.listar_id(id)

    @staticmethod
    def aniversariantes():
        mes = int(input("qual o mês dos aniversários (em número)? "))
        Clientes.aniv(mes)

UI.main()