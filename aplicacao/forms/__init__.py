from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,TextAreaField, SubmitField, BooleanField,StringField, RadioField, SelectField,HiddenField, BooleanField, SubmitField
from wtforms.validators import DataRequired, length, email, equal_to
from flask_wtf.file import FileField,FileAllowed

class FormLogin(FlaskForm):
    usuario = StringField('Usuário', validators=[DataRequired(), length(5, 12)], render_kw={"class": "form-control speak-on-hover"})
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 18)], render_kw={"class": "form-control speak-on-hover"})
    lembrar = BooleanField('Lembrar-se')
    submit_entrar = SubmitField('Entrar', render_kw={"class": "speak-on-hover"})


class FormLoginCentro(FlaskForm):
    usuario = StringField('Nome de Usuário', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired()])
    lembrar = BooleanField('Lembrar-se')
    submit_entrar = SubmitField('Entrar')


class MensagemForm(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    conteudo = TextAreaField('Conteúdo', validators=[DataRequired()])
    submit = SubmitField('Enviar')

class FormularioForm(FlaskForm):
    resposta = RadioField('Resposta', choices=[('Sim', 'Sim'), ('Não', 'Não')], validators=[DataRequired()])
    proxima_pergunta = SubmitField('Próxima Pergunta')
    salvar_pdf = SubmitField('Salvar em PDF')


class PerfilDoadoresForm(FlaskForm):
    nome = StringField('Nome Completo', validators=[DataRequired()])
    genero = SelectField('Gênero', choices=[('Masculino', 'Masculino'), ('Feminino', 'Feminino')])
    tipo_sanguineo = SelectField('Tipo Sanguíneo', choices=[('A', 'A'), ('B', 'B'), ('AB', 'AB'), ('O', 'O')])
    doa_sangue = BooleanField('Doa Sangue')
    doa_medula = BooleanField('Doa Medula')
    doa_leite_materno = BooleanField('Doa Leite Materno')
    cep = StringField('CEP', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    logradouro = StringField('Logradouro')
    bairro = StringField('Bairro')
    cidade = StringField('Cidade')
    estado = StringField('Estado')
    cpf = StringField('CPF', validators=[DataRequired()])
    data_nascimento = StringField('Data de Nascimento', validators=[DataRequired()])
    foto = FileField('Foto', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Apenas imagens são permitidas.')])
    submit = SubmitField('Salvar')

class PerfilCentroForm(FlaskForm):

    instituicao = StringField('Instituição', validators=[DataRequired()])
    taxas = StringField('Valor taxas', validators=[DataRequired()])
    telefones = StringField('Telefones', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    cep = StringField('CEP', validators=[DataRequired()])
    logradouro = StringField('Logradouro')
    bairro = StringField('Bairro')
    cidade = StringField('Cidade')
    estado = StringField('Estado')
    cnpj = StringField('CNPJ', validators=[DataRequired()])
    foto = FileField('Foto', validators=[FileAllowed(['jpg', 'jpeg', 'png', 'gif'], 'Apenas imagens são permitidas.')])
    submit = SubmitField('Salvar')




class FormCadastrarUsuario(FlaskForm):
    usuario = StringField('Nome de Usuário', validators=[DataRequired(), length(5, 12)])
    email = StringField('E-mail', validators=[DataRequired(), email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 18)])
    confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), equal_to('senha')])
    submit_criar = SubmitField('Criar')

class FormCadastrarCentro(FlaskForm):
    usuario = StringField('Nome de Usuário', validators=[DataRequired(), length(4, 24)])
    endereco =StringField('Endereco', validators=[DataRequired(), length(4, 24)])
    email = StringField('E-mail', validators=[DataRequired(), email()])
    senha = PasswordField('Senha', validators=[DataRequired(), length(6, 18)])
    confirmacao = PasswordField('Confirmação de Senha', validators=[DataRequired(), equal_to('senha')])
    submit_criar = SubmitField('Criar')