from werkzeug.utils import secure_filename
import pdfkit

from aplicacao import app, database, bcrypt, login_manager
from flask import send_from_directory,make_response, redirect, render_template, url_for, flash, request, session, get_flashed_messages
from aplicacao.forms import FormLogin, FormCadastrarUsuario,FormCadastrarCentro,\
    PerfilDoadoresForm,FormLoginCentro,FormularioForm,PerfilCentroForm,MensagemForm
from aplicacao.models import Usuario, Estoques_, PostIts,Centro,PerfilDoadores,Formulario,Formulario2,Formulario3,\
    PerfilCentro,Mensagem,TermosUso
from flask_login import login_user, logout_user,login_required
import requests
# import API Mercado Pago
import services
from api_mercadopago import payment
from flask import Flask, render_template, request, redirect
import os
import mercadopago
from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required

import random


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
@app.template_filter('length')
def length_filter(seq):
    return len(seq)
from flask import render_template, request, redirect, url_for


@app.route('/cadastrar_mensagem', methods=['GET', 'POST'])
@login_required
def cadastrar_mensagem():
    form = MensagemForm()
    if request.method == 'POST':
        nome = request.form.get('nome')
        conteudo = request.form.get('conteudo')

        mensagem = Mensagem(nome=nome, conteudo=conteudo)
        database.session.add(mensagem)
        database.session.commit()

        flash('Mensagem cadastrada com sucesso!', 'success')
        return redirect(url_for('exibir_mensagens'))

    return render_template('cadastrar_mensagem.html', form=form)

from flask import redirect, url_for, render_template
from fpdf import FPDF

app.config['PDF_FOLDER'] = '\\aplicacao\\PDF_FOLDER'
import os

# ...

pdf_folder = app.config['PDF_FOLDER']
if not os.path.exists(pdf_folder):
    os.makedirs(pdf_folder)


from fpdf import FPDF

from fpdf import FPDF

from fpdf import FPDF
from flask import render_template, request, redirect, url_for, send_from_directory
from fpdf import FPDF
import os

@app.route('/salvar_formulario3', methods=['POST'])
@login_required
def salvar_formulario3():
    user_id = current_user.id

    pergunta1 = request.form['pergunta1']
    pergunta2 = request.form['pergunta2']
    pergunta3 = request.form['pergunta3']
    pergunta4 = request.form['pergunta4']
    pergunta5 = request.form['pergunta5']
    pergunta6 = request.form['pergunta6']
    pergunta7 = request.form['pergunta7']
    pergunta8 = request.form['pergunta8']
    pergunta9 = request.form['pergunta9']
    pergunta10 = request.form['pergunta10']

    perguntas_html = {
        'pergunta1': 'Foi submetido a transplante de órgãos ou de medula?',
        'pergunta2': 'Apresenta diabetes com complicações vasculares? Faz uso de insulina?',
        'pergunta3': 'Recebeu enxerto de duramater?',
        'pergunta4': 'Já teve algum desses quadros?',
        'pergunta5': 'Apresenta atualmente algum desses quadros?',
        'pergunta6': 'Teve hepatite após os 11 anos de idade?',
        'pergunta7': 'Tem ou teve alguma doença transmissível por sangue?',
        'pergunta8': 'Fez ou faz uso de drogas ilícitas injetáveis?',
        'pergunta9': 'Tem ou teve Malária?',
        'pergunta10': 'Tem ou teve Doença de Parkinson?'
    }

    formulario3 = Formulario3(
        user_id=user_id,
        pergunta1=pergunta1,
        pergunta2=pergunta2,
        pergunta3=pergunta3,
        pergunta4=pergunta4,
        pergunta5=pergunta5,
        pergunta6=pergunta6,
        pergunta7=pergunta7,
        pergunta8=pergunta8,
        pergunta9=pergunta9,
        pergunta10=pergunta10
    )

    database.session.add(formulario3)
    database.session.commit()

    # Criar o PDF
    pdf = FPDF()
    pdf.add_page()

    # Adicionar o conteúdo do formulário ao PDF
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Respostas do Formulário 3', ln=True, align='C')

    pdf.set_font('Arial', '', 12)
    for i in range(1, 11):
        pergunta = perguntas_html[f'pergunta{i}']
        print(pergunta)
        resposta = request.form[f'pergunta{i}']
        print(resposta)
        pdf.cell(0, 10, f'{pergunta}: {resposta}', ln=True)

    # Salvar o PDF no servidor
    pdf_filename = f'formulario3_user_{user_id}.pdf'
    pdf.output(os.path.join(app.config['PDF_FOLDER'], pdf_filename), 'F')

    return redirect(url_for('mostrar_pdf', filename=pdf_filename))


