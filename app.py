import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flask import Flask, request, jsonify
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)


@app.route('/PROFILE_DATA', methods=['GET'])
def profile_data_fn():
    if request.method == 'GET':
        profile_data = [
            {'id': 1, 'profilePicture': 'https://github.com/guilxp.png'},
            {'id': 2, 'name': 'Guilherme Pantoja'},
            {'id': 3,
             'tagline': 'A dedicated technology professional, passionate about development and driven by a thirst for knowledge.'},
            {'id': 4, 'jobTitle': 'Oracle Cloud Consultant'},
            {'id': 5, 'location': 'Araucária, Paraná - Brazil'},
            {'id': 6, 'yearsOfExperience': 3},
            {'id': 7,
             'skills': ["React.js", "Next.js", "TypeScript", "Tailwind CSS", "PHP", "Golang", "PL/SQL", "RESTful APIs",
                        "Git"]},
            {'id': 8, 'email': 'guilherme.pantoja1201@gmail.com'},
            {'id': 9, 'phone': '+55 41 98771-7929'},
            {'id': 10, 'website': 'https://github.com/guilxp'}
        ]
        return jsonify({'profile_data': profile_data})


@app.route('/SKILLS_DATA', methods=['GET'])
def skills_data_fn():
    if request.method == 'GET':
        skills_data = [
            {'id': 1, 'icon': 'IoLogoJavaScript', 'title': 'JavaScript',
             'comment': 'I started my programming journey with JavaScript, developing tools such as CSV to JSON converters and deepening my knowledge of frameworks, solidifying my foundation for more complex projects.'},
            {'id': 2, 'icon': 'SiNextdotjs', 'title': 'Next.js',
             'comment': 'Experience with Next.js in projects such as interactive dashboards, integrated with Progress4GL for real-time visualization of inventory, shipping, and sales data.'},
            {'id': 3, 'icon': 'RiTailwindCssFill', 'title': 'Tailwind CSS',
             'comment': 'Tailwind CSS has revolutionized my approach to front-end styling. Its utility-first methodology empowers me to rapidly create responsive and visually appealing interfaces without the need for custom CSS.'},
            {'id': 4, 'icon': 'FaGolang', 'title': 'Go',
             'comment': 'I have experience with Go in a personal project involving the development of a real-time chat system API using React.js. The application enables the creation of instant messaging rooms, reactions, marking messages as read, and access to conversation history. Utilizing WebSockets, it offers real-time notifications and functionalities for creating, searching, and deleting rooms. The architecture is based on Go, with Go-chi for routing, Postgres as the database, and WebSockets for communication, serving as a foundation for interactive platforms.'},
            {'id': 5, 'icon': 'BsFiletypeSql', 'title': 'PL/SQL',
             'comment': '"The majority of my experience lies in SQL, where I have developed numerous projects, both personal and professional. I have primarily worked with Oracle Cloud, creating critical reports for finance, inventory, and HCM modules.'},
            {'id': 6, 'icon': 'IoLogoPython', 'title': 'Python',
             'comment': 'I have experience with Python, including the development of academic CRUD systems and APIs. Notably, the backend of this website was built using Python and Flask.'},
            {'id': 7, 'icon': 'SiOracle', 'title': 'Oracle Visual Builder',
             'comment': 'Oracle Visual Builder is a development platform tailored for Oracle Cloud, seamlessly integrating with Oracle APIs and systems, such as finance, inventory, and HCM modules. It enables the development and customization of user interfaces, as well as the automation of workflows, without the need for extensive coding, facilitating rapid solution development for both developers and business professionals.'},
            {'id': 8, 'icon': 'SiOracle', 'title': 'Oracle BI Publisher',
             'comment': 'I have been involved in numerous projects where I developed data analysis reports using BI tools such as SQL, PL/SQL, Oracle Databases, and Oracle Developer Suite for query creation. For data visualization, I utilized Oracle BI Publisher. Additionally, I have worked on modules within Oracle Cloud Applications, including ERP, Finance, HCM, EPM, GL, INV, AR, and AP.'},
            {'id': 9, 'icon': 'SiOracle', 'title': 'Oracle Integration Cloud',
             'comment': '"I have been involved in numerous projects focused on developing system integrations using Oracle Integration Cloud. My experience includes working with a variety of technologies, such as RESTful APIs, SOAP, and XAML, to connect disparate systems and automate business processes.'}
        ]
        return jsonify({'skills_data': skills_data})


