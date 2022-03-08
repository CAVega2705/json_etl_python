# JSON ETL [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

import json
from turtle import color
import requests

import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    
    # Ejercicio de consumo de datos por API
    url = "https://jsonplaceholder.typicode.com/todos"

    # El primer paso es que copien esa URL en su explorador web
    # y analicen los datos en general:
    # 1) Observando la URL se puede ver que en total hay 200 entradas,
    # del id=1 al id=200
    # 2) Observando la URL se puede ver que en total hay 10 usuarios,
    # del userId=1 al userId=10
    # 3) En cada entrada se especifica si el usuario completó ese título,
    # mediante el campo "completed".


    # Alumno, de cada usuario en el total de las 200 entradas
    # debe contar cuantos títulos completó cada usuario (de los 10 posibles)
    # y armar un gráfico de barras resumiendo la información.
    # gráfico en el eje "x" está cada uno de los 10 usuarios y en el eje
    # "y" la cantidad de títulos completados

    # Para poder ir haciendo esto debe ir almacenando la información
    # de cada usuario a medida que "itera" en un bucle los datos
    # del JSON recolectado. Al finalizar el bucle deberá tener la data
    # de los 10 usuarios con cuantos títulos completó cada uno.

    # Debe poder graficar dicha información en un gráfico de barras.
    # En caso de no poder hacer el gráfico comience por usar print
    # para imprimir cuantos títulos completó cada usuario
    # y verifique si los primeros usuarios (mirando la página a ojo)
    # los datos recolectados son correctos.

    data =  requests.get("https://jsonplaceholder.typicode.com/todos")
    respuestas = data.json()
    userID_1 = 0
    userID_2 = 0
    userID_3 = 0
    userID_4 = 0
    userID_5 = 0
    userID_6 = 0
    userID_7 = 0
    userID_8 = 0
    userID_9 = 0
    userID_10 = 0

    for user in respuestas:
        if user['completed'] == True:
            if user['userId'] == 1:
                userID_1 = userID_1 + 1
            elif user['userId'] == 2:
                userID_2 = userID_2 + 1
            elif user['userId'] == 3:
                userID_3 = userID_3 + 1
            elif user['userId'] == 4:
                userID_4 = userID_4 + 1
            elif user['userId'] == 5:
                userID_5 = userID_5 + 1
            elif user['userId'] == 6:
                userID_6 = userID_6 + 1
            elif user['userId'] == 7:
                userID_7 = userID_7 + 1
            elif user['userId'] == 8:
                userID_8 = userID_8 + 1
            elif user['userId'] == 9:
                userID_9 = userID_9 + 1
            elif user['userId'] == 10:
                userID_10 = userID_10 + 1

    notas = [userID_1, userID_2, userID_3, userID_4, userID_5, userID_6, userID_7, userID_8, userID_9, userID_10]
    usuarios = [1,2,3,4,5,6,7,8,9,10]

    fig = plt.figure()
    plot = fig.add_subplot()

    plot.bar(usuarios, notas, label='Pruebas Completas')           
    plot.set_facecolor('darkred')
    plot.set_title("Títulos completados por cada usuario")
    plot.set_ylabel("Cantidad de Titulos")
    plot.set_xlabel("UserId")
    plot.set_xticks(range(1, 11))
    plot.set_yticks(range(0, 15))
    plt.show()  

    print("terminamos")