@app.route('/pdf/<filename>')
def mostrar_pdf(filename):
    return send_from_directory(app.config['PDF_FOLDER'], filename, mimetype='application/pdf', as_attachment=False)


@app.route('/pdf')
def pdf():
    user_id = current_user.id
    pdf_filename = f'formulario3_user_{user_id}.pdf'
    return render_template('pdf.html', pdf_filename=pdf_filename)


@app.route('/visualizar_formulario3')
@login_required
def visualizar_formulario3():
    user_id = current_user.id  # Supondo que você tenha um sistema de autenticação e obtenha o ID do usuário atual aqui
    formulario3 = Formulario3.query.filter_by(user_id=user_id).first()
    return render_template('formularioLeite.html', formulario3=formulario3)

@app.route('/salvar_formulario2', methods=['POST'])
@login_required
def salvar_formulario2():
    user_id = current_user.id  # Supondo que você tenha um sistema de autenticação e obtenha o ID do usuário atual aqui

    pergunta1 = request.form['pergunta1']
    pergunta2 = request.form['pergunta2']
    pergunta3 = request.form['pergunta3']
    pergunta4 = request.form['pergunta4']
    pergunta5 = request.form['pergunta5']
    pergunta6 = request.form['pergunta6']
    pergunta7 = request.form['pergunta7']

    perguntas_html = {
        'pergunta1': 'Foi submetido a transplante de órgãos ou de medula?',
        'pergunta2': 'Apresenta diabetes com complicações vasculares? Faz uso de insulina?',
        'pergunta3': 'Recebeu enxerto de duramater?',
        'pergunta4': 'Já teve algum desses quadros?',
        'pergunta5': 'Apresenta atualmente algum desses quadros?',
        'pergunta6': 'Teve hepatite após os 11 anos de idade?',
        'pergunta7': 'Tem ou teve alguma doença transmissível por sangue?',
        'pergunta8': 'Fez ou faz uso de drogas ilícitas injetáveis?',
        'pergunta9': 'Tem ou teve Malária?',
        'pergunta10': 'Tem ou teve Doença de Parkinson?'
    }
    formulario2 = Formulario2(user_id=user_id, pergunta1=pergunta1, pergunta2=pergunta2, pergunta3=pergunta3,
                            pergunta4=pergunta4,
                            pergunta5=pergunta5, pergunta6=pergunta6, pergunta7=pergunta7)

    database.session.add(formulario2)
    database.session.commit()


    # Criar o PDF
    pdf = FPDF()
    pdf.add_page()

    # Adicionar o conteúdo do formulário ao PDF
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Respostas do Formulário 3', ln=True, align='C')

    pdf.set_font('Arial', '', 12)
    for i in range(1, 11):
        pergunta = perguntas_html[f'pergunta{i}']
        print(pergunta)
        resposta = request.form[f'pergunta{i}']
        print(resposta)
        pdf.cell(0, 10, f'{pergunta}: {resposta}', ln=True)

    # Salvar o PDF no servidor
    pdf_filename = f'formulario3_user_{user_id}.pdf'
    pdf.output(os.path.join(app.config['PDF_FOLDER'], pdf_filename), 'F')

    return redirect(url_for('mostrar_pdf', filename=pdf_filename))


