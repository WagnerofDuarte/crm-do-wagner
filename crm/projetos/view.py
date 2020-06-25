from flask import Blueprint, render_template, request, redirect, url_for
from crm import db
from crm.projetos.models import Projeto
import os

projeto = Blueprint('projeto', __name__, template_folder="templates")

@projeto.route('/', methods=['POST', 'GET'])
def index():

    projetos = Projeto.query.all()
    projetos.sort(key=lambda x: x.data, reverse=False)
    
    if request.method == 'POST' and 'nome' in request.form:
        projetos = Projeto(request.form['nome'], 
                           request.form['tipo'], 
                           request.form['cliente'], 
                           request.form['url'], 
                           request.form['valor'], 
                           request.form['po'], 
                           request.form['prazo'], 
                           request.form['inicio'], 
                           request.form['status'], 
                           request.form['nota'])
        db.session.add(projetos)
        db.session.commit()
        
        return redirect(url_for('projeto.index'))
    
    return render_template('projetos.html', projetos=projetos)

    """if(request.method == 'POST'):
        nome = request.form['pesquisa']
        search = "%{}%".format(nome)
        projetos = Projeto.query.filter(Projeto.nome.like(search)).all()
        for i in projetos:
            print(i.nome)

    return render_template('teste.html', projetos = projetos)"""

@projeto.route('/especifico/<_id>', methods=['GET'])
def especifico(_id):

    projeto = Projeto.query.get_or_404(_id)
    projeto_comentarios = projeto.comentarios.split('|')

    if request.method == 'POST' and 'nomeprojeto' in request.form:
        
        nomenomeprojeto = request.form['nomeprojeto']
        tipo = request.form['tipo']
        cliente = request.form['cliente']
        url = request.form['url']
        valor = request.form['valor']
        po = request.form['po']
        prazo = request.form['prazo']
        inicio = request.form['inicio']
        status = request.form['status']
        nota = request.form['nota']

        projeto.nomeprojeto = nomenomeprojeto
        projeto.tipo = tipo
        projeto.cliente = cliente
        projeto.url = url
        projeto.valor = valor
        projeto.po = po
        projeto.prazo = prazo
        projeto.inicio = inicio
        projeto.status = status
        projeto.nota = nota

        db.session.commit()

        return redirect(url_for('projeto.especifico', _id = projeto.id))
    
    if request.method == 'POST':
        db.session.delete(projeto)
        db.session.commit()
        
        return redirect(url_for('projeto.index'))
    
    return render_template('especifico_projetos.html', projeto = projeto, projeto_comentarios = projeto_comentarios)