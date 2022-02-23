import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
import os

# mail server parameters
smtpHost = "smtp.gmail.com"
smtpPort = 587
mailUname = 'seuemail@gmail.com'
mailPwd = 'suasenha'
fromEmail = 'seuemail@gmail.com'

# mail body, recepients, attachment files
mailSubject = "Email automático de Python"
mailContentHtml ="""
<p>Olá, Tudo bem?</p>
<p>Eu sou uma IA programada por LittleJohn
<p>Isso é um <b>teste</b> usando envio de email por comando de voz em um script de python script.
<p>A biblioteca <b>smtplib</b> foi utilizada juntamento com <p>pinwin32</p>
"""
recepientsMailList = ["remetente@gmail.com"]
attachmentFpaths = ["smtp.png", "poster.png"]

def sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail, mailSubject, mailContentHtml, recepientsMailList, attachmentFpaths):
    # create message object
    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = ','.join(recepientsMailList)
    msg['Subject'] = mailSubject
    # msg.attach(MIMEText(mailContentText, 'plain'))
    msg.attach(MIMEText(mailContentHtml, 'html'))

    # create file attachments
    for aPath in attachmentFpaths:
        # check if file exists
        part = MIMEBase('application', "octet-stream")
        part.set_payload(open(aPath, "rb").read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="{0}"'.format(os.path.basename(aPath)))
        msg.attach(part)

    # Send message object as email using smptplib
    s = smtplib.SMTP(smtpHost, smtpPort)
    s.starttls()
    s.login(mailUname, mailPwd)
    msgText = msg.as_string()
    sendErrs = s.sendmail(fromEmail, recepientsMailList, msgText)
    s.quit()

    # check if errors occured and handle them accordingly
    if not len(sendErrs.keys()) == 0:
        raise Exception("Errors occurred while sending email", sendErrs)

sendEmail(smtpHost, smtpPort, mailUname, mailPwd, fromEmail,mailSubject, mailContentHtml, recepientsMailList, attachmentFpaths)

print("execution complete...")
