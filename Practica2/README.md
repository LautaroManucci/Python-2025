# Proyecto: Analisis de Partidas y MVPs

Este proyecto analiza los resultados de varias partidas, generando rankings y determinando los MVPs.
El codigo fuente con las funciones necesarias se encuentra en el directorio `src`, mientras que los notebooks de analisis estan en la carpeta `notebooks`.

## Instalacion de Dependencias

Para ejecutar este proyecto, se recomienda crear un entorno virtual y luego instalar las dependencias necesarias.

### 1. Crear un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
```

### 2. Activar el entorno virtual
- En Windows:
  ```bash
  venv\Scripts\activate
  ```
- En macOS/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Instalar dependencias
Ejecuta el siguiente comando en la terminal dentro del proyecto:
```bash
pip install -r requirements.txt
```

## Ejecución del Proyecto desde el notebook
Asegurate de estar en el entorno virtual y luego abre Jupyter Notebook:
```bash
jupyter notebook
```
Dentro de Jupyter, navega hasta la carpeta `notebooks` y abre el archivo correspondiente.

## Estructura del Proyecto
```
Practica2/
│── notebooks/           # Notebooks con analisis y resultados
    ├── Ej10.ipynb
│── src/                 # Código fuente y funciones
│   ├── __init__.py      # Este archivo lo hace un paquete
│   ├── funciones.py     # Archivo donde estan las funciones
│── requirements.txt     # Dependencias del proyecto
│── README.md            # Instrucciones y documentación
```

## Autor
Lautaro David Manucci

¡Disfruta el analisis de partidas! 🚀