@app.route('/salvar_formulario', methods=['POST'])
@login_required
def salvar_formulario():
    user_id = current_user.id  # Supondo que você tenha um sistema de autenticação e obtenha o ID do usuário atual aqui

    pergunta1 = request.form['pergunta1']
    pergunta2 = request.form['pergunta2']
    pergunta3 = request.form['pergunta3']
    pergunta4 = request.form['pergunta4']
    pergunta5 = request.form['pergunta5']
    pergunta6 = request.form['pergunta6']
    pergunta7 = request.form['pergunta7']
    pergunta8 = request.form['pergunta8']
    pergunta9 = request.form['pergunta9']
    pergunta10 = request.form['pergunta10']
    pergunta11 = request.form['pergunta11']

    perguntas_html = {
        'pergunta1': 'Foi submetido a transplante de órgãos ou de medula?',
        'pergunta2': 'Apresenta diabetes com complicações vasculares? Faz uso de insulina?',
        'pergunta3': 'Recebeu enxerto de duramater?',
        'pergunta4': 'Já teve algum desses quadros?',
        'pergunta5': 'Apresenta atualmente algum desses quadros?',
        'pergunta6': 'Teve hepatite após os 11 anos de idade?',
        'pergunta7': 'Tem ou teve alguma doença transmissível por sangue?',
        'pergunta8': 'Fez ou faz uso de drogas ilícitas injetáveis?',
        'pergunta9': 'Tem ou teve Malária?',
        'pergunta10': 'Tem ou teve Doença de Parkinson?'
    }

    formulario = Formulario(user_id=user_id, pergunta1=pergunta1, pergunta2=pergunta2, pergunta3=pergunta3,
                            pergunta4=pergunta4,
                            pergunta5=pergunta5, pergunta6=pergunta6, pergunta7=pergunta7, pergunta8=pergunta8,
                            pergunta9=pergunta9, pergunta10=pergunta10, pergunta11=pergunta11)

    database.session.add(formulario)
    database.session.commit()

    # Criar o PDF
    pdf = FPDF()
    pdf.add_page()

    # Adicionar o conteúdo do formulário ao PDF
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Respostas do Formulário 3', ln=True, align='C')

    pdf.set_font('Arial', '', 12)
    for i in range(1, 11):
        pergunta = perguntas_html[f'pergunta{i}']
        print(pergunta)
        resposta = request.form[f'pergunta{i}']
        print(resposta)
        pdf.cell(0, 10, f'{pergunta}: {resposta}', ln=True)

    # Salvar o PDF no servidor
    pdf_filename = f'formulario3_user_{user_id}.pdf'
    pdf.output(os.path.join(app.config['PDF_FOLDER'], pdf_filename), 'F')

    return redirect(url_for('mostrar_pdf', filename=pdf_filename))


@app.route('/finalizar')
@login_required
def finalizar():
    perfil = PerfilDoadores.query.filter_by(usuario_id=current_user.id).first()
    return render_template('postits.html', perfil=perfil)






@app.route('/visualizar_formulario2')
@login_required
def visualizar_formulario2():
    user_id = current_user.id  # Supondo que você tenha um sistema de autenticação e obtenha o ID do usuário atual aqui

    formulario2 = Formulario2.query.filter_by(user_id=user_id).first()

    return render_template('formularioMedula.html', formulario2=formulario2)


@app.route('/visualizar_formulario')
@login_required
def visualizar_formulario():
    user_id = current_user.id  # Supondo que você tenha um sistema de autenticação e obtenha o ID do usuário atual aqui
    formulario = Formulario.query.filter_by(user_id=user_id).first()
    return render_template('formularioSangue.html', formulario=formulario)


@app.route('/mensagens')
@login_required
def exibir_mensagens():

    mensagens = Mensagem.query.all()
    print(mensagens)
    return render_template('exibir_mensagens.html', mensagens=mensagens)

# Função para consultar o CEP na API ViaCEP e preencher os campos de endereço
def preencher_endereco_por_cep(cep, form):

    url = f"https://viacep.com.br/ws/{cep}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if not data.get("erro"):
            form.logradouro.data = data.get("logradouro", "")
            form.bairro.data = data.get("bairro", "")

            # Dentro da função perfilDoador(), adicione a chamada à função preencher_endereco_por_cep()

