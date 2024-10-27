import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_code(code:str, email:str):
    smtp_server = 'smtp.mail.ru'
    smtp_port = 465  # Для SSL
    username = 'support@danski.ru'
    password = 'a8SBXQqaaXyXbvpzhTq4'
    recipient = email
    subject = 'Код на Python'

    # Убедимся, что code - это строка

    # Создание сообщения
    msg = MIMEMultipart()
    msg['From'] = username
    msg['To'] = recipient
    msg['Subject'] = subject

    # HTML-контент письма
    body = f"""
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ваш код подтверждения</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
                background-color: #f4f4f4;
            }}
            .container {{
                background-color: #ffffff;
                padding: 20px;
                border-radius: 5px;
                box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            }}
            .footer {{
                margin-top: 20px;
                font-size: 12px;
                color: #888888;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Здравствуйте!</h1>
            <p>Ваш код подтверждения: <strong>{code}</strong></p>
            <p>Пожалуйста, используйте этот код для завершения регистрации.</p>
            <p>Если вы не запрашивали этот код, просто проигнорируйте это письмо.</p>
        </div>
        <div class="footer">
            <p>С уважением, <br> Ваша команда.</p>
        </div>
    </body>
    </html>
    """

    msg.attach(MIMEText(body, 'html'))

    # Попытка отправить письмо
    try:
        with smtplib.SMTP_SSL(smtp_server, smtp_port) as server:
            server.login(username, password)
            server.send_message(msg)
        print('Письмо отправлено успешно!')
    except Exception as e:
        print(f'Ошибка: {e}')
