def write_notification(email: str, message=""):
    with open('mensage.txt', mode='a') as email_file:
        conteudo = f'Email: {email} - msg: {message}\n'
        email_file.write(conteudo)