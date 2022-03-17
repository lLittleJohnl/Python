import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from tkinter import *

def ISOC():

    smtpHost = "smtp.gmail.com"
    smtpPort = 587
    from_adress = 'joaovitorpessoa10@gmail.com'
    password = 'bbexyjmecnrbsxpc'
    to_adress = 'joaovitorpessoa10@gmail.com'
    subject = 'Título'
    content ="""
                <p>Prezados</p>
                <p>Segue o exemplo de funcionamento do arquivo.</p>'
            """
    msg = MIMEMultipart()
    msg['From'] = from_adress
    msg['To'] = to_adress
    msg['Subject'] = subject
    body = MIMEText(content, 'html')
    msg.attach(body)
    file_path = "C:\\Users\\joaov\Downloads\\Santa_Ceia.txt"
    file_name = 'Santa_Ceia.txt'
    attachment = open(file_path, 'rb')
    att = MIMEBase('application','octet-stream')
    att.set_payload(attachment.read())
    encoders.encode_base64(att)
    att.add_header('Content-Disposition',f'attachment; filename = {file_name}')
    attachment.close()
    msg.attach(att)
    try: 
        server = smtplib.SMTP(smtpHost, smtpPort)
        server.ehlo()
        server.starttls()
        server.login(from_adress, password)
        server.sendmail(msg['From'], msg['To'], msg.as_string())
    except Exception as e:
        print(e)
    finally:
        server.quit()
    confirmation ='Script executado com sucesso.'
    conf_text['text'] = confirmation

window = Tk()
window.title('Automação - ISOC')
window.geometry('300x100')
alert_text = Label(window, text='O programa será executado após sua confirmação.')
alert_text.grid(column=0, row=0)
button_text = Button(window, text='Executar',command=ISOC)
button_text.grid(column=0, row=1)
conf_text = Label(window, text='')
conf_text.grid(column=0, row=2)
window.mainloop()

# nav = webdriver.Edge(executable_path =r'C:\Users\f8085167\Documents\Python\env\ISOC_Automation\msedgedriver.exe')
# nav.get('https://app.pipefy.com/pipes/301971215')
# time.sleep(10)
# nav.find_element_by_xpath('//*[@id="root"]/div/div/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[3]/div[1]/div/input').send_keys('ggnutzmann@timbrasil.com.br')
# nav.find_element_by_xpath('//*[@id="root"]/div/div/form/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div/div[3]/div[2]/div[1]/div/input').send_keys('Thomas#100')
# nav.find_element_by_xpath('//*[@id="root"]/div/div/form/div/div/div/button/span').click()
# time.sleep(5)
# nav.find_element_by_xpath('//*[@id="sub-header-button-item"]/li/button').click()
# time.sleep(5)
# nav.find_element_by_xpath('//*[@id="pipe_placeholder"]/div[2]/div/div[1]/main/div[2]/div[3]/div/a').click()
# time.sleep(5)
# nav.find_element_by_xpath('//*[@id="pipe_placeholder"]/div[2]/div/div[1]/div[2]/div[1]/div[1]/div[3]/div/div/button').click()
# time.sleep(5)
# nav.find_element_by_xpath('/html/body/div[10]/div/div[2]/footer/button[2]').click()
# time.sleep(10)
# nav.close()
# time.sleep(5)