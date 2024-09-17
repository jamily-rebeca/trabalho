from pacientes import Paciente, Pacientes_CRUD
from amanda import Consulta, Consultas_CRUD
from medico import Medico, Medico_CRUD

def inserir_paciente(nome, idade, fone , cpf):
    obj = Paciente(0, nome, idade, fone, cpf)
    Pacientes_CRUD.inserir(obj)


def listar_pacientes():
    return Pacientes_CRUD.listar()

def listar_pacientes_id(id_paciente):
    return Pacientes_CRUD.listar_id_paciente(id_paciente)
    
def atualizar_paciente(id, nome, idade, fone, cpf):
    obj = Paciente(id, nome, idade, fone, cpf)
    Pacientes_CRUD.atualizar(obj)

def excluir_paciente(id):
    Pacientes_CRUD.excluir(id)

