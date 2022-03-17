import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders

# SMTP - Simple Mail Transfer Protocol
# parâmetros do servidor do e-mail
smtpHost:str = "smtp.gmail.com"
smtpPort:int = 587
server = smtplib.SMTP(smtpHost, smtpPort)
# TLS = Transport Layer Security
server.ehlo()
server.starttls()
from_adress = 'joaovitorpessoa10@gmail.com'
password = ''
server.login(from_adress, password)

# parâmetros do email
to_adress = 'joaovitorpessoa10@gmail.com'
subject = 'Documento - Demandas ISOC'
content ="""
            <p>Prezados</p>
            <p>Segue em anexo documentação conforme acordado.</p>'
         """

msg = MIMEMultipart()
msg['From'] = from_adress
msg['To'] = to_adress
msg['Subject'] = subject
body = MIMEText(content, 'html')
msg.attach(body)

# O anexo é enviado de forma binária
file_path = "path_do_arquivo"
file_name = 'nome_do_arquivo.extensão'

# RB = Read Binary 
attachment = open(file_path, 'rb')
# Lendo o arquivo em RB e codificando em base 64
att = MIMEBase('application','octet-stream')
att.set_payload(attachment.read())
encoders.encode_base64(att)
# Cabeçalho
att.add_header('Content-Disposition',f'attachment; filename = {file_name}')
attachment.close()
msg.attach(att)
server.sendmail(msg['From'], msg['To'], msg.as_string())
server.quit()
print("MISSION COMPLETE!")