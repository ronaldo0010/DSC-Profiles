from app import app
from flask import Flask, render_template

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def about():
    path = "static/images/"
    dsc = "https://www.linkedin.com/company/dscuct/"
    ronaldo = "Ronaldo Cedras, is a third year computer science student at Stellenbosch University. Since a young age, he has shown interest in computers and making it do things. I joined DSC on a quest to better myself as a developer and becoming a more well-rounded software engineer. As a tech mentor I hope to help mould students to exactly this. In his free time he watches animated philosophy on YouTube, clicks on heads in Rainbow Six Siege and surfs the internet."

    ls = [
    {
    'name': 'Wavhudi Beckham',
    'photo': path+"Wavhudi.png",
    'intro': "Wavhudi Cornelius Mulaudzi is a second-year Computer Science and Computer Engineering student at the University Of Cape Town. His role at the DSC club is Tech mentor. He is passionate about coding and solving socio-economic problems through the application of Information Technology. He hopes to achieve his dream of becoming a software developer and owning his own Tech company.",
    },
    {
    'name': 'Ryan Cecrest',
    'photo': path+"Ryan.png",
    'intro': "Ryan joined the DSC to become part of a community that supports and encourages the development of ambitious software develops who want to make an impact on the world. He wants to help students to get the most out of there DSC experience while having fun and learning new concepts along the way."
    },
    {
    'name': 'Ronaldo Seegras',
    'photo': path+"Ronaldo.png",
    'git': "https://github.com/ronaldo0010",
    'web': "https://rcedras.herokuapp.com/",
    'role': "Web & Mobile apps",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'lang': "Python, Java, JS, Dart, Html, CSS",
    'intro': ronaldo,

    },
    {
    'name': 'Richard Dawson',
    'photo': path+"Richard.png",
    'git': "https://github.com/ronaldo0010",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'web': "https://rcedras.herokuapp.com/",
    'intro': "Richard makes marketing materials for both print and web, and joined the Google DSC to bring hopeful coders closer to the tech industry. He’s deeply invested in the intersection between technology and business, and has previous experience in the fields of biomedical engineering, higher education, web development and graphic design, and screenwriting",
    },
    {
    'name': 'Nkosi Gates',
    'photo': path+"Nkosi.png",
    'git': "https://github.com/ronaldo0010",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'web': "https://rcedras.herokuapp.com/",
    'intro': "Nkosi is a Part-time student at the University of London majoring in Computer Science : Games Development and a Test Engineer.",
    },
    {
    'name': 'Jonathan De Wet',
    'photo': path+"Jonathan_dk.png",
    'git': "https://github.com/ronaldo0010",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
    'web': "https://rcedras.herokuapp.com/",
    'intro': "Jonathan de Kock is a professional full-stack developer who forms part of the Google DSC as a result of his love for teaching eager minds how to think like programmers, solve real-world challenges by being innovative and how to flourish in the tech industry. He is a self taught developer with a focus on building powerful cross-platform applications for listed companies using web technologies",
    },
    {
    'name': "George Rautenbach",
    'git': "https://github.com/Koellewe",
    'web': "https://rauten.co.za/",
    'photo': path+"George.png",
    'role': "Computer Ethics, DevOps, SysAdmin",
    'lang': "Bash, Go, Python, SQL, PHP",
    'linked': "https://www.linkedin.com/in/jans-rautenbach/",
    'intro': "George is a final year Computer Science & Philosophy student interested in the intersection between these fields. When he isn’t working on personal and collaborative tech projects, he blogs about computer ethics, AI identity, and other philosophical ideas. ",

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
        if 'intro' not in ls[i]:
            ls[i]['intro'] = ' '
        if 'lang' not in ls[i]:
            ls[i]['lang'] = ' '
        ls[i]['mid'] = str(i * 3)

    return render_template('about.html', ls=ls, stop=len(ls))
