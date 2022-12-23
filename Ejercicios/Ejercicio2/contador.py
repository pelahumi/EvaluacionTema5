from io import open
import sys

def visitas():

    contador = open("contador.txt", "a+")
    contador.seek(0)

    try:
        escribir = int(contador.readline())
        if len(sys.argv) == 1:
            if sys.argv[1] == "inc":
                escribir += 1
            elif sys.argv[2] == "dec":
                escribir -= 1
        print(escribir)
        contador = open("contador.txt", "r")
        contador.write(str(escribir))
        contador.close()
    except:
        print("Error: archivo corrupto")

        

