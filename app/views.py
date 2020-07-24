from app import app
from flask import Flask, render_template
import random

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/team')
def about():
    path = "static/images/"
    dsc = "https://www.linkedin.com/company/dscuct/"
    ronaldo = "Ronaldo Cedras, is a third year computer science student at Stellenbosch University. Since a young age, he has shown interest in computers and making it do things. I joined DSC on a quest to better myself as a developer and becoming a more well-rounded software engineer. As a tech mentor I hope to help mould students to exactly this. In his free time he watches animated philosophy on YouTube, clicks on heads in Rainbow Six Siege and surfs the internet."
    suvana = "Suvana, who is one of our Tech mentors, is a full-time student at the university of Cape Town. She is in her final year of study in Electrical and Computer Engineering. Suvana joined the DSC to put in practice the theory she learnt on campus and to help others. “The community space was filled with exciting people who were eager to take on real problems”"

    ls = [

{
    'name': "Nkosilathi Tauro",
    'git': "https://github.com/nkosi-tauro",
    'web': "https://nkositauro.me/",
    'role': "Web, Mobile Apps & Games",
    'lang': "Python, Swift, JavaScript, Java, C#",
    'linked': "https://www.linkedin.com/in/nkosi-tauro/",
    'photo': "https://media-exp1.licdn.com/dms/image/C5603AQGGhtbzhC7rHQ/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=GTAZz1sNGBP9o-UgWZsjhdrmEVWH0ck_oRw-VqMF8cU",
    'intro': suvana,
},
{
    'name': "George Rautenbach",
    'git': "https://github.com/Koellewe",
    'web': "https://rauten.co.za/",
    'role': "Computer Ethics, DevOps, SysAdmin",
    'lang': "Bash, Go, Python, SQL, PHP",
    'linked': "https://www.linkedin.com/in/jans-rautenbach/",
    'photo':"https://media-exp1.licdn.com/dms/image/C5603AQEHFxW-n9eV3g/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=xGVFAWyL9t_rJBickEE6BzG0cP_ZqXWT2XeDpAAbTzE",
    'intro': ronaldo,
},
{
    'name': "Suvana Rohanlal",
    'git': "https://github.com/Suvana-Rohanlal",
    'role': "Web & Mobile Apps, Embedded Systems",
    'lang': "Java, Python, HTML, CSS, JS,C++",
    'linked': "www.linkedin.com/in/suvana-rohanlal",
    'photo':"https://media-exp1.licdn.com/dms/image/C4D03AQGBfK_IVkjZwQ/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=lgq6GPibLubIjwscuWsoNvCQT_cjE5Q6HwiLBefIJtI",
    'intro': suvana,
},

{
    'name': "Nkanyiso Sigwaza",
    'git': "https://github.com/NkanyisoSigwaza",
    'role': "Mobile Apps",
    'lang': "Java, Python, HTML, CSS, JS, C++, Dart, Flutter, SQL",
    'linked': "https://www.linkedin.com/in/nkanyiso-sigwaza-57734a131/",
    'intro': suvana,
},
{
    'name': "Ronaldo Cedras",
    'git': "https://github.com/ronaldo0010",
    'web': "https://rcedras.herokuapp.com/",
    'role': "Web & Mobile apps",
    'lang': "Python, Java, JS, Dart, Html, CSS",
    'intro': ronaldo,
    'photo':"https://media-exp1.licdn.com/dms/image/C5603AQETGGYPsRiQ1w/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=lkmMVZGV8blloCMovclR0ZvAKHZeZbhpfiJBPrZrtZk",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
},



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

        ls[i]['mid'] = mid_gen()

    return render_template('about.html', ls=ls, stop=len(ls))

def mid_gen():
    return str(random.randint(10,500))
