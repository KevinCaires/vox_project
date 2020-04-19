from gtts import gTTS
from playsound import playsound
import pygame
from speech_recognition import Recognizer, UnknownValueError, Microphone

def record_audio(audio):
    """
    Função que responde o comando do ususário.
    """
    # Atribui a entrada de aúdio e sua linguagem.
    tts = gTTS(audio, lang='pt-br')
    # Salva a entrada no formato mp3.
    tts.save('audios/audio_input.mp3')

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

        print('Entre com uma fala')

        # Armazena a informação de audio na variável.
        audio = mic_in.listen(source)

        try:
            # Passa o aúdio para o reconhecedor de padrões do google trasformar em frase.
            frase = mic_in.recognize_google(audio, language='pt-BR')
            print(f'Entrada de aúdio: {frase}')
            record_audio(frase)
        except UnknownValueError:
            print('Padão de fala não reconhecido. Tente novamente!')
    return frase

def reponse_audio():
    print('Processando o que me disse ...')
    pygame.init()  # pylint: disable=no-member

    # Carrega o aúdio no mixer.
    pygame.mixer.music.load('audios/audio_input.mp3')
    # seleciona o volume da saída do mixer.
    pygame.mixer.music.set_volume(1)
    # Inicia a saída de aúdio.
    pygame.mixer.music.play()

    # Cria um temporizador.
    clock = pygame.time.Clock()
    # Espera 10 para responder o aúdio.
    clock.tick(10)

    while pygame.mixer.music.get_busy():
        # Inicia um evento para o caso de o mixer estiver ocupado o proxímo retorno aguarde 10 segundos
        pygame.event.poll()
        clock.tick(10)