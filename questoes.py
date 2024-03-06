"""Questões:

1) Observe o trecho de código abaixo:

int INDICE = 13, SOMA = 0, K = 0;

enquanto K < INDICE faça

{

K = K + 1;

SOMA = SOMA + K;

}

imprimir(SOMA);



Ao final do processamento, qual será o valor da variável SOMA?



2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.



IMPORTANTE:

Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;



3) Descubra a lógica e complete o próximo elemento:



a) 1, 3, 5, 7, ___

b) 2, 4, 8, 16, 32, 64, ____

c) 0, 1, 4, 9, 16, 25, 36, ____

d) 4, 16, 36, 64, ____

e) 1, 1, 2, 3, 5, 8, ____

f) 2,10, 12, 16, 17, 18, 19, ____



4) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em uma sala diferente. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada.

Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?


5) Escreva um programa que inverta os caracteres de um string.


IMPORTANTE:

a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

b) Evite usar funções prontas, como, por exemplo, reverse;"""


#questao1
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K


print("Questao 1: o resultado sera igual a:", SOMA)

#questao2
def fibonacci_sequence(n):
    fib_sequence = [0, 1]
    while fib_sequence[-1] < n:
        next_fib = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_fib)
    return fib_sequence

def verifica_numero_fibonacci(numero, sequence):
    if numero in sequence:
        return True
    else:
        return False

numero = 78
print("\nQuestão 2:")
sequencia_fibonacci = fibonacci_sequence(numero)
if verifica_numero_fibonacci(numero, sequencia_fibonacci):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

#questao3
print(""" \nQuestão 3:
    a) Sequência de números ímpares consecutivos.
    Resposta: 1, 3, 5, 7, 9

    b) Sequência de números multiplicados por 2. Cada número é o dobro do anterior.
    Resposta: 2, 4, 8, 16, 32, 64, 128

    c) Sequência de números quadrados. 
    Resposta: 0, 1, 4, 9, 16, 25, 36, 49

    d) Sequência de números quadrados dos números pares. O próximo número após 64 é 100.
    Resposta: 4, 16, 36, 64, 100

    e) Sequência de Fibonacci, onde cada número é a soma dos dois anteriores. 
    Resposta: 1, 1, 2, 3, 5, 8, 13

    f) não sei.""")

#questao4
print(""" \nQuestão 4:
      Primeira ida à sala das lâmpadas: 
      Ligue o primeiro interruptor e espere alguns minutos.
      Desligue o primeiro interruptor e ligue o segundo interruptor.
      Agora temos três cenários possíveis:
      a) Se a lâmpada estiver acesa, então o segundo interruptor controla essa lâmpada.
      b) Se a lâmpada estiver apagada e ainda estiver fria, então o terceiro interruptor controla essa lâmpada.
      c) Se a lâmpada estiver apagada, mas estiver quente, então o primeiro interruptor controla essa lâmpada.

      Segunda ida à sala das lâmpadas:
      Agora, você só precisa verificar o interruptor que não foi usado na primeira ida.
      Se ele estiver ligado, ele controla a lâmpada que estava apagada e fria.
      Se estiver desligado, ele controla a lâmpada que estava apagada e quente.""")


#questao5
def inverter_string(string):
    # Inicializamos uma string vazia para armazenar o resultado
    string_invertida = ""
    
    # Percorremos a string da última posição até a primeira, adicionando os caracteres invertidos à nova string
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]
    
    return string_invertida
print("\nQuestão 5: ")
# Exemplo de uso
string_original = "Python é incrível!"
string_invertida = inverter_string(string_original)
print("String original:", string_original)
print("String invertida:", string_invertida)

