## Projeto de IHM para entrada de voz e resposta.

### **Observações**:
Esse código foi testado apenas em ambiente `linux`. Não sabemos como ele poderá responder em um ambiente `windows` ou `macos`.

### Linguagem utilizada
`python==3.6.9`

### Como usar:

1 - Crie uma ambiente virtual do python. E.g. `virtualenv` ou `virtualenvwrapper`.

2 - Após estar com o ambiente virtual ativo instale os pacotes necessários que estão dentro de requirements.txt - Você pode fazer isso utilizando o comando make install.

3 - Agora que os pacotes já foram instalados podemos rodar o código no terminal - Você pode fazer isso com o comando make run


### **Problemas comuns:**

Pode haver erros no momento de instalar o pacote pyaudio, pois ele irá depender de outros programas instalados em seu sistema. Solucionei o problema no `StackOverflow`, link https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error.


### **Notas para o professor.**

Ao criar a aplicação foram usados os módulos `gTTS`, `SpeechRecognition` e o `pygame`.

O módulo `SpeechRecognition` foi usado para realizar o reconhecimento da fala e interpretação da mesma pelo programa. Ele recebe uma entrada de aúdio, reconhece o comando e realiza a ação de acordo com a programação utilizada. Maiores informações no link https://pypi.org/project/SpeechRecognition/.

O módulo `gTTS` foi utilizado para realizar a resposta em aúdio. Esse módulo foi criado pela empresa google, com ele nós passamos uma entrada de texto, cuja a qual ele transforma em aúdio para ser reproduzido pelo programa conforme a codificação do mesmo. Maiores informações no link https://pypi.org/project/gTTS/.

O módulo `pygame` foi utilizado para realizar a reprodução da resposta gravada em formato mp3. Apesar de esse módulo se criado para utilização no desenvolvimento de jogos, o mesmo pode ser utilizado em váriados projetos. Mais informações no link https://www.pygame.org/wiki/about/.


### **Como utilizar.**

Quando iniciamos o programa temos dispostos na tela do terminal dois comando padrões do sistema, `ADICIONAR` e `PARAR`.

O comando `ADICIONAR` irá adicionar um novo comando e sua resposta, adiconando ao banco de dados do sistema, banco de dados simples `sqlite3`, que ficara guadado ná máquina enquanto o arquivo permanecer intacto.

O comando `PARAR` irá parar o programa. Você conseguira o mesmo resultado com o comando `ctrl + C`.
