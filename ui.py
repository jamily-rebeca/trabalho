from datetime import datetime
import json
from pacientes import Paciente, Pacientes_CRUD
from amanda import Consulta, Consultas_CRUD
from medico import Medico, Medico_CRUD

class UI:
    @staticmethod
    def menu_main():
        print("1 - Pacientes\n2 - Consultas\n3 - Médicos\n4 - Sair")
        op = int(input("digite uma opção: "))
        if op > 0 and op <= 4:
            return op

    @staticmethod
    def main():
        op = UI.menu_main()
        if op == 1:
            UI_pacientes.main_pacientes()
        if op == 2:
            UI_consultas.main_consultas()
        if op == 3:
            UI_medicos.main_medicos()
        if op == 4:
            print("fim")

class UI_pacientes:
    @staticmethod
    def menu_pacientes():
        print("1 - inserir paciente\n2 - listar pacientes\n3 - listar pacientes por id\n4 - atualizar dados\n5 - excluir paciente\n6 - sair")
        op = int(input("digite um comando: "))
        if op > 0 and op <= 6:
            return op

    @staticmethod
    def main_pacientes():
        op = UI_pacientes.menu_pacientes()
        if op == 1:
            UI_pacientes.inserir()
        if op == 2:
            UI_pacientes.listar()
        if op == 3:
            UI_pacientes.listar_id()
        if op == 4:
            UI_pacientes.atualizar()
        if op == 5:
            UI_pacientes.excluir()
        if op == 6:
            UI.main()

    @staticmethod
    def inserir():
        nome = input("digite o nome do paciente: ")
        fone = input("digite o telefone do cliente: ")
        cpf = input("digite o cpf do cliente: ")
        idade = int(input("digite a idade do paciente: "))

        obj = Paciente(0, nome, idade, fone, cpf)
        Pacientes_CRUD.inserir(obj)

        UI_pacientes.main_pacientes()

    @staticmethod
    def listar():
        Pacientes_CRUD.listar()
        UI_pacientes.main_pacientes()


    @staticmethod
    def listar_id():
        id_paciente = int(input("digite o id do paciente: "))
        Pacientes_CRUD.listar_id_paciente(id_paciente)
        UI_pacientes.main_pacientes()


    @staticmethod
    def atualizar():
        id = int(input("digite o id do paciente que terá seus dados modificados: "))
        nome = input("digite o novo nome do paciente: ")
        fone = input("digite o novo telefone do paciente: ")
        str_idade = input("digite a idade do paciente: ")
        idade = datetime.strptime(str_idade, "%d/%m/%Y")
        cpf = input("digite o cpf do paciente: ")
        obj = Paciente(id, nome, idade, fone, cpf)
        Pacientes_CRUD.atualizar(obj)
        UI_pacientes.main_pacientes()

    @staticmethod
    def excluir():
        id = int(input("digite o id do paciente que desejas excluir: "))
        Pacientes_CRUD.excluir(id)
        UI_pacientes.main_pacientes()

class UI_medicos:          #DAQUI PARA BAIXO TEM QUE ARRUMAR
    @staticmethod
    def menu_medicos():
        print("1 - inserir médico\n2 - listar médicos\n3 - listar médicos por id\n4 - atualizar dados\n5 - excluir médico\n6 - sair")
        op = int(input("digite um comando: "))
        if op > 0 and op <= 6:
            return op
        else:
            raise ValueError("digite um valor válido")
        
    @staticmethod
    def main_medicos():
        op = UI_medicos.menu_medicos()
        if op == 1:
            UI_medicos.inserir()
        if op == 2:
            UI_medicos.listar()
        if op == 3:
            UI_medicos.listar_id()
        if op == 4:
            UI_medicos.atualizar()
        if op == 5:
            UI_medicos.excluir()
        if op == 6:
            UI.main()

    @staticmethod
    def inserir():
        nome = input("digite o nome do médico: ")
        especificacao = input("digite a especificação do médico: ")


        obj = Medico(0, nome, especificacao)

        Medico_CRUD.inserir(obj)
        UI_medicos.menu_medicos()

    @staticmethod
    def listar():
        Medico_CRUD.listar()
        UI_medicos.menu_medicos()

    @staticmethod
    def listar_id():
        id = int(input("digite o id: "))
        Medico_CRUD.listar_id_medico(id)
        UI_medicos.menu_medicos()

    @staticmethod
    def atualizar():
        id = int(input("digite o id do médico que terá seus dados modificados: "))
        nome = input("digite o novo nome de médico: ")
        especificacao = input("digite a nova especificação do medico: ")

        obj = Medico(id, nome, especificacao)

        Medico_CRUD.atualizar(obj)
        UI_medicos.menu_medicos()

    @staticmethod
    def excluir():
        id = int(input("digite o id do médico que desejas excluir: "))

        Medico_CRUD.excluir(id)
        UI_medicos.menu_medicos()

class UI_consultas:
    @staticmethod
    def menu_consultas():
        print("1 - marcar consulta\n2 - listar minhas consultas\n3 - listar minhas consultas em determinada especificação\n4 - atualizar\n5 - excluir\n6 - sair" )
        op = int(input("digite uma opção: "))
        if op > 0 and op <= 6:
            return op

    @staticmethod
    def main_consultas():
        op = UI_consultas.menu_consultas()
        if op == 1:
            UI_consultas.inserir()
        if op == 2:
            UI_consultas.listar()
        if op == 3:
            UI_consultas.listar_id()
        if op == 4:
            UI_consultas.atualizar()
        if op == 5:
            UI_consultas.excluir()
        if op == 6:
            UI.main()

    @staticmethod
    def inserir():
        id_paciente = int(input("digite o id do paciente: "))
        id_medico = int(input("digite o id do médico: "))
        especificacao = input("digite a especificação de sua consulta")
        horario_str = input("digite a data de sua consulta no formato dd/mm/aaaa hh:mm: ")
        horario = datetime.strptime(horario_str, "%d/%m/%Y %H:%M")

        obj = Consulta(0, id_paciente, id_medico, especificacao, horario)

        Consultas_CRUD.inserir(obj)
        UI_consultas.menu_consultas()

    @staticmethod
    def listar():
        id = int(input("digite o id do paciente: "))
        Consultas_CRUD.listar(id)
        UI_consultas.menu_consultas()

    @staticmethod
    def listar_id():
        id_paciente = int(input("digite o id do paciente: "))
        especificacao = (input("digite a especificação: "))
        Consultas_CRUD.listar_id(id_paciente, especificacao)
        UI_consultas.menu_consultas()

    @staticmethod
    def atualizar():
        id_consulta = int(input("digite o id da consulta: "))
        id_paciente = int(input("digite o id do paciente: "))
        id_medico = int(input("digite o id do médico: "))
        especificacao = input("digite a especificação de sua consulta: ")
        horario_str = input("digite o novo horário no formato dd/mm/aaaa hh:mm: ")
        horario = datetime.strptime(horario_str, "%d/%m/%Y %H:%M")

        obj = Consulta(id_consulta, id_paciente, id_medico, especificacao, horario)

        Consultas_CRUD.atualizar(obj)
        UI_consultas.menu_consultas()

    @staticmethod
    def excluir():
        id = int(input("digite o id da consulta que desejas excluir: "))

        Consultas_CRUD.excluir(id)
        UI_consultas.menu_consultas()



UI.main()