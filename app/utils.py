"""
UTILIDADES DEL SISTEMA - ALCALDÍA DE COTA
"""
import json
import os
import hashlib
from datetime import datetime, date
from pathlib import Path
from .config import ConfigCota

class UtilsCota:
    """Clase con funciones utilitarias para el sistema"""
    
    @staticmethod
    def fecha_actual(formato="%d/%m/%Y"):
        """Devuelve la fecha actual formateada"""
        return datetime.now().strftime(formato)
    
    @staticmethod
    def hora_actual(formato="%H:%M:%S"):
        """Devuelve la hora actual formateada"""
        return datetime.now().strftime(formato)
    
    @staticmethod
    def timestamp():
        """Devuelve un timestamp único"""
        return datetime.now().strftime("%Y%m%d_%H%M%S")
    
    @staticmethod
    def mes_actual_nombre():
        """Devuelve el nombre del mes actual en español"""
        meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]
        return meses[datetime.now().month - 1]
    
    @classmethod
    def guardar_informe(cls, contenido, mes, año, tipo="mensual"):
        """Guarda un informe en la estructura organizada"""
        # Obtener rutas
        reports_dir = ConfigCota.obtener_ruta("reports")
        año_dir = reports_dir / str(año)
        mes_dir = año_dir / mes
        
        # Crear directorios si no existen
        año_dir.mkdir(exist_ok=True)
        mes_dir.mkdir(exist_ok=True)
        
        # Generar nombre de archivo
        timestamp = cls.timestamp()
        nombre_archivo = f"Informe_{tipo}_Cota_{mes}_{año}_{timestamp}.txt"
        ruta_completa = mes_dir / nombre_archivo
        
        # Guardar contenido
        with open(ruta_completa, 'w', encoding='utf-8') as f:
            f.write(contenido)
        
        # Registrar en log
        cls.registrar_log(f"Informe generado: {nombre_archivo}")
        
        return str(ruta_completa)
    
    @classmethod
    def guardar_json(cls, datos, nombre_archivo, subcarpeta=None):
        """Guarda datos en formato JSON"""
        if subcarpeta:
            ruta = ConfigCota.DATA_DIR / "base_datos" / subcarpeta
            ruta.mkdir(exist_ok=True)
            archivo_path = ruta / f"{nombre_archivo}.json"
        else:
            archivo_path = ConfigCota.DATA_DIR / "base_datos" / f"{nombre_archivo}.json"
        
        with open(archivo_path, 'w', encoding='utf-8') as f:
            json.dump(datos, f, indent=2, ensure_ascii=False)
        
        return str(archivo_path)
    
    @classmethod
    def cargar_json(cls, nombre_archivo, subcarpeta=None):
        """Carga datos desde un archivo JSON"""
        if subcarpeta:
            archivo_path = ConfigCota.DATA_DIR / "base_datos" / subcarpeta / f"{nombre_archivo}.json"
        else:
            archivo_path = ConfigCota.DATA_DIR / "base_datos" / f"{nombre_archivo}.json"
        
        try:
            with open(archivo_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}
    
    @staticmethod
    def calcular_hash(texto):
        """Calcula el hash MD5 de un texto (para verificar integridad)"""
        return hashlib.md5(texto.encode()).hexdigest()
    
    @classmethod
    def registrar_log(cls, mensaje, nivel="INFO"):
        """Registra un mensaje en el log del sistema"""
        log_dir = ConfigCota.BASE_DIR / "logs"
        log_dir.mkdir(exist_ok=True)
        
        log_file = log_dir / "sistema.log"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(f"[{timestamp}] [{nivel}] {mensaje}\n")
    
    @classmethod
    def obtener_proyectos_activos(cls):
        """Obtiene la lista de proyectos activos"""
        config = ConfigCota.cargar_configuracion()
        proyectos = config.get("proyectos_prioritarios", [])
        return [p for p in proyectos if p.get("estado") == "En ejecución"]
    
    @classmethod
    def obtener_indicadores_meta(cls):
        """Obtiene los indicadores meta configurados"""
        config = ConfigCota.cargar_configuracion()
        return config.get("indicadores_meta", {})
    
    @classmethod
    def generar_codigo_reporte(cls, mes, año, tipo="GD"):
        """Genera un código único para el reporte"""
        mes_num = datetime.strptime(mes, "%B").month if isinstance(mes, str) else mes
        return f"COTA-{tipo}-{año}-{mes_num:02d}-{cls.timestamp()[-6:]}"
    
    @staticmethod
    def formatear_numero(numero, decimales=0):
        """Formatea un número con separadores de miles"""
        if decimales > 0:
            return f"{numero:,.{decimales}f}".replace(",", "X").replace(".", ",").replace("X", ".")
        else:
            return f"{numero:,}".replace(",", ".")
    
    @classmethod
    def verificar_archivos_sistema(cls):
        """Verifica que todos los archivos necesarios existan"""
        archivos_requeridos = [
            ConfigCota.CONFIG_DIR / "cota.json",
            ConfigCota.BASE_DIR / "requirements.txt",
            ConfigCota.APP_DIR / "main.py"
        ]
        
        resultados = []
        for archivo in archivos_requeridos:
            if archivo.exists():
                resultados.append(f"✓ {archivo.name}")
            else:
                resultados.append(f"✗ {archivo.name} (FALTANTE)")
        
        return resultados

# Instancia global de utilidades
utils = UtilsCota()