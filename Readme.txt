# Proyecto de Monitoreo de Temperatura

## Descripción

Este proyecto tiene como objetivo monitorear y controlar las temperaturas en un proceso de soldadura sin plomo. Utiliza un modelo de inteligencia artificial para predecir temperaturas basadas en datos históricos y sugiere correcciones en tiempo real. La aplicación está construida con Flask y proporciona una interfaz web para interactuar con el modelo.

## Componentes Clave

1. **Modelo de IA**:
   - Implementado en `Base/ai_model.py`.
   - Utiliza regresión lineal para predecir temperaturas.
   - Funciones clave:
     - `train_model(X, y)`: Entrena el modelo con datos de entrada.
     - `predict_temperature(model, time_sec)`: Predice la temperatura esperada para un tiempo dado.

2. **Gestión de Temperaturas**:
   - Implementado en `Base/temperature_profile.py`.
   - Define el perfil de temperatura ideal para la soldadura.
   - Función clave:
     - `define_temperature_profile()`: Devuelve un diccionario con las etapas del perfil de temperatura.

3. **Aplicación Flask**:
   - Implementada en `Base/flask_app.py`.
   - Proporciona rutas para acceder a datos de temperatura.
   - Funciones clave:
     - Ruta `/`: Renderiza la página principal.
     - Ruta `/get_temperature`: Devuelve la temperatura actual y esperada en formato JSON.

4. **Visualización de Datos**:
   - Implementado en `Base/data_visualization.py`.
   - Muestra las temperaturas en tiempo real utilizando gráficos animados.
   - Función clave:
     - `visualize_temperature(serial_port)`: Configura y actualiza el gráfico con datos de temperatura.

5. **Inicialización**:
   - Implementado en `Base/firstSteps.py`.
   - Carga y entrena el modelo al inicio.
   - Configura la aplicación Flask y el puerto serial para la lectura de datos.

## Flujo de Trabajo

1. **Entrenamiento del Modelo**:
   - Se entrena un modelo de regresión lineal con datos de temperatura históricos.
   - El modelo se guarda en un archivo para su uso posterior.

2. **Interacción con la Aplicación**:
   - Los usuarios pueden acceder a la aplicación Flask a través de un navegador web.
   - Se pueden obtener datos de temperatura actuales y esperadas mediante la ruta `/get_temperature`.

3. **Visualización en Tiempo Real**:
   - Las temperaturas se visualizan en tiempo real utilizando gráficos animados que se actualizan con datos leídos desde un puerto serial.

## Instrucciones de Uso

1. **Instalación de Dependencias**:
   - Asegúrate de tener instaladas las bibliotecas necesarias, como Flask, NumPy, scikit-learn y Matplotlib.

2. **Ejecutar la Aplicación**:
   - Inicia la aplicación Flask ejecutando el siguiente comando en la terminal:
     ```bash
     python Base/flask_app.py
     ```

3. **Acceso a la Aplicación**:
   - Abre un navegador web y accede a `http://localhost:5000` para interactuar con la aplicación.

4. **Obtener Datos de Temperatura**:
   - Visita la ruta `/get_temperature` para obtener la temperatura actual y esperada en formato JSON.

## Ejemplos de Uso

- **Obtener Temperatura**:
  - Realiza una solicitud GET a `/get_temperature` para recibir un JSON con los datos de temperatura.

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request con tus sugerencias o mejoras.
