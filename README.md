## Projeto de IHM para entrada de voz e resposta.

### **Observações**:
Esse código foi testado apenas em ambiente linux. Não sabemos como ele poderá responder em um ambiente windows ou macos.

### Linguagem utilizada
python==3.6.9

### Como usar:
1 - Crie uma ambiente virtual do python. E.g. _virtualenv_ ou _virtualenvwrapper_.

2 - Após estar com o ambiente virtual ativo instale os pacotes necessários que estão dentro de _requirements.txt_ - Você pode fazer isso utilizando o comando _make install_.

3 - Agora que os pacotes já foram instalados podemos rodar o código no terminal - Você pode fazer isso com o comando _make run_

### **Problemas comuns:**
Pode haver erros no momento de instalar o pacote pyaudio, pois ele irá depender de outros programas instalados em seu sistema. Solucionei o problema no stackoverflow(https://stackoverflow.com/questions/20023131/cannot-install-pyaudio-gcc-error).
