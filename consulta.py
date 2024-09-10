from datetime import datetime
import json
from paciente import Paciente_CRUD
from medico import Medico_CRUD

class Consulta:
    def __init__(self, id_consulta, id_paciente, id_medico, especificacao, horario:datetime):
        self.set_id_consulta(id_consulta)
        self.set_idPaciente(id_paciente)
        self.set_idMedico(id_medico)
        self.set_especificacao(especificacao)
        self.set_horario(horario)

    def set_id_consulta(self, id_consulta:int):
        self.id_consulta = id_consulta

    def get_id_consulta(self):
        return self.id_consulta
    
    def set_idPaciente(self, id_paciente:int):
        self.id_paciente = id_paciente

    def get_idPaciente(self):
        return self.id_paciente

    def set_idMedico(self, id_medico:int):
        self.id_medico = id_medico

    def get_idMedico(self):
        return self.id_medico

    def set_especificacao(self, especificacao:str):
        self.especificacao = especificacao

    def get_especificacao(self):
        return self.especificacao

    def set_horario(self, horario:datetime):
        self.horario = horario

    def get_horario(self):
        strHorario = datetime.strftime(self.horario, "%d/%m/%Y %H:%M")
        return strHorario

    def __str__(self):
        return f"{self.get_id_consulta()} - {self.get_idPaciente()} - {self.get_idMedico()} - {self.get_especificacao()} - {self.get_horario()}"

class Consultas_CRUD:
    objetos = []

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("consultas.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Consulta(obj["id_consulta"], obj["id_paciente"], obj["id_medico"], obj["especificacao"], datetime.strptime(obj["horario"], "%d/%m/%Y %H:%M"))
                    cls.objetos.append(c)
        except FileNotFoundError:
            pass

    @staticmethod
    def modo(obj):
        if isinstance(obj, datetime):
            return datetime.strftime(obj, "%d/%m/%Y %H:%M")
        return vars(obj)

    @classmethod
    def salvar(cls):
        with open("consultas.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Consultas_CRUD.modo)

    @classmethod
    def inserir(cls, obj:Consulta):
        cls.abrir()
        x = 0
        for y in cls.objetos:
            if y.get_id_consulta() > x:
                x = y.get_id_consulta()
        obj.set_id_consulta(x + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls, id_paciente):
        Paciente_CRUD.abrir()
        consultas = []
        for paciente in Paciente_CRUD.objetos:
            if id_paciente == paciente.get_idPaciente():
                cls.abrir()
                for consulta in cls.objetos:
                    if id_paciente == consulta.get_idPaciente():
                        consultas.append(consulta)
        return consultas

    @classmethod
    def listar_id(cls, id_paciente, id_medico):
        if not id_paciente or not id_medico:
            raise ValueError("Dados inválidos")
        Paciente_CRUD.abrir()
        Medico_CRUD.abrir()
        consultas = []
        for paciente in Paciente_CRUD.objetos:
            if id_paciente == paciente.get_idPaciente():
                for medico in Medico_CRUD.objetos:
                    if id_medico == medico.get_idMedico():
                        cls.abrir()
                        for consulta in cls.objetos:
                            if id_paciente == consulta.get_idPaciente() and id_medico == consulta.get_idMedico():
                                consultas.append(consulta)
        return consultas

    @classmethod
    def atualizar(cls, consulta:Consulta):
        cls.abrir()
        for x in cls.objetos:
            if consulta.get_id_consulta() == x.get_id_consulta():
                x.set_idPaciente(consulta.get_idPaciente())
                x.set_idMedico(consulta.get_idMedico())
                x.set_especificacao(consulta.get_especificacao())
                x.set_horario(consulta.get_horario())
                cls.salvar()
                return
        raise ValueError("Consulta não encontrada")

    @classmethod
    def excluir(cls, id_consulta):
        if id_consulta:
            cls.abrir()
            for obj in cls.objetos:
                if id_consulta == obj.get_id_consulta():
                    cls.objetos.remove(obj)
                    cls.salvar()
                    return
            raise ValueError("Consulta não encontrada")