@app.route('/perfilDoador', methods=['GET', 'POST'])
@login_required
def perfilDoador():
    # Verificar se o usuário atual já possui um perfil de doador
    perfil_existente = PerfilDoadores.query.filter_by(usuario_id=current_user.id).first()
    if perfil_existente:
        return redirect('/index')
    form = PerfilDoadoresForm()
    if form.validate_on_submit():
        nome = form.nome.data
        genero = form.genero.data
        tipo_sanguineo = form.tipo_sanguineo.data
        doa_sangue = 1 if form.doa_sangue.data else 0
        doa_medula = 1 if form.doa_medula.data else 0
        doa_leite_materno = 1 if form.doa_leite_materno.data and genero == 'Feminino' else 0
        cep = form.cep.data
        email= form.email.data
        logradouro = form.logradouro.data
        bairro = form.bairro.data
        cidade = form.cidade.data
        estado = form.estado.data
        cpf = form.cpf.data
        data_nascimento = form.data_nascimento.data
        foto = form.foto.data

        # Preencher os campos de endereço automaticamente usando o CEP
        preencher_endereco_por_cep(cep, form)

        filename = secure_filename(foto.filename) if foto else 'images/Capturar-fotor-bg-remover-2023061495012.png'
        upload_folder = os.path.join('aplicacao', 'static', 'UPLOAD_FOLDER')

        if foto:
            foto.save(os.path.join(upload_folder, filename))

        perfil = PerfilDoadores(usuario_id=current_user.id, nome=nome, genero=genero, email=email, tipo_sanguineo=tipo_sanguineo,
                                doa_sangue=doa_sangue, doa_medula=doa_medula,
                                doa_leite_materno=doa_leite_materno,
                                cep=cep, logradouro=logradouro, bairro=bairro, cidade=cidade, estado=estado,
                                cpf=cpf, data_nascimento=data_nascimento, foto=filename)

        database.session.add(perfil)
        database.session.commit()

        opcoes_selecionadas = []
        if doa_sangue:
            opcoes_selecionadas.append('sangue')
        if doa_medula:
            opcoes_selecionadas.append('medula')
        if doa_leite_materno:
            opcoes_selecionadas.append('leite')

        paginas_destino = []  # Lista para armazenar as páginas de destino

        for opcao in opcoes_selecionadas:
            if opcao == 'sangue':
                paginas_destino.append('visualizar_formulario')
            elif opcao == 'medula':
                paginas_destino.append('visualizar_formulario2')
            elif opcao == 'leite':
                paginas_destino.append('visualizar_formulario3')

        if paginas_destino:  # Se houver páginas de destino, redirecionar para a próxima
            proxima_pagina = paginas_destino.pop(0)  # Remove a primeira página da lista
            return redirect(url_for(proxima_pagina))

        # Se todas as páginas foram concluídas, redirecionar para index.html
        return redirect('/index')

    return render_template('perfilDoador.html', form=form)




@app.route('/perfilDoador/view/list', methods=['GET'])
@login_required
def viewPerfilDoadorlist():
    perfil = PerfilDoadores.query.all()
    print(perfil)
    return render_template('perfilDoador_view.html', perfil=perfil)

@app.route('/perfilDoador/view', methods=['GET'])
@login_required
def viewPerfilDoador():
    perfil = PerfilDoadores.query.filter_by(usuario_id=current_user.id).first()
    if not perfil:
        return redirect('/perfilDoador')

    return render_template('perfilDoador_view.html', perfil=perfil)

@app.route('/perfilDoador/editar', methods=['GET', 'POST'])
@login_required
def editarPerfilDoador():
    perfil = PerfilDoadores.query.filter_by(usuario_id=current_user.id).first()
    if not perfil:
        return redirect('/perfilDoador')

    form = PerfilDoadoresForm(obj=perfil)
    if form.validate_on_submit():
        form.populate_obj(perfil)
        database.session.commit()
        flash('Perfil atualizado com sucesso!', 'success')
        return redirect('/perfilDoador/view')

    return render_template('perfilDoador_edit.html', form=form)

@app.route('/perfilCentro', methods=['GET', 'POST'])
@login_required
def perfilCentro():
    # Verificar se o usuário atual já possui um perfil de centro
    perfil_existente = PerfilCentro.query.filter_by(usuario_id=current_user.id).first()
    if perfil_existente:
        return redirect('index2')

    form = PerfilCentroForm()
    if form.validate_on_submit():
        instituicao = form.instituicao.data
        taxas = form.taxas.data
        telefones = form.telefones.data
        email = form.email.data
        cep = form.cep.data
        logradouro = form.logradouro.data
        bairro = form.bairro.data
        cidade = form.cidade.data
        estado = form.estado.data
        cnpj = form.cnpj.data
        foto = form.foto.data

        # Preencher os campos de endereço automaticamente usando o CEP
        preencher_endereco_por_cep(cep, form)

        filename = secure_filename(foto.filename)
        upload_folder = os.path.join('aplicacao', 'static', 'UPLOAD_FOLDER')

        foto.save(os.path.join(upload_folder, filename))

        perfil = PerfilCentro(usuario_id=current_user.id, instituicao=instituicao, taxas=taxas,
                              telefones=telefones, email=email, cep=cep, logradouro=logradouro,
                              bairro=bairro, cidade=cidade, estado=estado, cnpj=cnpj, foto=filename)
        print(perfil)
        database.session.add(perfil)
        database.session.commit()

        return redirect('index2')

    return render_template('perfilCentro.html', form=form)

