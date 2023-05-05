# criação de threads e processos 
'''No script principal.py a seguir, vamos criar uma thread e um processo que executam a mesma função. Na linha 9, criamos uma thread para executar a função funcao_a utilizando a classe thread. O construtor tem como parâmetros a função que deverá ser executada (target) e quais parâmetros serão passados para essa função (args). O parâmetro args espera um iterável (lista, tupla etc.), onde cada elemento será mapeado para um parâmetro da função target.'''

'''Atenção!
Como criar threads e processos em Python:

Vamos utilizar a classe thread e process, dos módulos threading e multiprocessing, respectivamente. Para facilitar a transição entre processos e threads simples, o Python fez os construtores e métodos das duas classes muito parecidos.'''

# script principal.py
from threading import Thread
from multiprocessing import Process

def funcao_a(nome):
    print(nome)

def main():
    t = Thread(target=funcao_a, args=("Minha Thread",))
    t.start()

    p = Process(target=funcao_a, args=("Meu Processo",))
    p.start()

if __name__ == '__main__':
    main()
