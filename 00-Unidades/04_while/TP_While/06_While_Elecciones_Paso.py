import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: Santiago
apellido: Santa Cruz
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        contador = 0
        total_votos = 0
        acumulador_edades = 0

        while True:
            nombre = prompt("mensaje", "Ingrese el nombre del candidato")
            if nombre == None:
                break

            edad = prompt("mensaje", "Ingrese la edad del candidato")
            edad = int(edad)
            if edad == None:
                break
            elif edad < 25:
                edad = int(prompt("mensaje", "Edad invalida! ingrese otra"))
            else:
                acumulador_edades += edad

            votos = prompt("mensaje", "Ingrese la cantidad de votos que obtuvo")
            votos = int(votos)
            if votos == None:
                break
            elif votos < 0:
                votos = int(prompt("mensaje", "Cantidad invalida! ingrese otra"))
            else:
                total_votos += votos

            if contador == 0 or votos > maximo:
                maximo = votos
                candidato_mas_votado = nombre
            
            if contador == 0 or votos < minimo:
                minimo = votos
                candidato_menos_votado = nombre
                edad_menos_votado = edad
            
            contador += 1

            
        promedio = int(acumulador_edades / contador)


        alert("mensaje", f"nombre del candidato con mas votos {candidato_mas_votado}\nnombre del candidato con menos votos {candidato_menos_votado} con {edad_menos_votado} años\npromedio de edades de los candidatos: {promedio}\ntotal de votos emitidos: {total_votos}")

            


if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
