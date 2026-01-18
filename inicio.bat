@echo off
chcp 65001 >nul
title SISTEMA ALCALDIA DE COTA - GOBIERNO DIGITAL
color 0A

echo ============================================
echo   SISTEMA DE GESTION - ALCALDIA DE COTA
echo   GOBIERNO DIGITAL - VERSION DEFINITIVA
echo ============================================
echo.

:: Verificar que estamos en C:\Sistema_Cota
cd /d "C:\Sistema_Cota" 2>nul
if errorlevel 1 (
    echo ERROR: No se encuentra C:\Sistema_Cota
    echo Crea la carpeta y coloca alli los archivos
    pause
    exit /b 1
)

echo ✓ Directorio correcto: %cd%
echo.

:: 1. Verificar Python
echo [1] Verificando Python...
python --version
if errorlevel 1 (
    echo ✗ Python no encontrado
    echo Instala Python desde python.org y marca "Add to PATH"
    pause
    exit /b 1
)

:: 2. Verificar/Instalar dependencias
echo [2] Verificando dependencias...
python -c "import streamlit" 2>nul
if errorlevel 1 (
    echo ✗ Instalando dependencias...
    pip install -r requirements.txt
) else (
    echo ✓ Dependencias OK
)

:: 3. Verificar estructura
echo [3] Verificando estructura...
if not exist "config\cota.json" (
    echo ✗ ERROR: No se encuentra config\cota.json
    echo Crea el archivo de configuracion
    pause
    exit /b 1
)

if not exist "app\main.py" (
    echo ✗ ERROR: No se encuentra app\main.py
    pause
    exit /b 1
)

echo ✓ Estructura OK
echo.

:: 4. Iniciar sistema
echo [4] INICIANDO SISTEMA...
echo.
echo ============================================
echo   URL: http://localhost:8600
echo   Puerto: 8600
echo ============================================
echo.
echo Por favor espera 10 segundos...
echo Se abrira en tu navegador automaticamente.
echo.

:: Cerrar procesos anteriores
taskkill /F /IM python.exe 2>nul
timeout /t 3 /nobreak >nul

:: Iniciar Streamlit
start /B python -m streamlit run app/main.py --server.port 8600 --server.headless false

:: Esperar
timeout /t 10 /nobreak >nul

:: Abrir navegador
start http://localhost:8600

echo.
echo ✓ SISTEMA INICIADO CORRECTAMENTE
echo.
echo Si no se abre, visita manualmente:
echo http://localhost:8600
echo.
echo Presiona Ctrl+C en esta ventana para detener.
echo.
pause