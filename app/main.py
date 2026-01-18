# A PRINCIPAL - GOBIERNO DIGITAL
# Alcaldía Municipal de Cota - Versión Definitiva
"""
SISTEMA DE GESTIÓN - GOBIERNO DIGITAL
ALCALDÍA MUNICIPAL DE COTA - VERSIÓN DEFINITIVA
"""
import streamlit as st
import os
import sys
from datetime import datetime

# Configurar rutas
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Configuración básica (sin módulos locales)
config = {
    "municipio": {
        "nombre": "Cota", 
        "nombre_completo": "Municipio de Cota",
        "codigo_dane": "25290",
        "nit": "899999034-1",
        "departamento": "Cundinamarca"
    },
    "alcaldia": {
        "sitio_web": "https://www.cota-cundinamarca.gov.co",
        "correo_sistemas": "sistemas@cota-cundinamarca.gov.co",
        "direccion": "Cra 5 # 4-30, Cota, Cundinamarca",
        "telefono_principal": "(+57 1) 896 7000",
        "secretario_tic": "ING. CARLOS ALBERTO GÓMEZ",
        "alcalde": "DR. JUAN PABLO GARCÍA"
    },
    "sistema": {
        "version": "1.0.0"
    }
}

# Funciones de utilidad
def fecha_actual():
    return datetime.now().strftime("%d/%m/%Y")

def hora_actual():
    return datetime.now().strftime("%H:%M:%S")

def guardar_informe(contenido, mes, año):
    # En lugar de guardar archivo, devolvemos ruta simulada
    return f"informes/Informe_Cota_{mes}_{año}.txt"

