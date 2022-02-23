import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# parâmetros do servidor do e-mail
smtpHost = "smtp.gmail.com"
smtpPort = 587
mailUname = 'seuemail@gmail.com'
#Use a senha de App se for o Gmail:
mailPwd = 'suasenha'
fromEmail = 'seuemail@gmail.com'

# corpo do e-mail, destinatários, arquivos anexos
mailSubject = "Escreva seu título"
#Dê uma olhada em html para customizar seu email
mailContentHtml ="<p>Escreva seu email</p>"
#Aqui você adiciona os destinatários
recepientsMailList = ["seuemail@gmail.com"]

def sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail, mailSubject, mailContentHtml, recepientsMailList):
    # Cria o objeto mensagem
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = ','.join(recepientsMailList)
    msg['Subject'] = mailSubject
    # msg.attach(MIMEText(mailContentText, 'plain'))
    msg.attach(MIMEText(mailContentHtml, 'html'))

    # Enviar objeto mensagem como email usando smptplib
    s = smtplib.SMTP(smtpHost, smtpPort)
    s.starttls()
    s.login(mailUname, mailPwd)
    msgText = msg.as_string()
    sendErrs = s.sendmail(fromEmail, recepientsMailList, msgText)
    s.quit()

    # Verificar se ocorreram erros e tratar adequadamente
    if not len(sendErrs.keys()) == 0:
        raise Exception("Ocorreram erros ao enviar e-mail", sendErrs)

sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,mailSubject, mailContentHtml, recepientsMailList)

print("--- Execução Completa ---")