@app.route('/perfilCentro/view', methods=['GET'])
@login_required
def viewPerfilCentro():
    perfil = PerfilCentro.query.filter_by(usuario_id=current_user.id).first()
    if not perfil:
        return redirect('/perfilCentro')

    return render_template('perfilCentro_view.html', perfil=perfil)

@app.route('/perfilCentro/editar', methods=['GET', 'POST'])
@login_required
def editarPerfilCentro():
    perfil = PerfilCentro.query.filter_by(usuario_id=current_user.id).first()
    if not perfil:
        return redirect('/perfilCentro')

    form = PerfilCentroForm(obj=perfil)
    if form.validate_on_submit():
        form.populate_obj(perfil)
        database.session.commit()
        flash('Perfil atualizado com sucesso!', 'success')
        return redirect('/perfilCentro/view')

    return render_template('perfilCentro_edit.html', form=form)

@app.route('/postits', methods=['GET', 'POST'])
@login_required
def postits():
    if request.method == 'POST':
        conteudo = request.form['conteudo']
        cor = random.choice(['yellow', 'pink', 'blue', 'green'])
        postits = PostIts(conteudo=conteudo, cor=cor, usuario_id=current_user.id)
        database.session.add(postits)
        database.session.commit()
        return redirect('/postits')
    else:
        postits = PostIts.query.filter_by(usuario_id=current_user.id).all()
        return render_template('postits.html', postits=postits, current_user=current_user)


@app.route('/postits_exib', methods=['GET', 'POST'])

def postits_exhib():
    if request.method == 'POST':
        conteudo = request.form['conteudo']
        postit = PostIts(conteudo=conteudo,  )
        database.session.add(postit)
        database.session.commit()
        return redirect('/postits')
    else:
        postits = PostIts.query.all()
        return render_template('mural.html', postits=postits)


@app.route('/postits/delete/<int:postit_id>', methods=['POST'])
@login_required
def delete_postit(postit_id):
    postit = PostIts.query.get_or_404(postit_id)
    if postit.usuario_id == current_user.id:
        database.session.delete(postit)
        database.session.commit()
    return redirect('/postits')


from sqlalchemy.exc import SQLAlchemyError


@app.route('/login_doador', methods=['GET', 'POST'])
def loginDoador():
    form = FormLogin()
    if form.validate_on_submit():
        try:
            user = Usuario.query.filter_by(usuario=form.usuario.data).first()
            if user and bcrypt.check_password_hash(user.senha, form.senha.data):
                login_user(user, remember=form.lembrar.data)
                flash(f'Login feito: {form.usuario.data}', 'alert alert-success')
                return redirect('/aceitarTermosCentro')
            else:
                flash('Usuário ou senha incorretos', 'alert alert-danger')
        except SQLAlchemyError as e:
            flash(f'Erro no banco de dados: {str(e)}', 'alert alert-danger')
        except Exception as e:
            flash(f'Ocorreu um erro: {str(e)}', 'alert alert-danger')

    flash_messages = []
    for message in get_flashed_messages():
        flash_messages.append((message, 'alert-danger'))

    return render_template('loginDoador.html', form=form, messages=flash_messages)


@app.route('/login_centro', methods=['GET', 'POST'])
def login_centro():
    form = FormLoginCentro()
    try:
        centro = Centro.query.filter_by(usuario=form.usuario.data).first()
        if centro and bcrypt.check_password_hash(getattr(centro, 'senha'), form.senha.data):
            login_user(centro, remember=form.lembrar.data)
            flash(f'Login feito: {form.usuario.data}', 'alert alert-success')
            return redirect('/aceitarTermosCentro')
        else:
                    flash('Usuário ou senha incorretos', 'alert alert-danger')
    except SQLAlchemyError as e:
        flash(f'Erro no banco de dados: {str(e)}', 'alert alert-danger')
    except Exception as e:
        flash(f'Ocorreu um erro: {str(e)}', 'alert alert-danger')

    flash_messages = []
    for message in get_flashed_messages():
        flash_messages.append((message, 'alert-danger'))

    return render_template('loginCentro.html', form=form, messages=flash_messages)


