import psycopg2
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def select():
    # Connection
    host = ""
    dbname = ""
    user = ""
    password = ""
    sslmode = "allow"


    conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
    conn = psycopg2.connect(conn_string) 
    print("Connection established")

    cursor = conn.cursor()
    cursor.execute("select f.id, f.store_id, f.file from db_file.store_files f where f.client = 'MacDonalds'")
    rows = cursor.fetchall()
    return rows  

def removee(df):
    qtdS = 0
    qtdE = 0
    listaS = []
    listaE = []
    for i in df:
        try:
            os.remove(r'{}'.format(i[2]))
            print(i[2], '>> ARQUIVO APAGADO COM SUCESSO')
            listaS.append(i[2])
            qtdS += 1

        except:
            print(i[2],'<< ERRO - ARQUIVO OU DIRETORIO NÃO ENCONTRADO')
            listaE.append(i[2])
            qtdE += 1
            continue
    return listaS, listaE, qtdS, qtdE


def send_email(frase):
    smtp_server = 'smtp.gmail.com' 
    sender_email = '' 
    recipients = ['mike-william98@hotmail.com']
    password = ''
    port = 587
    
    subject = 'Rotina Apaga Arquivos'
    body = frase
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] =  ', '.join(recipients)
    message['Subject'] = subject 
    mail_content = body
    message.attach(MIMEText(mail_content, 'plain'))

    server = smtplib.SMTP(smtp_server, port)
    server.starttls()
    server.login(sender_email, password)
    text = message.as_string()
    server.sendmail(sender_email, recipients, text)

    return '>> Email sent!'


def main():  
    try:
        df = select() 

        listaS = []
        listaE = []
        listaS, listaE, qtdS , qtdE = removee(df)

        frase = ('''Executada com SUCESSO\n>> ARQUIVOS APAGADOS COM SUCESSO: {}\n<< ERROS - ARQUIVO OU DIRETORIO NÃO ENCONTRADO: {}'''.format(qtdS, qtdE))
        
    except:
        frase = ('Executado com ERRO')

    print(frase)
    send_email(frase)

main()
      
        

