from flask import Blueprint, render_template, request, redirect, url_for
from crm import db
from crm.clientes.models import Cliente
from crm.projetos.models import Projeto
from datetime import *
from sqlalchemy.sql import func

home = Blueprint('home', __name__, template_folder="templates")

@home.route("/index", methods=['GET', 'POST'])
@home.route('/', methods=['GET', 'POST'])
def index():

    clientes = Cliente.query.all()
    if request.method == 'POST' and "nome" in request.form:
        nome = request.form['nome']
        email = request.form['email']
        telefone = request.form['telefone']
        status = request.form['status']
        endereco = request.form['endereco']
        datainsercao = request.form['datainsercao']
        prospeccao = request.form.get('prospeccao')

        clientes = Cliente(nome = nome,
                            email = email,
                            telefone = telefone,
                            status = status,
                            endereco = endereco,
                            datainsercao = datainsercao,
                            prospeccao = prospeccao)

        db.session.add(clientes)
        db.session.commit()

        return redirect(url_for('home.index'))

    projetos = Projeto.query.all()
    projetos.sort(key=lambda x: x.data, reverse=False)
    listadoida = list()
    
    for c in clientes:
        d1 = datetime.today()
        d2 = datetime.strptime(c.datainsercao, '%Y-%m-%d')

        delta = abs((d1 - d2).days)
        
        if delta <= 5:
           listadoida.append(c)

    totprojetos = int(0)
    
    for p in projetos:
        if p.status != "Cancelado":
            totprojetos += 1
        else:
            pass
    
    faturamento = Projeto.query.with_entities(func.sum(Projeto.valor)).all()

    media = Projeto.query.with_entities(func.avg(Projeto.nota)).all()
        
    data = date.today()
    ano = data.strftime('%Y')

    if request.method == 'POST' and "nomeprojeto" in request.form:
        projetos = Projeto(request.form['nomeprojeto'], 
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
        
        
        return redirect(url_for('home.index'))

    

    return render_template('index.html', clientes=clientes, 
                                         projetos=projetos,  
                                         faturamento=faturamento,
                                         media=media,
                                         ano=ano,
                                         totprojetos=totprojetos,
                                         listadoida=listadoida)