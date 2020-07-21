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
    'name': 'Wavhudi temp-sur',
    'photo': pht+"Wavhudi.png",
    },
    {
    'name': 'Ryan temp-sur',
    'photo': pht+"Ryan.png",
    },
    {
    'name': 'Ronaldo temp-sur',
    'photo': pht+"Ronaldo.png",
    'git': "https://github.com/ronaldo0010",
    'web': "https://rcedras.herokuapp.com/",
    'role': "all-round memer",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",

    },
    {
    'name': 'Richard temp-sur',
    'photo': pht+"Richard.png",
    'git': "https://github.com/ronaldo0010",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'web': "https://rcedras.herokuapp.com/"
    },
    {
    'name': 'Nkosi temp-sur',
    'photo': pht+"Nkosi.png",
    'git': "https://github.com/ronaldo0010",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'web': "https://rcedras.herokuapp.com/"
    },
    {
    'name': 'Jonathan temp-sur',
    'photo': pht+"Jonathan_dk.png",
    'git': "https://github.com/ronaldo0010",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'web': "https://rcedras.herokuapp.com/"
    },
    {
    'name': 'George temp-sur',
    'photo': pht+"George.png",
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
        if 'role' not in ls[i]:
            ls[i]['role'] = "Tech Mentor"

    return render_template('about.html', ls=ls, stop=len(ls))