@app.route('/usuarios', methods=['GET', 'POST'])
def listar_usuarios():
    usuarios = Usuario.query.all()
    return render_template('listar_usuarios.html', usuarios=usuarios)

@app.route('/deletar-usuario/<int:id>', methods=['POST'])
@login_required
def deletar_usuario(id):
    usuario = Usuario.query.get_or_404(id)
    database.session.delete(usuario)
    database.session.commit()
    flash('Usuário deletado com sucesso', 'alert alert-success')
    return redirect('/usuarios')

from sqlalchemy.exc import SQLAlchemyError

# ...

@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
def cadastrar_usuario():
    form = FormCadastrarUsuario()
    if form.validate_on_submit():
        try:
            senha_crypto = bcrypt.generate_password_hash(form.senha.data, rounds=16)
            user = Usuario(usuario=form.usuario.data, email=form.email.data, senha=senha_crypto)
            database.session.add(user)
            database.session.commit()
            flash('Usuário cadastrado com sucesso', 'alert alert-success')
            return redirect('/cadastrar_usuario')
        except SQLAlchemyError as e:
            database.session.rollback()
            flash('Ocorreu um erro ao cadastrar a instituição', 'alert alert-danger')
            print(str(e))
            return render_template('cadastrar_usuario.html', form=form)

    flash_messages = []
    for message in get_flashed_messages():
        flash_messages.append((message, 'alert-danger'))

    return render_template('cadastrar_usuario.html', form=form, messages=flash_messages)


@app.route('/cadastrar_centro', methods=['GET', 'POST'])
def cadastrar_centro():
    form = FormCadastrarCentro()
    if form.validate_on_submit():
        try:
            senha_crypto = bcrypt.generate_password_hash(form.senha.data, rounds=16)
            user = Centro(usuario=form.usuario.data, email=form.email.data, endereco=form.endereco.data, senha=senha_crypto)
            database.session.add(user)
            database.session.commit()
            flash('Instituição cadastrada com sucesso', 'alert alert-success')
            return redirect('/cadastrar_centro')
        except SQLAlchemyError as e:
            database.session.rollback()
            flash('Ocorreu um erro ao cadastrar a instituição', 'alert alert-danger')
            print(str(e))
            return render_template('cadastroCentro.html', form=form, message=flash)

        flash_messages = []
        for message in get_flashed_messages():
            flash_messages.append((message, 'alert-danger'))

    return render_template('cadastroCentro.html', form=form, message=flash)


@app.route("/")
def home():
    return render_template('home.html')

@app.route("/termos")
def termos():
    return render_template('termos.html')


from flask_login import current_user



@app.route('/aceitar_termos', methods=['GET', 'POST'])
def aceitarTermos():
    if current_user.is_authenticated:  # Verifica se o usuário está autenticado
        user = current_user  # Obtém o usuário atual
        termos_uso = TermosUso.query.filter_by(user_id=user.id).first()
        if termos_uso:
            return redirect(url_for('perfilDoador'))
        if request.method == 'POST':
            termos_uso = TermosUso(user_id=user.id, aceito=True)
            database.session.add(termos_uso)
            database.session.commit()
            flash('Termos de uso aceitos com sucesso!', 'alert alert-success')
            return redirect(url_for('perfilDoador'))
        else:
            return render_template('termodoador.html')
    else:
        flash('Você precisa estar logado para aceitar os termos de uso.', 'alert alert-danger')
        return redirect(url_for('loginDoador'))

@app.route('/aceitarTermosCentro', methods=['GET', 'POST'])
def aceitarTermosCentro():
    if current_user.is_authenticated:  # Verifica se o usuário está autenticado
        user = current_user  # Obtém o usuário atual
        termos_uso = TermosUso.query.filter_by(user_id=user.id).first()
        if termos_uso:
            return redirect(url_for('perfilCentro'))
        if request.method == 'POST':
            termos_uso = TermosUso(user_id=user.id, aceito=True)
            database.session.add(termos_uso)
            database.session.commit()
            flash('Termos de uso aceitos com sucesso!', 'alert alert-success')
            return redirect(url_for('perfilCentro'))
        else:
            return render_template('termocentro.html')
    else:
        flash('Você precisa estar logado para aceitar os termos de uso.', 'alert alert-danger')
        return redirect(url_for('loginCentro'))


@app.route("/termo_doador")
def termoDoador():
    return render_template('termodoador.html')

@app.route("/termo_centro")
def termoCentro():
    return render_template('termocentro.html')
