import threading
import time

#exemplo de função com parametros
def funcao(mensagem):
    for i in range(3):
        print(i, mensagem)
        time.sleep(1)
        
print('Iniciando Programa')
x = threading.Thread(target=funcao, args=('Executando!',))
x.start()
print('finalizando o Programa')
                     