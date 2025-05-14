import subprocess
import time
import os


class AbrirProgramas:
    
    def abrir_programas(self, programas):
        for programa in programas:
            try:
                subprocess.Popen(programa)
                print(f"Programa abierto: {programa}")
                time.sleep(3)
            except Exception as e:
                print(f"Error al abrir {programa}: {e}")

    def abrir_archivos(self, archivos):
        for archivo in archivos:
            try:
                os.startfile(archivo)
                print(f"Archivo abierto: {archivo}")
                time.sleep(2)
            except Exception as e:
                print(f"Error al abrir archivo {archivo}: {e}")


if __name__ == '__main__':

    archivos = [
        r'C:\Users\jalvaredo\OneDrive - CV CONTROL SA\Sincro\Bancos\BANCOS actualizado.xlsm',
        r'C:\Users\jalvaredo\OneDrive - CV CONTROL SA\Sincro\LISTADO DE COBRANZAS.xlsx'
    ]

    programas = [
        r'C:\Program Files\Microsoft Office\root\Office16\OUTLOOK.EXE',
        r'c:\Program Files\Google\Chrome\Application\chrome.exe',
        r'C:\Program Files (x86)\TANGO GESTION\Cliente\Aplicaciones\MENUA.EXE'
    ]

    iniciar = AbrirProgramas()
    iniciar.abrir_archivos(archivos)
    time.sleep(2)
    iniciar.abrir_programas(programas)
