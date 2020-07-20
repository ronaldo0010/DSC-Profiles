from app import app
from flask import Flask, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def about():
    pht = "static/images/"
    dsc = "https://www.linkedin.com/company/dscuct/"

    ls = [
    {
    'name': 'Wavhudi',
    'photo': pht+"Wavhudi.jpg",
    },
    {
    'name': 'Ryan',
    'photo': pht+"Ryan.jpg",
    },
    {
    'name': 'Ronaldo',
    'photo': pht+"Ronaldo.png",
    'git': "https://github.com/ronaldo0010",
    'web': "https://rcedras.herokuapp.com/",
    'role': "all-round memer",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",

    },
    {
    'name': 'Richard',
    'photo': pht+"Richard.jpg",
    'git': "https://github.com/ronaldo0010",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'web': "https://rcedras.herokuapp.com/"
    },
    {
    'name': 'Nkosi',
    'photo': pht+"Nkosi.png",
    'git': "https://github.com/ronaldo0010",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'web': "https://rcedras.herokuapp.com/"
    },
    {
    'name': 'Jonathan DK',
    'photo': pht+"Jonathan_dk.jpg",
    'git': "https://github.com/ronaldo0010",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'web': "https://rcedras.herokuapp.com/"
    },
    {
    'name': 'George',
    'photo': pht+"George.jpg",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    }
    ]
    for i in range(len(ls)):
        if 'linked' not in ls[i]:
            ls[i]['linked'] = dsc
        if 'web' not in ls[i]:
            ls[i]['web'] = None
        if 'git' not in ls[i]:
            ls[i]['git'] = None

    return render_template('about.html', ls=ls, stop=len(ls))
