import subprocess
import time
import os
import webbrowser
from pathlib import Path


class AbrirProgramas:

    def abrir_programas(self, programas):
        for programa in programas:
            try:
                if not Path(programa).exists():
                    print(f"No existe el programa: {programa}")
                    continue

                subprocess.Popen([programa])
                print(f"Programa abierto: {programa}")
                time.sleep(3)

            except Exception as e:
                print(f"Error al abrir {programa}: {e}")

    def abrir_archivos(self, archivos):
        for archivo in archivos:
            try:
                if not Path(archivo).exists():
                    print(f"No existe el archivo: {archivo}")
                    continue

                os.startfile(archivo)
                print(f"Archivo abierto: {archivo}")
                time.sleep(2)

            except Exception as e:
                print(f"Error al abrir archivo {archivo}: {e}")
    
    def abrir_webs(self, urls):
        for url in urls:
            try:
                webbrowser.open(url)
                print(f"Web abierta: {url}")
                time.sleep(2)
            except Exception as e:
                print(f"Error al abrir la web {url}: {e}")


if __name__ == '__main__':

    archivos = [
        r'C:\Users\jalvaredo\OneDrive - CV CONTROL SA\Sincro\Bancos\BANCOS actualizado.xlsm'
    ]

    programas = [
        r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE',
        r'C:\Program Files\Google\Chrome\Application\chrome.exe'
    ]

    urls = [
        'https://cvcontrol.odoo.com/web/login?redirect=%2Fodoo%3F',
        'https://www.galicia.ar/',
        'https://bna.com.ar/',
        'https://clientes.balanz.com/auth/login',
        'https://web.whatsapp.com/'
        
    ]

    iniciar = AbrirProgramas()
    iniciar.abrir_archivos(archivos)
    time.sleep(2)
    iniciar.abrir_programas(programas)
    iniciar.abrir_webs(urls)