@app.route('/EXPERIENCE_DATA', methods=['GET'])
def experience_data_fn():
    if request.method == 'GET':
        experience_data = [
            {'id': 1, 'company': 'Peloton Consulting Group', 'position': 'Oracle Cloud Developer Consultant',
             'duration': '2023 - Present',
             'description': 'I participated in various projects where I developed data analysis reports in BI, using tools such as SQL, PL/SQL, Oracle Databases, and Oracle Developer Suite to create queries. For data visualization, I used Oracle BI Publisher, OTBI, Excel, and Oracle E-Business Suite Applications. I worked on modules of Oracle Cloud Applications, including ERP, Financials, HCM, EPM, GL, INV, AR, and AP. Additionally, I was involved in projects for developing system integrations with Oracle Integration Cloud, using tools such as RESTful APIs, SOAP, XAML, among others.'},
            {'id': 2, 'company': 'Gelopar Refrigeração Paranaense LTDA', 'position': 'IT Assistant',
             'duration': '2022 - 2023',
             'description': 'I optimized programs using PROGRESS 4GL (TOTVS DATASUL) and developed dynamic dashboards with React.js/Next.js, Tailwind CSS, and Styled Components for data visualization. I also implemented interactive animations, flexible data handling, and sliders. I contributed to the intranet development with PHP and SQL, creating and maintaining features like news modules and a calendar. Additionally, I implemented automation flows to improve processes, provided technical support, and worked with agile methodologies like Scrum and Kanban, along with Git and pipeline configuration.'},
            {'id': 3, 'company': 'Gelopar Refrigeração Paranaense LTDA', 'position': 'Administrative Assistant',
             'duration': '2021 - 2022',
             'description': 'Verify invoices against specifications, maintain accurate records in the TOTVS DATASUL ERP system, and manage inter-warehouse transfers. Record all transactions, collaborate with departments to ensure updated records, and promptly address issues for swift resolution.'}
        ]
        return jsonify({'experience_data': experience_data})


@app.route('/ABOUT_ME_DATA', methods=['GET'])
def about_data_fn():
    about_data = [
        {'id': 1,
         'introduction': "Hi, I'm Guilherme Pantoja, an Oracle Consultant with experience in React JS, passionate about creating engaging web applications and solving complex problems through code.",
         'background': "I'm pursuing a degree in Software Analysis and Development. With over 2 years of experience in the development field, I have honed skills in data integration, development including web and backend, data visualization, and data modeling.",
         'skills': "I'm proficient in a variety of technologies including React.js, Next.js, JavaScript, Python, Go, and PL/SQL. I'm also experienced in version control and developing Android applications using Kotlin and React Native.",
         'projects': "Some of my notable projects include a dynamic dashboard built with Next.js and Progress 4GL, a company intranet where key users could update data in real-time, a website for my youth church community where users can create rooms and post questions that can be reacted to and answered, built with React.js and Go, and various projects using Oracle Integration technologies within client environments.",
         'interests': "Outside of coding, I enjoy traveling to new places with my family, playing the piano and guitar, and watching good movies.",
         'careerGoals': "In the future, I am committed to continuously refining my skills as a developer, embracing new technologies, and contributing to impactful projects that enrich people's lives in meaningful ways.",
         'stats': {'yearsOfExperience': '2+', 'numberOfProjects': 11, 'certificationsEarned': 7}}
    ]
    return jsonify({'about_data': about_data})


@app.route('/CONTACT_DATA', methods=['GET'])
def contact_data_fn():
    contact_data = [
        {'id': 1,
         'email': 'guilherme.pantoja1201@gmail.com',
         'phone': '+55 41 98771 7929',
         'website': 'https://www.github.com/guilxp'
         }
    ]
    return jsonify({'contact_data': contact_data})


@app.route('/send-email', methods=['POST'])
def send_email():
    try:
        data = request.json
        fullname = data.get('fullname')
        sender_email = data.get('email')
        message_content = data.get('message')

        smtp_server = os.getenv('SMTP_SERVER')
        smtp_port = os.getenv('SMTP_PORT')
        smtp_user = os.getenv('SMTP_USER')
        smtp_password = os.getenv('SMTP_PASSWORD')
        recipient_email = os.getenv('EMAIL_DESTINO')

        msg = MIMEMultipart()
        msg['From'] = f"{fullname} <{sender_email}>"
        msg['To'] = recipient_email
        msg['Subject'] = f'Mensagem de {fullname}'

        body = f"Mensagem do {fullname} (Email: {sender_email})\n\n{message_content}"
        msg.attach(MIMEText(body, 'plain'))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_password)
            server.send_message(msg)

        return jsonify({'message': 'Email enviado com sucesso!'}), 200

    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({'error': 'Falha ao enviar o email.'}), 500


if __name__ == '__main__':
    app.run(debug=True)