@app.route("/index")
def index():
    perfil = PerfilDoadores.query.filter_by(usuario_id=current_user.id).first()

    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios, perfil=perfil)

@app.route("/index2")
def index2():
    perfil = PerfilCentro.query.filter_by(usuario_id=current_user.id).first()

    usuarios = Usuario.query.all()
    return render_template('index2.html', usuarios=usuarios, perfil=perfil)


@app.route("/planos")
def planos():
    return render_template('planoscentro.html')


# API Mercado Pago
@app.route('/buy/<int:id_product>')
def buy_product(id_product):
    product = services.get_product_id(id_product)
    return redirect(payment(request, product=product))

@app.route("/assign")
def assign():
    products = services.get_products()
    return render_template('products.html', products=products)
# Fim API



@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Sessão encerrada', 'alert alert-info')
    return redirect(url_for('loginDoador'))


@app.route('/cadastro_doacao', methods=['GET', 'POST'])
def cadastro_doacao():
    if request.method == 'POST':
        instituicao = request.form['instituicao']
        tipo = request.form['tipo']
        quantidade = int(request.form['quantidade'])
        doacao = request.form['doacao']
        estoques = Estoques_(instituicao=instituicao,doacao=doacao, tipo=tipo, quantidade=quantidade)
        database.session.add(estoques)
        database.session.commit()
        return render_template('cadastro.html', sucesso=True)
    else:
        return render_template('cadastro.html', sucesso=False)


@app.route('/remocao', methods=['GET', 'POST'])
def remocao():
    if request.method == 'POST':
        instituicao = request.form['instituicao']
        doacao = request.form['doacao']
        tipo = request.form['tipo']
        estoques = Estoques_.query.filter_by(instituicao=instituicao,doacao=doacao,tipo=tipo).first()
        if estoques:
            database.session.delete(estoques)
            database.session.commit()
            return render_template('remocao.html', sucesso=True)
        else:
            return render_template('remocao.html', sucesso=False)
    else:
        return render_template('remocao.html', sucesso=None)


@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        instituicao = request.form['instituicao']
        doacao = request.form['doacao']
        quantidade = int(request.form['quantidade'])
        tipo= request.form['tipo']
        estoques = Estoques_(instituicao=instituicao,doacao=doacao, tipo=tipo, quantidade=quantidade)
        if estoques:
            estoques.quantidade += quantidade
            database.session.commit()
            return render_template('adicionar.html', sucesso=True)
        else:
            return render_template('adicionar.html', sucesso=False)
    else:
        return render_template('adicionar.html', sucesso=None)


@app.route('/subtrair', methods=['GET', 'POST'])
def subtrair():
    if request.method == 'POST':
        instituicao = request.form['instituicao']
        quantidade = int(request.form['quantidade'])
        tipo = request.form['tipo']
        doacao = request.form['doacao']
        estoques = Estoques_(instituicao=instituicao, doacao=doacao, tipo=tipo, quantidade=quantidade)
        if estoques:
            if estoques.quantidade >= quantidade:
                estoques.quantidade -= quantidade
                database.session.commit()
                return render_template('subtrair.html', sucesso=True)
            else:
                return render_template('subtrair.html', sucesso=False)
        else:
            return render_template('subtrair.html', sucesso=None)
    else:
        return render_template('subtrair.html', sucesso=None)


@app.route('/atualizacao', methods=['GET', 'POST'])
def atualizacao():
    if request.method == 'POST':
        instituicao = request.form['instituicao']
        tipo = request.form['tipo']
        nova_quantidade = int(request.form['quantidade'])
        doacao = request.form['doacao']

        estoques = Estoques_.query.filter_by(instituicao=instituicao, doacao=doacao, tipo=tipo).first()

        if estoques:
            estoques.quantidade = nova_quantidade
            database.session.commit()
            return render_template('atualizacao.html', sucesso=True)
        else:
            return render_template('atualizacao.html', sucesso=False)
    else:
        return render_template('atualizacao.html', sucesso=None)

@app.route('/lista_produtos')
def listarP():
    estoques = Estoques_.query.all()
    return render_template('lista_produtos.html', estoques=estoques)

@app.route('/gerencia_estoq')
def gerencia_p():
    estoques = Estoques_.query.all()
    return render_template('gerenciar_estoque.html', estoques=estoques)


@app.route('/formularios')
def formularios():
    return render_template('formularios.html')

