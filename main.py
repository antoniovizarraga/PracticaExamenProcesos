from multiprocessing import Process, Queue
from time import sleep

# Función que utiliza el queue o cola para funcionar
def sumaValoresQueue(cola):
    res = 0
    limiteReal = cola.get()

    

    while limiteReal is not None:

        limiteReal = int(limiteReal)

        limite = limiteReal

        limiteReal += 1


        for i in range(limiteReal):
            res += i
            
        print("Suma de todos los valores hasta el " + str(limite) + ": " + str(res))

        res = 0

        limiteReal = cola.get()
        

    #return res

# La misma función que la anterior creada pero evita el uso de Queue
def sumaValores(limite):
    res = 0
    limiteReal = limite

    


    limiteReal += 1


    for i in range(limiteReal):
        res += i
            
    print("Suma de todos los valores hasta el " + str(limite) + ": " + str(res))

    res = 0

    

    return res

# Función que lee el contenido de un fichero establecido por
# parámetro línea por línea y su contenido lo introduce
# dentro del queue insertado también por parámetro.
def leeFicheroQueue(rutaFichero, cola):
    fichero = open(rutaFichero)

    for linea in fichero:
        cola.put(linea)
        sleep(2)
    
    fichero.close()


    cola.put(None)


    


if __name__ == "__main__":
    queue = Queue() # Se crea una cola

    # Se crean los procesos que llevarán a cabo las dos funciones
    proceso1 = Process(target=leeFicheroQueue, args=("numeros.txt",queue))
    proceso2 = Process(target=sumaValoresQueue, args=(queue,))

    # Se inician los procesos
    print("Inicio proceso 1")
    proceso1.start()
    print("Inicio proceso 2")
    proceso2.start()


    # Se espera a que termine el proceso 1
    proceso1.join()

    print("Proceso 1 terminado")

    # Se espera a que termine el proceso 2
    proceso2.join()

    print("Proceso 2 terminado")




