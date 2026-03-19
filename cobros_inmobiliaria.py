# 1. LOS INVITADOS (Imports) - Siempre en la línea 1
import tkinter as tk

# 2. EL MANUAL DE INSTRUCCIONES (La Función)
def procesar_factura():
    try:
        # Aquí conectamos la "tubería" con los muebles
        # Usamos los nombres de los Entry que crearemos abajo
        ca = float(entrada_canon.get())
        tasa = float(entrada_tasa.get())
        dia = int(entrada_dia.get())
        iva = 1.16
        
        monto_bs = ca * tasa * iva
        
        if dia > 5:
            resultado.config(text=f"MORA: Bs. {monto_bs + (50 * tasa):.2f}", fg="red")
        else:
            resultado.config(text=f"AL DÍA: Bs. {monto_bs:.2f}", fg="green")
            
    except ValueError:
        resultado.config(text="Error: Ingrese números", fg="orange")

# 3. LA CASA Y LOS MUEBLES (Interfaz) - Fuera de la función
ventana = tk.Tk()
ventana.title("Control de Cobros")
ventana.geometry("500x500")
# Mueble 1: Canon
tk.Label(ventana, text="Monto Canon (USD):").pack()
entrada_canon = tk.Entry(ventana)
entrada_canon.pack()

# Mueble 2: Tasa
tk.Label(ventana, text="Tasa BCV:").pack()
entrada_tasa = tk.Entry(ventana)
entrada_tasa.pack()

# Mueble 3: Día
tk.Label(ventana, text="Día de Pago:").pack()
entrada_dia = tk.Entry(ventana)
entrada_dia.pack()

# El Botón que activa la receta
boton = tk.Button(ventana, text="Calcular", command=procesar_factura)
boton.pack(pady=10)

# El letrero de salida
resultado = tk.Label(ventana, text="")
resultado.pack()

# 4. EL SERVICIO (El bucle infinito)
ventana.mainloop()