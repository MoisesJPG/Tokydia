@echo off
cls

:: Configuración del servicio web
set Port=8080

:: Iniciar el servidor HTTP de Python
python -m http.server %Port%

pause