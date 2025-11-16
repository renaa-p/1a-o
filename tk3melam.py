#Autor Renato Ortiz s2
import tkinter as tk
from tkinter import messagebox

def medida_corte():
    ancho_placa = 244
    alto_placa = 215
    area_placa = ancho_placa * alto_placa
    ancho_pieza = float(entrada_ancho_pieza.get())
    alto_pieza = float(entrada_alto_pieza.get())
    area_pieza = ancho_pieza * alto_pieza
    num_piezas = int(entrada_num_piezas.get())
    area_total_piezas = area_pieza * num_piezas
    perdida_por_corte = 0.4

#Calcular el número total de cortes requeridos
    cortes_por_pieza = (ancho_pieza + alto_pieza) * 2 / ancho_placa + (ancho_pieza + alto_pieza) * 2 / alto_placa
    cortes_totales = cortes_por_pieza * num_piezas

#Area total perdida por cortes
    area_total_perdida = cortes_totales * perdida_por_corte

#Calcular número de placas necesarias
    num_placas = area_total_piezas / (area_placa - area_total_perdida)
    num_placas = int(num_placas) + 1 if num_placas % 1 != 0 else int(num_placas)

#Costo total
    precio_placa = 29900
    costo_total = num_placas * precio_placa

#Material sobrante
    area_sobrante = num_placas * area_placa - area_total_piezas - area_total_perdida

#Mostrar resultados
    texto_resultado = f"Número de placas necesarias: {num_placas}\n"
    texto_resultado += f"Costo total: ${costo_total}\n"
    texto_resultado += f"Superficie perdida por cortes: {area_total_perdida:.2f} cm²\n"
    texto_resultado += f"Superficie sobrante: {area_sobrante:.2f} cm²"

    messagebox.showinfo("Resultados", texto_resultado)

ventana = tk.Tk()
ventana.geometry("300x150")
ventana.title("Cálculo de cortes de melamina")

tk.Label(ventana, text="Ancho de la pieza (cm):").grid(row=2, column=0)
entrada_ancho_pieza = tk.Entry(ventana)
entrada_ancho_pieza.grid(row=2, column=1)

tk.Label(ventana, text="Alto de la pieza (cm):").grid(row=3, column=0)
entrada_alto_pieza = tk.Entry(ventana)
entrada_alto_pieza.grid(row=3, column=1)

tk.Label(ventana, text="Número de piezas:").grid(row=4, column=0)
entrada_num_piezas = tk.Entry(ventana)
entrada_num_piezas.grid(row=4, column=1)

boton_calcular = tk.Button(ventana, text="Calcular", command=medida_corte)
boton_calcular.grid(row=5, column=0, columnspan=2)

ventana.mainloop()