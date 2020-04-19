from os import path, system
from speech_recognition import Recognizer, UnknownValueError, Microphone
import sqlite3

DB_PATH = 'database/all_commands.db'

# Caso não exista o cominho e arquivo de banco de dados ele cria.
if not path.exists(DB_PATH):
    # Caso não exista a pasta onde fica o DB o programa cria.
    if not path.exists('database'):
        system('mkdir database')
    
    # Cria e conecta ao DB.
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    # Cria a tabela e as colunas de comandos e respostas
    cur.execute('''
        CREATE TABLE commands_and_responses
        (commands, responses)
    ''')
    # Commita a criação a cima.
    conn.commit()
    conn.close()

def sql_insert(command, response):
    """
    Insere um novo comando e sua resposta no DB.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        '''
        INSERT INTO commands_and_responses VALUES ('%s', '%s')
        ''' % (str(command).upper(), str(response).upper())
    )
    conn.commit()
    conn.close()

def set_command():
    """
    Resolve o comando e a resposta passada pelo usuário, para ser salvo no DB.
    """
    command = input('''
    Escreva um comando que não seja muito complexo.
    O comando deve obedecer as normas da lingua portuguesa(BR).

    ''')

    response = input('''
    Escreva uma resposta não muito longa.
    A resposta deve obedecer as normas da lingua portuguesa(BR).
    
    ''')
    sql_insert(command, response)

def get_response(command):
    """
    Consulta o comando no DB e retorna a reposta salva.
    """
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.execute(
        '''
        SELECT responses FROM commands_and_responses WHERE commands = '%s'
        ''' % str(command).upper()
    )
    response = cur.fetchone()
    return str(response)
