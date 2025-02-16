from pacientes import Paciente, Pacientes_CRUD
from consultas import Consulta, Consultas_CRUD
from medico import Medico, Medico_CRUD

class View:
    @staticmethod
    def inserir_paciente(nome, idade, fone, cpf):
        obj = Paciente(0, nome, idade, fone, cpf)
        Pacientes_CRUD.inserir(obj)

    @staticmethod
    def listar_pacientes():
        return Pacientes_CRUD.listar()

    @staticmethod
    def listar_pacientes_id(id_paciente):
        return Pacientes_CRUD.listar_id_paciente(id_paciente)

    @staticmethod
    def atualizar_paciente(id, nome, idade, fone, cpf):
        obj = Paciente(id, nome, idade, fone, cpf)
        Pacientes_CRUD.atualizar(obj)

    @staticmethod
    def excluir_paciente(id):
        Pacientes_CRUD.excluir(id)

    @staticmethod
    def inserir_medico(nome, especificacao):
        obj = Medico(0, nome, especificacao)
        Medico_CRUD.inserir(obj)

    @staticmethod
    def listar_medicos():
        return Medico_CRUD.listar()

    @staticmethod
    def listar_medicos_id(id_medico):
        return Medico_CRUD.listar_id_medico(id_medico)

    @staticmethod
    def atualizar_medico(id, nome, especificacao):
        obj = Medico(id, nome, especificacao)
        Medico_CRUD.atualizar(obj)

    @staticmethod
    def excluir_medico(id):
        Medico_CRUD.excluir(id)

    @staticmethod
    def inserir_consulta(id_paciente, id_medico, especificacao, horario):
        obj = Consulta(0, id_paciente, id_medico, especificacao, horario)
        Consultas_CRUD.inserir(obj)

    @staticmethod
    def listar_consultas(id_paciente):
        return Consultas_CRUD.listar(id_paciente)

    @staticmethod
    def listar_consultas_especificacao(id_paciente, especificacao):
        return Consultas_CRUD.listar_id(id_paciente, especificacao)

    @staticmethod
    def atualizar_consulta(id_consulta, id_paciente, id_medico, especificacao, horario):
        obj = Consulta(id_consulta, id_paciente, id_medico, especificacao, horario)
        Consultas_CRUD.atualizar(obj)

    @staticmethod
    def excluir_consulta(id_consulta):
        Consultas_CRUD.excluir(id_consulta)
