def calcular_distancia(velocidade_media, tempo):
    """
    Calcula a distancia percorrida usando velocidade media e tempo.
    Args:
        velocidade_media: A velocidade media do objeto.
        tempo: O tempo decorrido.
    Returns:
        A distancia percorrida.
    """
    distancia = velocidade_media * tempo
    return distancia

# exemplo de uso
velocidade = 60  # km/h
tempo = 2  # h
distancia = calcular_distancia(velocidade, tempo)
print(f'A distancia percorrida é de {distancia} km')