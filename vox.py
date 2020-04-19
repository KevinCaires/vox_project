import speech_recognition as sr
from gtts import gTTS
from playsound import playsound

# Função responsável por utilizar fala.
def cria_audio(audio):
	# Especifica a linguagem do aúdio.
	tts = gTTS(audio, lang='pt-br')
	# Salva arquivo de aúdio.
	tts.save('audios/hello.mp3')
	print('Estou aprendendo o que você me disse ...')
	playsound('audios/hello.mp3')


# Função responsável por ouvir e reconhecer a fala.
def ouvir_microfone():
	# Habilita o microfone para ouvir o usuário.
	microfone = sr.Recognizer()
	with sr.Microphone() as source:
		# Chama a função de redução de ruido.
		microfone.adjust_for_ambient_noise(source)
		# Avisa ao usuário que está pronto para ouvir.
		print('Diga algo para mim ...')
		# Armazena a informação de audio na variável.
		audio = microfone.listen(source)

		try:
			# Passa o audio para o reconhecedor de padroes.
			frase = microfone.recognize_google(audio, language='pt-BR')
			# Após alguns segundos, retorna a frase falada.
			print("Você disse: " + frase)
		# Retorna um erro caso não entenda a frase.
		except sr.UnknowValueError:
			print('Não entendi')

	return frase

frase = ouvir_microfone()
cria_audio(frase)
