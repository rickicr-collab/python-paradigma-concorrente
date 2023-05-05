import threading
import time

# exemplo de função sem paramentros 
def funcao():
    for i in range(3):
        print(i,'executando a thread')
        time.sleep(1)
print('Iniciando o Programa')
threading.Thread(target=funcao).start()
print('Finalizando o Programa')