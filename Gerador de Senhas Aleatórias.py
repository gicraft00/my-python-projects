import random
import string
comprimento = int(input('Digite o comprimento da senha'))
caracteres = string.ascii_letters + string.digits + string.punctuation
senha = ''.join(random.choice(caracteres) for i in range(comprimento))
print('senha gerada:', senha)
