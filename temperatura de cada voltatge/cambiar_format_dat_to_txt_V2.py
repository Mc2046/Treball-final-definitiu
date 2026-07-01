import sys
import os

def limpiar_datos_namd(archivo_entrada):
    # Comprobamos si el archivo original existe
    if not os.path.exists(archivo_entrada):
        print(f"Error: No encuentro el archivo '{archivo_entrada}'.")
        print("Asegúrate de que lo has escrito bien y estás en la carpeta correcta.")
        return

    # Magia de nombres: separamos el nombre de la extensión original (.dat, .log, etc)
    nombre_base, extension_original = os.path.splitext(archivo_entrada)
    
    # Creamos el nuevo nombre añadiendo "_Excel.txt" al final
    archivo_salida = f"{nombre_base}_Excel.txt"

    with open(archivo_entrada, 'r') as f_in, open(archivo_salida, 'w') as f_out:
        # Escribimos los encabezados (he puesto "Valor" para que te sirva para Corriente, Temperatura, Energía...)
        f_out.write("Tiempo(ns)\tValor\n")
        
        lineas_procesadas = 0
        for linea in f_in:
            partes = linea.split()
            
            # Filtramos: que tenga 2 columnas y la primera sea un número (aceptando decimales)
            if len(partes) >= 2 and partes[0].replace('.', '', 1).isdigit():
                # Aplicamos el replace a ambas columnas para poner coma en lugar de punto
                paso = partes[0].replace(".", ",")
                valor = partes[1].replace(".", ",")
                
                f_out.write(f"{paso}\t{valor}\n")
                lineas_procesadas += 1
                
    print("-" * 50)
    print(f"¡Éxito! Se han procesado {lineas_procesadas} líneas.")
    print(f"Tus datos listos para Excel están en: '{archivo_salida}'")
    print("-" * 50)

# ==========================================
# LECTURA DESDE LA TERMINAL
# ==========================================
if __name__ == "__main__":
    # Comprobamos que le has pasado un archivo al ejecutar el comando
    if len(sys.argv) < 2:
        print("\nUso incorrecto. Faltan argumentos.")
        print("Debes ejecutar el programa así:")
        print("python3 cambiar_format_dat_to_txt.py <nombre_del_archivo>\n")
    else:
        # sys.argv[1] coge la primera palabra que escribas después de "cambiar_format_dat_to_txt.py"
        archivo_indicado = sys.argv[1]
        limpiar_datos_namd(archivo_indicado)
