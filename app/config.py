"""
CONFIGURACIÓN DEL SISTEMA - ALCALDÍA DE COTA
"""
import json
import os
from pathlib import Path

class ConfigCota:
    """Clase para manejar la configuración del sistema"""
    
    # Rutas del sistema
    BASE_DIR = Path("C:/Sistema_Cota")
    CONFIG_DIR = BASE_DIR / "config"
    DATA_DIR = BASE_DIR / "data"
    REPORTS_DIR = BASE_DIR / "reports"
    APP_DIR = BASE_DIR / "app"
    
    @classmethod
    def cargar_configuracion(cls):
        """Carga la configuración desde cota.json"""
        config_path = cls.CONFIG_DIR / "cota.json"
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = json.load(f)
            return config
        except FileNotFoundError:
            print(f"⚠️  Advertencia: No se encontró {config_path}")
            return cls._configuracion_por_defecto()
        except json.JSONDecodeError:
            print(f"❌ Error: Archivo cota.json corrupto")
            return cls._configuracion_por_defecto()
    
    @staticmethod
    def _configuracion_por_defecto():
        """Configuración por defecto si no existe el archivo"""
        return {
            "municipio": {
                "nombre": "Cota",
                "nombre_completo": "Municipio de Cota, Cundinamarca",
                "codigo_dane": "25224"
            },
            "alcaldia": {
                "direccion": "Carrera 6 # 3-21, Centro",
                "telefono_principal": "(601) 123 4567",
                "correo_sistemas": "sistemas@cota-cundinamarca.gov.co",
                "sitio_web": "https://www.cota-cundinamarca.gov.co"
            },
            "sistema": {
                "nombre": "Sistema de Gestión de Gobierno Digital",
                "version": "1.0.0",
                "puerto_default": 8600
            }
        }
    
    @classmethod
    def obtener_ruta(cls, tipo, crear=True):
        """Obtiene rutas del sistema"""
        rutas = {
            "base": cls.BASE_DIR,
            "config": cls.CONFIG_DIR,
            "data": cls.DATA_DIR,
            "reports": cls.REPORTS_DIR,
            "app": cls.APP_DIR,
            "documentos": cls.DATA_DIR / "documentos",
            "evidencias": cls.DATA_DIR / "evidencias",
            "base_datos": cls.DATA_DIR / "base_datos"
        }
        
        ruta = rutas.get(tipo)
        if ruta and crear and not ruta.exists():
            ruta.mkdir(parents=True, exist_ok=True)
        
        return ruta
    
    @classmethod
    def verificar_estructura(cls):
        """Verifica y crea la estructura de carpetas necesaria"""
        carpetas = [
            cls.BASE_DIR,
            cls.CONFIG_DIR,
            cls.DATA_DIR,
            cls.REPORTS_DIR,
            cls.DATA_DIR / "documentos",
            cls.DATA_DIR / "evidencias",
            cls.DATA_DIR / "base_datos",
            cls.REPORTS_DIR / "2024"
        ]
        
        for carpeta in carpetas:
            if not carpeta.exists():
                print(f"📁 Creando carpeta: {carpeta}")
                carpeta.mkdir(parents=True, exist_ok=True)
        
        print("✅ Estructura de carpetas verificada")
        return True

# Instancia global de configuración
config = ConfigCota.cargar_configuracion()