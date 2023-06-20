from aplicacao import database, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Quiz(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    pergunta = database.Column(database.String, nullable=False)
    resposta = database.Column(database.Boolean, nullable=True)




class TermosUso(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    aceito = database.Column(database.Boolean, default=False)

    def __repr__(self):
        return f"TermosUso('{self.id}', '{self.user_id}')"
class Respostas(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    pergunta_id = database.Column(database.Integer, database.ForeignKey('pergunta.id'), nullable=False)
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    resposta = database.Column(database.String, nullable=False)

class Perguntas(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    pergunta = database.Column(database.String, nullable=False)

class Pergunta(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    pergunta = database.Column(database.String, nullable=False)

from flask_sqlalchemy import SQLAlchemy



class Formulario(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    pergunta1 = database.Column(database.String(10))
    pergunta2 = database.Column(database.String(10))
    pergunta3 = database.Column(database.String(10))
    pergunta4 = database.Column(database.String(10))
    pergunta5 = database.Column(database.String(10))
    pergunta6 = database.Column(database.String(10))
    pergunta7 = database.Column(database.String(10))
    pergunta8 = database.Column(database.String(10))
    pergunta9 = database.Column(database.String(10))
    pergunta10 = database.Column(database.String(10))
    pergunta11 = database.Column(database.String(10))

class Formulario3(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    pergunta1 = database.Column(database.String(10))
    pergunta2 = database.Column(database.String(10))
    pergunta3 = database.Column(database.String(10))
    pergunta4 = database.Column(database.String(10))
    pergunta5 = database.Column(database.String(10))
    pergunta6 = database.Column(database.String(10))
    pergunta7 = database.Column(database.String(10))
    pergunta8 = database.Column(database.String(10))
    pergunta9 = database.Column(database.String(10))
    pergunta10 = database.Column(database.String(10))
class Formulario2(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    user_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    pergunta1 = database.Column(database.String(10))
    pergunta2 = database.Column(database.String(10))
    pergunta3 = database.Column(database.String(10))
    pergunta4 = database.Column(database.String(10))
    pergunta5 = database.Column(database.String(10))
    pergunta6 = database.Column(database.String(10))
    pergunta7 = database.Column(database.String(10))
    pergunta8 = database.Column(database.String(10))



class Usuario(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)

class CentroDoacao(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    usuario = database.Column(database.String, nullable=False)
    email = database.Column(database.String, nullable=False, unique=True)
    senha = database.Column(database.String, nullable=False)


class Centro(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key=True)
    usuario =  database.Column(database.String, nullable=False, unique=True)
    endereco= database.Column(database.String, nullable=False, unique=True)
    email =  database.Column(database.String, nullable=False, unique=True)
    senha =  database.Column(database.String, nullable=False)

from datetime import datetime




class Mensagem(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String(100), nullable=False)
    conteudo = database.Column(database.Text, nullable=False)
    data_criacao = database.Column(database.DateTime, default=datetime.utcnow)

    def _repr_(self):
        return f'<Mensagem {self.id}>'

class PerfilDoadores(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    nome=database.Column(database.String)
    email = database.Column(database.String)
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    usuario = database.relationship('Usuario', backref=database.backref('perfil_doador', uselist=False))
    genero = database.Column(database.String)
    tipo_sanguineo = database.Column(database.String)
    doa_sangue = database.Column(database.Boolean)
    doa_medula = database.Column(database.Boolean)
    doa_leite_materno = database.Column(database.Boolean)
    cep = database.Column(database.String)
    logradouro = database.Column(database.String)
    bairro = database.Column(database.String)
    cidade = database.Column(database.String)
    estado = database.Column(database.String)
    cpf = database.Column(database.String)
    data_nascimento = database.Column(database.String)
    foto = database.Column(database.String)

class PerfilCentro(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    instituicao = database.Column(database.String)
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'), nullable=False)
    usuario = database.relationship('Usuario', backref=database.backref('perfil_centro', uselist=False))
    taxas = database.Column(database.String)
    telefones = database.Column(database.String)
    email = database.Column(database.String)
    cep = database.Column(database.String)
    logradouro = database.Column(database.String)
    bairro = database.Column(database.String)
    cidade = database.Column(database.String)
    estado = database.Column(database.String)
    cnpj = database.Column(database.String)
    foto = database.Column(database.String)

class Estoques_(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    instituicao = database.Column(database.String(100))
    doacao = database.Column(database.String(100))
    tipo = database.Column(database.String(100))
    quantidade = database.Column(database.Integer)


class PostIts(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    conteudo = database.Column(database.String(200))
    cor = database.Column(database.String(20))
    usuario_id = database.Column(database.Integer, database.ForeignKey('usuario.id'))
    usuario = database.relationship('Usuario', backref='postits')
