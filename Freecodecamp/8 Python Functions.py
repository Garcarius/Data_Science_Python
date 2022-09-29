def fred(): #se empieza la definicion de la funcion
    print("Zap")
def jane():
    print("ABC")

jane()
fred()
jane()

def greet(lang):
    if lang == 'es':
        print('Hola')
    elif lang == 'en':
        print('Hello')
    else:
        print('Bonjour MF')

greet('fr')
