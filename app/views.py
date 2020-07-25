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
    mid = []
    mid_1 = []

    mentors = [

{
    'name': "Nkosilathi Tauro",
    'git': "https://github.com/nkosi-tauro",
    'web': "https://nkositauro.me/",
    'role': "Web, Mobile Apps & Games",
    'lang': "Python, Swift, JavaScript, Java, C#",
    'linked': "https://www.linkedin.com/in/nkosi-tauro/",
    'photo': "https://media-exp1.licdn.com/dms/image/C5603AQGGhtbzhC7rHQ/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=GTAZz1sNGBP9o-UgWZsjhdrmEVWH0ck_oRw-VqMF8cU",
    'intro': 'Nkosi is a Part-time student at the University of London majoring in Computer Science : Games Development and a Test Engineer. I Joined the DSC so that I could be a part of a community of like minded individuals who want to make an impact in their communities, schools through tech.',
},
{
    'name': "George Rautenbach",
    'git': "https://github.com/Koellewe",
    'web': "https://rauten.co.za/",
    'role': "Computer Ethics, DevOps, SysAdmin",
    'lang': "Bash, Go, Python, SQL, PHP",
    'linked': "https://www.linkedin.com/in/jans-rautenbach/",
    'photo':"https://media-exp1.licdn.com/dms/image/C5603AQEHFxW-n9eV3g/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=xGVFAWyL9t_rJBickEE6BzG0cP_ZqXWT2XeDpAAbTzE",
    'intro': 'George is a final year Computer Science & Philosophy student interested in the intersection between these fields. When he isn’t working on personal and collaborative tech projects, he blogs about computer ethics, AI identity, and other philosophical ideas. “The tech industry is desperately lacking in devs that have an understanding for the moral impact of their work. I joined the DSC team to tackle this problem at its root. By being a tech mentor I intend to bring a well-rounded view of IT to those who will shape its future - students.”'
},
{
    'name': "Suvana Rohanlal",
    'git': "https://github.com/Suvana-Rohanlal",
    'role': "Web & Mobile Apps, Embedded Systems",
    'lang': "Java, Python, HTML, CSS, JS,C++",
    'linked': "www.linkedin.com/in/suvana-rohanlal",
    'photo': "https://media-exp1.licdn.com/dms/image/C4D03AQGBfK_IVkjZwQ/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=lgq6GPibLubIjwscuWsoNvCQT_cjE5Q6HwiLBefIJtI",
    'intro': 'Suvana, who is one of our Tech mentors, is a full-time student at the university of Cape Town. She is in her final year of study in Electrical and Computer Engineering. Suvana joined the DSC to put in practice the theory she learnt on campus and to help others. “The community space was filled with exciting people who were eager to take on real problems”. In her spare time Suvana enjoys a good nap, Watching MUFC, learning new coding languages and eating pasta '
,
},

{
    'name': "Nkanyiso Sigwaza",
    'git': "https://github.com/NkanyisoSigwaza",
    'role': "Mobile Apps",
    'lang': "Java, Python, HTML, CSS, JS, C++, Dart, Flutter, SQL",
    'linked': "https://www.linkedin.com/in/nkanyiso-sigwaza-57734a131/",
    'intro': 'Nkanyiso is in the 4th year of his analytics degree. He is part of the club’s tech mentors. He enjoys coding and anything and everything to do with businesses. “I love solving problems. Programming has taught me that there is always a solution to something. You may not have found it yet, but there is always a solution. This is what keeps me motivated when I’m facing a difficult problem. I joined the DSC So that I could be exposed to solving real world problems. I was tired of just solving the ‘problems’ that we were given in class. I want to contribute my time and energy onto projects that will help ease the tasks that people do on a daily basis.” – Nkanyiso ',
},
{
    'name': "Ronaldo Cedras",
    'git': "https://github.com/ronaldo0010",
    'web': "https://rcedras.herokuapp.com/",
    'role': "Web & Mobile apps",
    'lang': "Python, Java, JS, Dart, Html, CSS",
    'intro': 'Ronaldo Cedras, is a third year computer science student at Stellenbosch University. Since a young age, he has shown interest in computers and making it do things. I joined DSC on a quest to better myself as a developer and becoming a more well-rounded software engineer. As a tech mentor I hope to help mould students to exactly this. In his free time he watches animated philosophy on YouTube, clicks on heads in Rainbow Six Siege and surfs the internet.',
    'photo': "https://media-exp1.licdn.com/dms/image/C5603AQETGGYPsRiQ1w/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=lkmMVZGV8blloCMovclR0ZvAKHZeZbhpfiJBPrZrtZk",
    'linked': "https://www.linkedin.com/in/ronaldo-cedras-80b7a9162/",
},
{
    'name': "Londolani Ndou",
    'git': "https://github.com/Londolani",
    'web': "",
    'role': "Tech Mentor",
    'lang': "Python,Java,JavaScript,HTML,CSS,SQL",
    'linked': "https://www.linkedin.com/in/londolani-ndou-504242180/",
    'intro': 'I am a computer science and business computing major at UCT, currently interested in web development. I joined DSC in my first year through attending their great events which led me to want to be part of the events.',
    'photo': "https://media-exp1.licdn.com/dms/image/C4D03AQFcIu-wzfRe0Q/profile-displayphoto-shrink_800_800/0?e=1600905600&v=beta&t=z11S0qvqPrSuTWDz_PM9Zet0bPjsFEFDgBeJgwzyQwM",
},
{
    'name': "Ryan McCarlie",
    'git': "https://github.com/minimac321",
    'web': "",
    'role': "Web & Mobile Apps, Data Analytics",
    'lang': "Java, Python, R, JS, SQL, HTML, CSS",
    'linked': "https://za.linkedin.com/in/ryan-mccarlie-3a1657184",
    'photo': "https://media-exp1.licdn.com/dms/image/C4D03AQHs9Oj3R4m_tA/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=UY4d6AhrwlWGruVeaFZT_-ZIP1A8rV7M51w7bmHZr74",
    'intro': 'Ryan joined the DSC to become part of a community that supports and encourages the development of ambitious software develops who want to make an impact on the world. He wants to help students to get the most out of there DSC experience while having fun and learning new concepts along the way. Ryan is a full-time student at the University of Cape Town who is currently doing his Honours in Computer Science. He aims to complete his Masters in Data Science after that and he hopes to start his own software company one day. In his spare time, he enjoys watching football and is an avid support of Chelsea FC. He enjoys keeping fit by playing social soccer games with his friends.'
},

{
    'name': "Wavhudi Mulaudzi",
    'git': "https://github.com/Corneliusbytecode",
    'web': "www.wavhudimulaudzi.co.za",
    'role': "Tech Mentor",
    'lang': "Python, java, JavaScript, html, CSS,Dart",
    'linked': "https://www.linkedin.com/in/wavhudi-mulaudzi-93975617b",
    'photo': "https://media-exp1.licdn.com/dms/image/C4D03AQERbewM7IthHQ/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=V1aadIcIifI_DdUEOXbRlFuZOzai_7KEVbXrWQsqkrE",
    'intro': 'Wavhudi Cornelius Mulaudzi is a second-year Computer Science and Computer Engineering student at the University Of Cape Town. His role at the DSC club is Tech mentor. He is passionate about coding and solving socio-economic problems through the application of Information Technology. He hopes to achieve his dream of becoming a software developer and owning his own Tech company. “I am very passionate about the field of IT. Ever since from childhood when my brother got me my first desktop computer, I’d sit in front of it for hours just exploring files and folders and the things it can do. That started my love for IT, from that day I knew I will help the world through the application of Information Technology. I spend most of my free time using online resources to learn about web development, mobile application development, software development and business studies. I joined the DSC community because I want to use the knowledge I have so far to contribute in solving socio-economic problems we face today in our communities. I didn’t want to wait until I complete my studies to start contributing to my society, I wanted to start as soon as possible.  As a Tech mentor will help the DSC members identify and solve problems we face today in our community. I am hoping to learn a lot from this opportunity.” – Wavhudi '
},

{
    'name': "Jonathan David de Kock",
    'git': "https://github.com/Alkadian",
    'linked': "https://www.linkedin.com/in/jonathan-de-kock/",
    'role': "Web & Mobile Apps, SysAdmin",
    'lang': "PHP, MySQL, JS, Python, HTML, CSS, Bash, ",
    'web': "https://instagram.com/jonathan_de_kock_?igshid=k4wqnirop6yz",
    'photo': "https://media-exp1.licdn.com/dms/image/C5603AQF6u104_jUk5w/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=0IPd6ToISAw90_BHuTJ5G-fMY9t6RX3v6AW39blNp80",
    'intro' : 'Jonathan de Kock, who is one of our Tech mentors, is a professional full-stack developer who forms part of the Google DSC as a result of his love for teaching eager minds how to think like programmers, solve real-world challenges by being innovative and how to flourish in the tech industry. He is a self taught developer with a focus on building powerful cross-platform applications for listed companies using web technologies. Jonathan has completed several Microsoft approved courses throughout his development career and strives to continue learning new skills and technologies on a daily basis. “The greatest way to make sure that you do not reach a learning-plateau is to learn something new every day”. In his free time, Jonathan enjoys reading about space exploration, keeping fit and dabbling with other forms of programming, such as taking part in game development competitions or programming microcontrollers.'


}

    ]

    admin = [
    {
        'name': "Jonathan Hart",
        'role': "DSC Lead",
        'linked':"https://www.linkedin.com/in/jonohartz/",
        'intro': 'Jonathan is a final year business science student . He joined the club in its inaugural year (2018) and a year later became club lead. He is passionate about business statistics and computer science. "I joined the club because I wanted things to remember my time at UCT by. It’s too easy just to get a degree and only ever interact with people in your year and program. I saw the DSC as a chance to have an impact, and meet awesome people, and get closer to the tech world. It was a chance to build and be part of a special community that I’ll never forget." - Jono',
        'photo': "https://media-exp1.licdn.com/dms/image/C4E03AQEVee0kFydA7w/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=WPitM-OS053tP1KMrIxRt9nJ32GWGO0PpNKx6gVJZbY"
    },
    {
        'name': "Bilqis Deaney",
        'role': "DSC Vice Lead",
        'linked':"https://www.linkedin.com/in/bilqis-deaney-0a0675140/",
        'intro': 'Bilqis Deaney is a tech-enthusiast who holds a post-graduate diploma in educational technology. She is currently pursuing further studies in education. Bilqis joined DSC in 2018 and later became the vice-lead. "The DSC is a collaborative community that links like-minded individuals who want to make a positive difference and have a lasting impact on the world. I joined DSC because of the amazing learning opportunities and the opportunity to engage with diverse individuals. " - Bilqis. In Bilqis\' free time, she enjoys creating short films, photography and practicing Brazilian jiu-jitsu and Kyokushin karate.',
        'photo': "https://media-exp1.licdn.com/dms/image/C4D03AQEtj72Lf6csvQ/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=-tL4wOwJbE-eDXxhWBnG2NAQRsPUHvocRckepT_mUdk"
    },
    {
        'name': "Richard Ferreira",
        'role': "DSC Marketing Lead",
        'linked':"https://www.linkedin.com/in/thisisrichardferreira/",
        'intro': 'Richard, joined the Google DSC to bring hopeful coders closer to the tech industry. He/’s deeply invested in the intersection between technology and business, and has previous experience in the fields of biomedical engineering, higher education, web development and graphic design, and screenwriting. Richard\'s currently working towards an undergraduate degree in Mechanical Engineering at the University of Cape Town, and previously attended the Academy of Digital Arts where he studied web technologies and corporate branding. In his spare time he enjoys running, solving speedcubes, and learning new concepts.',
        'photo': "https://media-exp1.licdn.com/dms/image/C4D03AQEVffD8sd-k6w/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=MFYt2t4QAOe1M4U-ma5BDWxyngaP8eWTEDGNAMMZ0x4"
    },
    {
        'name': "Courtney Williams",
        'role': "DSC Corporate & Social Lead ",
        'linked':"https://www.linkedin.com/in/courtneytaylorwilliams/",
        'intro': '',
        'photo': "https://media-exp1.licdn.com/dms/image/C5103AQEAdd9rgoaoHw/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=9LrLgp7M9SJRmykntBeh67Zf1Bl7fjiJX6ulrIQJSkk"
    },
    {
        'name': "Nkosinathi Ntuli",
        'role': "DSC Technical Lead",
        'linked':"https://www.linkedin.com/in/nkosinathi-ntuli/",
        'intro': 'Nkosinathi (Martin) is a full-time student majoring in Electrical & Computer Engineering and a freelance backend web developer during his spare time. I joined DSC as a member in my first year at UCT. I joined DSC because I wanted to be part of a community in which people learn from each other and grow through sharing knowledge and experience, and that is what DSC UCT is to me.',
        'photo': "https://media-exp1.licdn.com/dms/image/C5603AQEJwC0idCbvGQ/profile-displayphoto-shrink_200_200/0?e=1600905600&v=beta&t=HUMUz4YTxNmy9BtgY3hayF3dTMx_owZubV7HkEjeNFg"
    },

    ]
    # mentors
    for i in range(len(mentors)):
        if 'linked' not in mentors[i]:
            mentors[i]['linked'] = dsc
        if 'web' not in mentors[i]:
            mentors[i]['web'] = None
        if 'git' not in mentors[i]:
            mentors[i]['git'] = None
        if 'role' not in mentors[i]:
            mentors[i]['role'] = "Tech Mentor"
        temp = mid_gen()

        if temp not in mid:
            mentors[i]['mid'] = temp
            mid.append(temp)
        else:
            temp = mid_gen()

    # admin _1
    for i in range(len(admin)):
        temp = mid_gen()

        if temp not in mid_1:
            admin[i]['mid'] = temp
            mid_1.append(temp)

    return render_template('about.html', ls=mentors, stop=len(mentors), ls1=admin, stop1=len(admin))

def mid_gen():
    return str(random.randint(10,500))
