"""
El ejercicio consiste en escribir una función
recursiva que calcule el valor de la serie armónica hasta un número n dado."""


def seriearmonica(n):
    if n == 1:
        return 1
    else:
        return 1 / n + seriearmonica(n-1)