from datetime import datetime
import json
from pacientes import Pacientes_CRUD
from medico import Medico_CRUD


class Consulta:
    def __init__(
        self, id_consulta, id_paciente, id_medico, especificacao, horario: datetime
    ):
        self.set_idConsulta(id_consulta)
        self.set_idPaciente(id_paciente)
        self.set_idMedico(id_medico)
        self.set_especificacao(especificacao)
        self.set_horario(horario)

    def set_idConsulta(self, id_consulta: int):
        self.id_consulta = id_consulta

    def get_idConsulta(self):
        return self.id_consulta

    def set_idPaciente(self, id_paciente: int):
        self.id_paciente = id_paciente

    def get_idPaciente(self):
        return self.id_paciente

    def set_idMedico(self, id_medico: int):
        self.id_medico = id_medico

    def get_idMedico(self):
        return self.id_medico

    def set_especificacao(self, especificacao: str):
        if especificacao:
            self.especificacao = especificacao
        else:
            raise ValueError("determine uma especificação")

    def get_especificacao(self):
        return self.especificacao

    def set_horario(self, horario: datetime):
        today = datetime.now()
        if horario > today:
            self.horario = horario
        else:
            raise ValueError("determine um horário válido")

    def get_horario(self):
        strHorario = datetime.strftime(self.horario, "%d/%m/%Y %H:%M")
        return strHorario

    def __str__(self):
        return f"\nid_consulta: {self.get_idConsulta()} | id_paciente: {self.get_idPaciente()} | id_médico: {self.get_idMedico()} | especificação: {self.get_especificacao()} | horário: {self.get_horario()}"


class Consultas_CRUD:
    objetos_consulta: list[Consulta] = []

    @classmethod
    def abrir(cls):
        cls.objetos_consulta = []
        try:
            with open("consultas.json", mode="r") as arquivo:
                texto = json.load(arquivo)
                for obj in texto:
                    c = Consulta(
                        obj["id_consulta"],
                        obj["id_paciente"],
                        obj["id_medico"],
                        obj["especificacao"],
                        datetime.strptime(obj["horario"], "%d/%m/%Y %H:%M"),
                    )
                    cls.objetos_consulta.append(c)
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
            json.dump(cls.objetos_consulta, arquivo, default=Consultas_CRUD.modo)

    @classmethod
    def inserir(cls, obj: Consulta):
        cls.abrir()
        x = 0
        for y in cls.objetos_consulta:
            if y.id_consulta > x:
                x = y.id_consulta
        obj.id_consulta = x + 1
        cls.objetos_consulta.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls, id_paciente):
        # na UI vou verificar se o id_paciente é válido e realmente existe na class Cliente
        consultas = []
        cls.abrir()
        for x in cls.objetos_consulta:
            if x.id_paciente == id_paciente:
                consultas.append(x)
        return consultas

    @classmethod
    def listar_id(cls, id_paciente, especificacao):
        if not id_paciente or not especificacao:
            raise ValueError("preencha os campos corretamente")
        # verificar se o id do paciente e especificacao é realmente válido na class UI
        consultas = []
        for x in Pacientes_CRUD.objetos_pacientes:
            if x.id_paciente == id_paciente:
                for y in Medico_CRUD.objetos_medicos:
                    if y.especificacao == especificacao:
                        for z in cls.objetos_consulta:
                            if (
                                z.id_paciente == id_paciente
                                and z.especificacao == especificacao
                            ):
                                consultas.append(z)
        return consultas

    @classmethod
    def atualizar(cls, consulta: Consulta):
        cls.abrir()
        for x in cls.objetos_consulta:
            if consulta.id_consulta == x.id_consulta:
                x.set_idPaciente(consulta.get_idPaciente())
                x.set_idMedico(consulta.get_idMedico())
                x.set_especificacao(consulta.get_especificacao())
                x.set_horario(consulta.get_horario())
                cls.salvar()
                return
            else:
                raise ValueError("id não encontrado")

    @classmethod
    def excluir(cls, id_consulta):
        if id_consulta:
            cls.abrir()
            for obj in cls.objetos_consulta:
                if id_consulta == obj.id_consulta:
                    cls.objetos_consulta.remove(obj)
                    cls.salvar()
                    return
            raise ValueError("Consulta não encontrada")
