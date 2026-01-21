# Abrir Archivos y Programas Automáticamente

Este script de Python permite abrir automáticamente una serie de archivos (como documentos de Excel) y programas (como Outlook, Chrome o TANGO GESTIÓN) en un entorno Windows. Es útil para automatizar la rutina diaria al iniciar el equipo o comenzar una jornada laboral.

## 🚀 Características

- Abre múltiples archivos con `os.startfile`
- Abre múltiples programas con `subprocess.Popen`
- Abre múltiples url con `webbrowser.open`
- Incluye manejo básico de errores
- Añade pausas entre cada apertura para evitar saturar el sistema

## 🧰 Requisitos

- Python 3.x
- Sistema operativo: Windows
- Acceso a las rutas especificadas en el script

## 📝 Uso

1. Clona este repositorio o copia el script a tu máquina local.
2. Personaliza las rutas en las variables `archivos` y `programas` con las ubicaciones de tus archivos y programas deseados.
3. Ejecuta el script desde la terminal o doble clic si lo conviertes a `.pyw`.

```bash
python abrir_programas.py
