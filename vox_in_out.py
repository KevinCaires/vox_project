from gtts import gTTS
from loader_recorder import set_command, get_response, get_command_list
from os import path, system
import pygame
from speech_recognition import Recognizer, UnknownValueError, Microphone

COMMAND_LIST = ['ADD', 'LISTAR']

def record_audio(audio):
    """
    Função que responde o comando do ususário.
    """
    # Cria a pasta raiz dos audios caso a mesma não exista
    if not path.exists('audios'):
        system('mkdir audios')

    # Atribui a entrada de aúdio e sua linguagem.
    tts = gTTS(audio, lang='pt-br')
    # Salva a entrada no formato mp3.
    tts.save('audios/audio_response.mp3')

def get_audio():
    """
    Função que resolve a fala do usuário.
    """
    # Função que reconhece a entrada da fala.
    mic_in = Recognizer()
    # Pega a entrada do microfone
    with Microphone() as source:
        # Ajusta a entrada eliminando ruidos.
        mic_in.adjust_for_ambient_noise(source)
        
        # Limpa informações de inicialização do terminal.
        system('clear')
        
        # Mostra na tela os comandos padrões.
        print('Comandos basicos:')
        for info in COMMAND_LIST:
            print(info)

        # Armazena a informação de audio na variável.
        audio = mic_in.listen(source)

        try:
            # Passa o aúdio para o reconhecedor de padrões do google trasformar em frase.
            phrase = mic_in.recognize_google(audio, language='pt-BR')
            print(f'Entrada de aúdio: {phrase}')
            
            # Condição para o caso de o usuário use o comando ADD.
            if str(phrase).upper() == COMMAND_LIST[0]:
                set_command()

                return get_audio()
            
            # Condição para o caso de o usuário use o comando LISTAR.
            if str(phrase).upper() == COMMAND_LIST[1]:
                command_list = [info for info in get_command_list()]

                return command_list

            record_audio(get_response(phrase))
            return reponse_audio()

        except UnknownValueError:
            print('Padrão de fala não reconhecido. Tente novamente!')

def reponse_audio():
    """
    Responde o usuário com o aúdio da resposta.
    """
    # Limpa o terminal.
    system('clear')

    print('Processando o que me disse ...')
    pygame.init()  # pylint: disable=no-member

    # Carrega o aúdio no mixer.
    pygame.mixer.music.load('audios/audio_response.mp3')
    # seleciona o volume da saída do mixer.
    pygame.mixer.music.set_volume(1)
    # Inicia a saída de aúdio.
    pygame.mixer.music.play()

    # Cria um temporizador.
    clock = pygame.time.Clock()

    while pygame.mixer.music.get_busy():
        # Inicia um evento para o caso de o mixer estiver ocupado o proxímo retorno aguarde 10 segundos
        pygame.event.poll()
        clock.tick(10)