# ============================================
# CONFIGURACIÓN DE STREAMLIT
# ============================================
st.set_page_config(
    page_title=f"Sistema de Gestión - {config['municipio']['nombre']}",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CSS PERSONALIZADO
# ============================================
st.markdown("""
<style>
    /* Estilos para Alcaldía de Cota */
    .cota-header {
        background: linear-gradient(135deg, #1e3a8a 0%, #2d4d9c 100%);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-bottom: 25px;
        text-align: center;
    }
    
    .cota-card {
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #10b981;
        box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }
    
    .cota-badge {
        background: #10b981;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.9em;
        display: inline-block;
        margin: 3px;
    }
    
    .stButton > button {
        background-color: #1e3a8a;
        color: white;
        border: none;
        padding: 12px 30px;
        border-radius: 8px;
        font-weight: bold;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        background-color: #2d4d9c;
        transform: translateY(-2px);
    }
    
    .metric-box {
        background: #f8f9fa;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# ============================================
# FUNCIÓN PRINCIPAL
# ============================================
def main():
    # ENCABEZADO OFICIAL
    st.markdown(f"""
    <div class="cota-header">
        <h1 style="margin:0">🏛️ ALCALDÍA MUNICIPAL DE {config['municipio']['nombre'].upper()}</h1>
        <h3 style="margin:10px 0; color:#dbeafe">Sistema de Gestión de Gobierno Digital</h3>
        <div style="margin-top:15px">
            <span class="cota-badge">Código DANE: {config['municipio']['codigo_dane']}</span>
            <span class="cota-badge">NIT: {config['municipio']['nit']}</span>
            <span class="cota-badge">{config['municipio']['departamento']}</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # BARRA LATERAL
    with st.sidebar:
        # Logo/imagen alternativa
        st.markdown("""
        <div style="background:#1e3a8a; padding:20px; border-radius:10px; text-align:center; color:white;">
        <h3>🏛️</h3>
        <h4>ALCALDÍA DE COTA</h4>
        <p>Sistema de Gestión</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📅 Período del Informe")
        
        col1, col2 = st.columns(2)
        with col1:
            mes = st.selectbox(
                "Mes",
                ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"],
                index=datetime.now().month - 1
            )
        with col2:
            año = st.number_input("Año", 2024, 2030, 2024)
        
        st.markdown("---")
        st.markdown("### 👤 Datos del Responsable")
        
        nombre = st.text_input("Nombre completo", "INGENIERO DE SISTEMAS")
        cargo = st.selectbox(
            "Cargo",
            ["Contrato de Prestación de Servicios", "Funcionario", "Consultor"]
        )
        
        st.markdown("---")
        st.info(f"**📞 Contacto:** {config['alcaldia']['correo_sistemas']}")
    
    # ============================================
    # FORMULARIO DE ACTIVIDADES
    # ============================================
    st.markdown("### ✅ ACTIVIDADES REALIZADAS")
    
    # Actividades organizadas por categoría
    actividades_categorias = {
        "Planificación": [
            "Revisión política gobierno digital",
            "Actualización diagnóstico TIC",
            "Planificación estratégica",
            "Definición de indicadores"
        ],
        "Implementación": [
            "Desarrollo portal web",
            "Configuración sistemas",
            "Implementación seguridad",
            "Migración sistemas"
        ],
        "Seguimiento": [
            "Monitoreo indicadores",
            "Seguimiento proyectos",
            "Análisis métricas",
            "Reporte novedades"
        ],
        "Capacitación": [
            "Capacitación funcionarios",
            "Entrenamiento seguridad",
            "Charlas sensibilización",
            "Asesoría técnica"
        ]
    }
    
    actividades_seleccionadas = []
    
    for categoria, actividades in actividades_categorias.items():
        with st.expander(f"📋 {categoria}", expanded=True):
            cols = st.columns(2)
            for idx, actividad in enumerate(actividades):
                col_idx = idx % 2
                if cols[col_idx].checkbox(actividad, key=f"{categoria}_{actividad}"):
                    actividades_seleccionadas.append(f"{categoria}: {actividad}")
    
    # ============================================
    # INDICADORES (SIN PANDAS)
    # ============================================
    st.markdown("### 📊 INDICADORES DE GESTIÓN")
    
    col_met1, col_met2, col_met3, col_met4 = st.columns(4)
    
    with col_met1:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.markdown("**🌐 Portal Web**")
        visitas = st.number_input("Visitas", 0, 100000, 1500, key="visitas", label_visibility="collapsed")
        st.markdown(f"**{visitas:,}** visitas")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='metric-box' style='margin-top:10px'>", unsafe_allow_html=True)
        paginas = st.number_input("Páginas", 0, 50000, 4200, key="paginas", label_visibility="collapsed")
        st.markdown(f"**{paginas:,}** páginas")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_met2:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.markdown("**📄 Trámites**")
        tramites = st.number_input("Online", 0, 10000, 65, key="tramites", label_visibility="collapsed")
        st.markdown(f"**{tramites}** online")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='metric-box' style='margin-top:10px'>", unsafe_allow_html=True)
        pqrs = st.number_input("PQRS", 0, 1000, 22, key="pqrs", label_visibility="collapsed")
        st.markdown(f"**{pqrs}** PQRS")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_met3:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.markdown("**👥 Capacitación**")
        capacitados = st.number_input("Personas", 0, 500, 14, key="capacitados", label_visibility="collapsed")
        st.markdown(f"**{capacitados}** personas")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='metric-box' style='margin-top:10px'>", unsafe_allow_html=True)
        horas = st.number_input("Horas", 0, 500, 28, key="horas", label_visibility="collapsed")
        st.markdown(f"**{horas}** horas")
        st.markdown("</div>", unsafe_allow_html=True)
    
    with col_met4:
        st.markdown("<div class='metric-box'>", unsafe_allow_html=True)
        st.markdown("**🖥️ Infraestructura**")
        servidores = st.number_input("Servidores", 0, 50, 6, key="servidores", label_visibility="collapsed")
        st.markdown(f"**{servidores}** servidores")
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("<div class='metric-box' style='margin-top:10px'>", unsafe_allow_html=True)
        disponibilidad = st.slider("Disponibilidad %", 0, 100, 99, key="dispo", label_visibility="collapsed")
        st.markdown(f"**{disponibilidad}%** disponibilidad")
        st.markdown("</div>", unsafe_allow_html=True)
    
    # ============================================
    # GENERAR INFORME
    # ============================================
    st.markdown("---")
    st.markdown("### 🚀 GENERAR INFORME OFICIAL")
    
    if st.button("📄 GENERAR INFORME COMPLETO", type="primary", use_container_width=True):
        # Crear contenido del informe
        contenido = f"""
{'='*70}
INFORME DE GESTIÓN - GOBIERNO DIGITAL
ALCALDÍA MUNICIPAL DE {config['municipio']['nombre'].upper()}, {config['municipio']['departamento'].upper()}
{'='*70}

PERÍODO: {mes} de {año}
FECHA: {fecha_actual()} {hora_actual()}
RESPONSABLE: {nombre}
CARGO: {cargo}

{'='*70}
ACTIVIDADES REALIZADAS ({len(actividades_seleccionadas)})
{'='*70}
{chr(10).join(['• ' + act for act in actividades_seleccionadas])}

{'='*70}
INDICADORES
{'='*70}
PORTAL WEB:
• Visitas: {visitas:,}
• Páginas vistas: {paginas:,}

TRÁMITES DIGITALES:
• Trámites online: {tramites}
• PQRS digitales: {pqrs}

CAPACITACIÓN:
• Personas capacitadas: {capacitados}
• Horas de capacitación: {horas}

INFRAESTRUCTURA:
• Servidores activos: {servidores}
• Disponibilidad: {disponibilidad}%

{'='*70}
FIRMAS
{'='*70}

Elaborado por:
___________________________
{nombre}
{cargo}

Revisado por:
___________________________
{config['alcaldia']['secretario_tic']}
Oficina de Sistemas y TIC

Aprobado por:
___________________________
{config['alcaldia']['alcalde']}
Alcaldía Municipal de {config['municipio']['nombre']}

{'='*70}
INFORMACIÓN DE CONTACTO
{'='*70}
• Dirección: {config['alcaldia']['direccion']}
• Teléfono: {config['alcaldia']['telefono_principal']}
• Correo: {config['alcaldia']['correo_sistemas']}
• Web: {config['alcaldia']['sitio_web']}

{'='*70}
*Documento generado por Sistema de Gestión v{config['sistema']['version']}*
{'='*70}
"""
        
        # Guardar informe (simulado)
        ruta = guardar_informe(contenido, mes, año)
        
        # Mostrar éxito
        st.success(f"✅ INFORME GENERADO EXITOSAMENTE")
        st.balloons()
        
        # Botón de descarga
        st.download_button(
            label="📥 DESCARGAR INFORME (.TXT)",
            data=contenido,
            file_name=f"Informe_Cota_{mes}_{año}.txt",
            mime="text/plain",
            type="primary"
        )
        
        # Mostrar información
        with st.expander("📋 VER DETALLES DEL INFORME"):
            st.text(contenido)
    
    # ============================================
    # PIE DE PÁGINA
    # ============================================
    st.markdown("---")
    st.markdown(f"""
    <div style="text-align:center; color:#666; font-size:0.9em">
    <strong>© 2024 - Alcaldía Municipal de {config['municipio']['nombre']}, {config['municipio']['departamento']}</strong><br>
    Sistema de Gestión de Gobierno Digital v{config['sistema']['version']}<br>
    {config['alcaldia']['direccion']} | {config['alcaldia']['telefono_principal']}
    </div>
    """, unsafe_allow_html=True)

# ============================================
# INICIALIZACIÓN
# ============================================
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        st.error(f"❌ Error en el sistema: {str(e)}")
        st.info("Si el problema persiste, contacte al área de sistemas.")