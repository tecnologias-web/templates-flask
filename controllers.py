from app import app
from flask import render_template


@app.route('/')
def index():
    return render_template(
        'index.html',
        titulo='Título do Contexto',
        lista=['Item 1', 'Item 2', 'Item 3'],
        objeto={
            'nome': 'Yuri',
            'sobrenome': 'Dirickson'
        }
    )


