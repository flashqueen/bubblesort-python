import cv2
import numpy as np

letrasgerais = input("Digite as letras a seguir: ")
letrasgerais = letrasgerais.split()


def bubbleSort(letrasgerais):
    for x in range(len(letrasgerais)-1, 0, -1):
        for i in range(x):
            if letrasgerais[i] > letrasgerais[i+1]:
                temp = letrasgerais[i]
                letrasgerais[i] = letrasgerais[i+1]
                letrasgerais[i+1] = temp

bubbleSort(letrasgerais)
print(letrasgerais)

#letras = sorted(letrasgerais, key=str.lower)
