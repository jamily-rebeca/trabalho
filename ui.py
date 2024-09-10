from datetime import datetime
import json
from clientes import Cliente, Clientes_CRUD
from horarios import Horario, Horarios_CRUD
from servicos import Servico, Servico_CRUD

class UI:
    @staticmethod
    def menu_main():
        print("1 - Clientes\n2 - Horários\n3 - serviços\n4 - Sair")
        op = int(input("digite uma opção: "))
        if op > 0 and op <= 4:
            return op

    @staticmethod
    def main():
        op = UI.menu_main()
        if op == 1:
            UI_clientes.main_clientes()
        if op == 2:
            UI_horarios.main_horarios()
        if op == 3:
            UI_servicos.main_servicos()
        if op == 4:
            print("fim")

class UI_clientes:
    @staticmethod
    def menu_clientes():
        print("1 - inserir cliente\n2 - listar clientes\n3 - listar por id\n4 - atualizar dados\n5 - excluir cliente\n6 - sair")
        op = int(input("digite um comando: "))
        if op > 0 and op <= 6:
            return op

    @staticmethod
    def main_clientes():
        op = UI_clientes.menu_clientes()
        if op == 1:
            UI_clientes.inserir()
        if op == 2:
            UI_clientes.listar()
        if op == 3:
            UI_clientes.listar_id()
        if op == 4:
            UI_clientes.atualizar()
        if op == 5:
            UI_clientes.excluir()
        if op == 6:
            UI.main()

    @staticmethod
    def inserir():
        nome = input("digite o nome do usuário: ")
        email = input("digite o email do usuário: ")
        fone = input("digite o telefone do usuário: ")

        obj = Cliente(0, nome, email, fone)

        Clientes_CRUD.inserir(obj)

        UI_clientes.main_clientes()

    @staticmethod
    def listar():
        Clientes_CRUD.listar()
        UI_clientes.main_clientes()


    @staticmethod
    def listar_id():
        id_cliente = int(input("digite seu id: "))
        Clientes_CRUD.listar_id_cliente(id_cliente)
        UI_clientes.main_clientes()


    @staticmethod
    def atualizar():
        id = int(input("digite o id do usuário que terá seus dados modificados: "))
        nome = input("digite o novo nome do usuário: ")
        email = input("digite o novo email do usuário: ")
        fone = input("digite o novo telefone do usuário: ")

        c = Cliente(id, nome, email, fone)

        Clientes_CRUD.atualizar(c)
        UI_clientes.main_clientes()

    @staticmethod
    def excluir():
        id = int(input("digite o id do usuário que desejas excluir: "))
        Clientes_CRUD.excluir(id)
        UI_clientes.main_clientes()

class UI_servicos:
    @staticmethod
    def menu_servicos():
        print("1 - inserir serviço\n2 - listar serviços\n3 - listar por id\n4 - atualizar dados\n5 - excluir serviço\n6 - sair")
        op = int(input("digite um comando: "))
        if op > 0 and op <= 6:
            return op

    @staticmethod
    def main_servicos():
        op = UI_servicos.menu_servicos()
        if op == 1:
            UI_servicos.inserir()
        if op == 2:
            UI_servicos.listar()
        if op == 3:
            UI_servicos.listar_id()
        if op == 4:
            UI_servicos.atualizar()
        if op == 5:
            UI_servicos.excluir()
        if op == 6:
            UI.main()

    @staticmethod
    def inserir():
        descricao = input("digite uma descrição do serviço: ")
        valor = float(input("digite o valor que o serviço custará: "))
        duracao = int(input("digite quanto tempo este serviço irá durar: "))

        obj = Servico(0, descricao, valor, duracao)

        Servico_CRUD.inserir(obj)
        UI_servicos.menu_servicos()

    @staticmethod
    def listar():
        Servico_CRUD.listar()
        UI_servicos.menu_servicos()

    @staticmethod
    def listar_id():
        id = int(input("digite o id: "))
        Servico_CRUD.listar_id_servico(id)
        UI_servicos.menu_servicos()

    @staticmethod
    def atualizar():
        id = int(input("digite o id do serviço que terá seus dados modificados: "))
        descricao = input("digite a nova descrição do serviço: ")
        valor = float(input("digite o novo valor do serviço: "))
        duracao = int(input("digite a nova duração do serviço: "))

        s = Servico(id, descricao, valor, duracao)

        Servico_CRUD.atualizar(s)
        UI_servicos.menu_servicos()

    @staticmethod
    def excluir():
        id = int(input("digite o id do usuário que desejas excluir: "))

        Servico_CRUD.excluir(id)
        UI_servicos.menu_servicos()

class UI_horarios:
    @staticmethod
    def menu_horarios():
        print("1 - marcar horário\n2 - listar meus horários\n3 - listar meus horários em determinado serviço\n4 - atualizar\n5 - sair")
        op = int(input("digite uma opção: "))
        if op > 0 and op <= 6:
            return op

    @staticmethod
    def main_horarios():
        op = UI_horarios.menu_horarios()
        if op == 1:
            UI_horarios.inserir()
        if op == 2:
            UI_horarios.listar()
        if op == 3:
            UI_horarios.listar_id()
        if op == 4:
            UI_horarios.atualizar()
        if op == 5:
            UI.main()

    @staticmethod
    def inserir():
        id_cliente = int(input("digite o seu id: "))
        id_servico = int(input("digite o id do serviço: "))
        datastr = input("digite a data no formato dd/mm/aaaa: ")
        data = datetime.strptime(datastr, "%d/%m/%Y")

        obj = Horario(0, id_cliente, id_servico, True, data)

        Horarios_CRUD.inserir(obj)
        UI_horarios.menu_horarios()

    @staticmethod
    def listar():
        id = int(input("qual o seu id? "))
        Horarios_CRUD.listar(id)
        UI_horarios.menu_horarios()

    @staticmethod
    def listar_id():
        id_cliente = int(input("digite o seu id: "))
        id_servico = int(input("digite o id do serviço: "))
        Horarios_CRUD.listar_id(id_cliente, id_servico)
        UI_horarios.menu_horarios()

    @staticmethod
    def atualizar():
        id_cliente = id(input("digite o seu id: "))
        id_servico = int(input("digite o id do novo serviço: "))
        datastr = input("digite a nova data no formato dd/mm/aaaa: ")
        data = datetime.strptime(datastr, "%d/%m/%Y")

        obj = Horario(0, id_cliente, id_servico, True, data)

        Horarios_CRUD.atualizar(obj)
        UI_horarios.menu_horarios()

    @staticmethod
    def excluir():
        id = int(input("digite o id do usuário que desejas excluir: "))

        Horarios_CRUD.excluir(id)
        UI_horarios.menu_horarios()



UI.main()