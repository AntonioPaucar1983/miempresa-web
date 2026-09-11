import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import base64

# Configuración de la página
st.set_page_config(
    page_title="Consultores Enterprise. S. A. - Consultoría Moderna",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inicializar tema
if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

# Paletas de colores modernas
LIGHT_MODE = {
    "bg_primary": "#ffffff",
    "bg_secondary": "#f8f9ff",
    "text_primary": "#0f1419",
    "text_secondary": "#64748b",
    "accent_1": "#6366f1",
    "accent_2": "#06b6d4",
    "accent_3": "#8b5cf6",
    "accent_4": "#ec4899",
    "gradient_1": "linear-gradient(135deg, #6366f1 0%, #06b6d4 100%)",
    "gradient_2": "linear-gradient(135deg, #8b5cf6 0%, #ec4899 100%)",
    "gradient_3": "linear-gradient(135deg, #06b6d4 0%, #3b82f6 100%)"
}

DARK_MODE = {
    "bg_primary": "#0f1419",
    "bg_secondary": "#1a1f2e",
    "text_primary": "#f1f5f9",
    "text_secondary": "#cbd5e1",
    "accent_1": "#a78bfa",
    "accent_2": "#38bdf8",
    "accent_3": "#c084fc",
    "accent_4": "#f472b6",
    "gradient_1": "linear-gradient(135deg, #a78bfa 0%, #38bdf8 100%)",
    "gradient_2": "linear-gradient(135deg, #c084fc 0%, #f472b6 100%)",
    "gradient_3": "linear-gradient(135deg, #38bdf8 0%, #60a5fa 100%)"
}

theme = DARK_MODE if st.session_state.dark_mode else LIGHT_MODE

# CSS Ultra Moderno
st.markdown(f"""
    <style>
        * {{
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        :root {{
            --bg-primary: {theme['bg_primary']};
            --bg-secondary: {theme['bg_secondary']};
            --text-primary: {theme['text_primary']};
            --text-secondary: {theme['text_secondary']};
            --accent-1: {theme['accent_1']};
            --accent-2: {theme['accent_2']};
            --accent-3: {theme['accent_3']};
            --accent-4: {theme['accent_4']};
        }}
        
        html, body, [data-testid="stAppViewContainer"] {{
            background-color: {theme['bg_primary']};
            color: {theme['text_primary']};
        }}
        
        [data-testid="stSidebar"] {{
            background-color: {theme['bg_secondary']};
            border-right: 1px solid rgba({theme['accent_1']}, 0.1);
        }}
        
        .main {{
            background-color: {theme['bg_primary']};
        }}
        
        .header-modern {{
            background: {theme['gradient_1']};
            padding: 80px 40px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 50px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
            position: relative;
            overflow: hidden;
        }}
        
        .header-modern h1 {{
            color: white;
            font-size: 3.5em;
            font-weight: 900;
            margin: 0;
            position: relative;
            z-index: 1;
            text-shadow: 0 10px 30px rgba(0,0,0,0.2);
        }}
        
        .header-modern p {{
            color: rgba(255,255,255,0.95);
            font-size: 1.3em;
            margin-top: 15px;
            position: relative;
            z-index: 1;
        }}
        
        .proposito-moderno {{
            background: {theme['gradient_2']};
            padding: 80px 50px;
            border-radius: 20px;
            text-align: center;
            margin: 60px 0;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.15);
            position: relative;
        }}
        
        .proposito-moderno h2 {{
            color: white;
            font-size: 2.8em;
            font-weight: 900;
            margin-bottom: 30px;
            letter-spacing: -1px;
        }}
        
        .proposito-moderno h3 {{
            color: white;
            font-size: 2.2em;
            line-height: 1.8;
            font-weight: 700;
            margin: 0;
        }}
        
        .metric-modern {{
            background: {theme['bg_secondary']};
            padding: 40px;
            border-radius: 16px;
            text-align: center;
            border: 2px solid rgba(99, 102, 241, 0.1);
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            position: relative;
            overflow: hidden;
        }}
        
        .metric-modern:hover {{
            transform: translateY(-20px) scale(1.05);
            border-color: {theme['accent_1']};
            box-shadow: 0 30px 60px rgba(99, 102, 241, 0.2);
        }}
        
        .metric-value {{
            font-size: 56px;
            font-weight: 900;
            color: {theme['accent_1']};
            margin: 20px 0;
            position: relative;
            z-index: 1;
        }}
        
        .metric-label {{
            font-size: 15px;
            color: {theme['text_secondary']};
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
            position: relative;
            z-index: 1;
        }}
        
        .service-modern {{
            background: {theme['bg_secondary']};
            padding: 35px;
            border-radius: 16px;
            border-left: 5px solid;
            margin-bottom: 25px;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
            position: relative;
            overflow: hidden;
        }}
        
        .service-modern:hover {{
            transform: translateX(10px) translateY(-10px);
            box-shadow: 0 20px 50px rgba(99, 102, 241, 0.15);
        }}
        
        .service-modern h3 {{
            margin-top: 0;
            font-size: 1.4em;
            font-weight: 700;
            margin-bottom: 15px;
        }}
        
        .service-modern p {{
            color: {theme['text_secondary']};
            line-height: 1.7;
            margin: 0;
        }}
        
        .news-modern {{
            background: {theme['bg_secondary']};
            padding: 30px;
            border-radius: 16px;
            margin-bottom: 20px;
            border-top: 4px solid {theme['accent_2']};
            transition: all 0.3s ease;
        }}
        
        .news-modern:hover {{
            transform: translateY(-8px);
            box-shadow: 0 15px 40px rgba(34, 211, 238, 0.15);
        }}
        
        .news-modern h3 {{
            margin-top: 0;
            font-size: 1.3em;
            color: {theme['text_primary']};
        }}
        
        .news-meta {{
            font-size: 0.9em;
            color: {theme['text_secondary']};
            margin: 15px 0;
        }}
        
        .section-title-modern {{
            font-size: 2.8em;
            font-weight: 900;
            text-align: center;
            margin: 60px 0 20px 0;
            color: {theme['accent_1']};
            letter-spacing: -1px;
        }}
        
        .section-subtitle-modern {{
            font-size: 1.2em;
            text-align: center;
            color: {theme['text_secondary']};
            margin-bottom: 50px;
            font-weight: 500;
        }}
        
        .divider-modern {{
            height: 3px;
            background: {theme['gradient_1']};
            margin: 60px 0;
            border-radius: 2px;
            opacity: 0.5;
        }}
        
        .cta-section {{
            background: {theme['gradient_1']};
            padding: 60px 40px;
            border-radius: 20px;
            text-align: center;
            margin: 60px 0;
            color: white;
            position: relative;
            overflow: hidden;
        }}
        
        .cta-section h3 {{
            position: relative;
            z-index: 1;
            font-size: 2em;
            margin-top: 0;
        }}
        
        .cta-section p {{
            position: relative;
            z-index: 1;
            font-size: 1.1em;
            opacity: 0.95;
        }}
    </style>
""", unsafe_allow_html=True)

# Botón Dark Mode
with st.sidebar:
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🌙" if not st.session_state.dark_mode else "☀️"):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()
    
    with col1:
        st.markdown(f"""
            <div style="text-align: center; padding: 20px 0;">
                <h2 style="color: {theme['accent_1']}; margin: 0; font-size: 1.8em;">CE</h2>
                <p style="color: {theme['text_secondary']}; font-size: 0.85em;">Moderna</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()

# Navegación
pagina = st.sidebar.radio(
    "Navegación",
    ["🏠 Inicio", "ℹ️ Nosotros", "💼 Servicios", "📰 Noticias", "📧 Contacto"],
    label_visibility="collapsed"
)

# ==================== PÁGINA: INICIO ====================
if pagina == "🏠 Inicio":
    st.markdown(f"""
        <div class="header-modern">
            <h1>Consultores Enterprise</h1>
            <p>Consultoría Gerencial Moderna</p>
        </div>
    """, unsafe_allow_html=True)
    
    fotos = ["fotos/fotoInicio.jpg", "fotos/fotoInicio1.jpg", "fotos/fotoInicio2.jpg", "fotos/fotoInicio3.jpg", "fotos/fotoInicio4.jpg"]
    
    carousel_html = f"""
    <style>
        .carousel {{
            position: relative;
            width: 100%;
            margin: 50px auto;
            overflow: hidden;
            border-radius: 20px;
            box-shadow: 0 30px 80px rgba(99, 102, 241, 0.2);
            max-height: 500px;
        }}
        .carousel-inner {{
            display: flex;
            animation: slide 25s infinite;
        }}
        .carousel-item {{
            min-width: 100%;
            flex: 0 0 100%;
        }}
        .carousel-item img {{
            width: 100%;
            height: 500px;
            object-fit: cover;
        }}
        @keyframes slide {{
            0%,20% {{ transform: translateX(0); }}
            25%,45% {{ transform: translateX(-100%); }}
            50%,70% {{ transform: translateX(-200%); }}
            75%,95% {{ transform: translateX(-300%); }}
            100% {{ transform: translateX(-400%); }}
        }}
        .carousel-counter {{
            position: absolute;
            bottom: 25px;
            left: 50%;
            transform: translateX(-50%);
            background: {theme['gradient_1']};
            color: white;
            padding: 12px 25px;
            border-radius: 50px;
            font-weight: 700;
            z-index: 10;
        }}
    </style>
    <div class="carousel">
        <div class="carousel-inner">
    """
    
    for foto in fotos:
        try:
            with open(foto, "rb") as f:
                carousel_html += f'<div class="carousel-item"><img src="data:image/jpeg;base64,{base64.b64encode(f.read()).decode()}"></div>'
        except:
            carousel_html += f'<div class="carousel-item" style="background:{theme["bg_secondary"]}"></div>'
    
    carousel_html += '</div><div class="carousel-counter">Galería • 5 fotos</div></div>'
    st.markdown(carousel_html, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="proposito-moderno">
            <h2>PROPÓSITO</h2>
            <h3>"ASESORAMOS TUS SUEÑOS<br>IMPULSAMOS TUS PROYECTOS<br>TRANSFORMAMOS TU EMPRESA"</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<h2 class="section-title-modern">Desempeño 2024</h2>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown(f"""
            <div class="metric-modern">
                <div class="metric-label">📊 Proyectos</div>
                <div class="metric-value">45+</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-modern">
                <div class="metric-label">😊 Clientes</div>
                <div class="metric-value">32</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="metric-modern">
                <div class="metric-label">📈 Experiencia</div>
                <div class="metric-value">12</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.markdown('<div class="divider-modern"></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        fig = go.Figure(data=[go.Bar(x=['2020','2021','2022','2023','2024'], y=[8,12,15,18,45], marker_color=theme['accent_1'])])
        fig.update_layout(title="Crecimiento", template="plotly_dark" if st.session_state.dark_mode else "plotly_white", showlegend=False, height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = go.Figure(data=[go.Pie(labels=['Manufactura','Servicios','Educación','Público','Comercio'], values=[8,10,6,5,3])])
        fig.update_layout(title="Sectores", height=350)
        st.plotly_chart(fig, use_container_width=True)
    
    st.markdown(f"""
        <div class="cta-section">
            <h3>Transformemos tu empresa juntos</h3>
            <p>Descubre cómo nuestras soluciones impulsan el crecimiento</p>
        </div>
    """, unsafe_allow_html=True)

elif pagina == "ℹ️ Nosotros":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f"<div class='header-modern'><h1>Consultores Enterprise</h1></div>", unsafe_allow_html=True)
    tab1, tab2, tab3, tab4 = st.tabs(["Historia", "Misión", "Visión", "Valores"])
    with tab1:
        st.write("Fundada en 2012, somos líderes en consultoría gerencial con presencia en principales ciudades del Ecuador.")
    with tab2:
        st.write("Proporcionar soluciones integrales que mejoren competitividad y eficiencia operacional.")
    with tab3:
        st.write("Ser el socio estratégico preferido de empresas ecuatorianas.")
    with tab4:
        st.write("**Integridad • Excelencia • Innovación • Responsabilidad • Colaboración**")

elif pagina == "💼 Servicios":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f'<h2 class="section-title-modern">Servicios</h2>', unsafe_allow_html=True)
    st.markdown('<div class="divider-modern"></div>', unsafe_allow_html=True)
    
    servicios = [
        {"titulo": "🔍 Diagnóstico Empresarial", "color": theme['accent_1']},
        {"titulo": "📋 Administración de Proyectos", "color": theme['accent_2']},
        {"titulo": "🎯 Planificación Estratégica", "color": theme['accent_3']},
        {"titulo": "⚙️ Optimización de Procesos", "color": theme['accent_4']},
        {"titulo": "🔄 Gestión del Cambio", "color": theme['accent_1']},
        {"titulo": "📚 Capacitación Ejecutiva", "color": theme['accent_2']}
    ]
    
    for s in servicios:
        st.markdown(f'<div class="service-modern" style="border-left-color:{s["color"]}"><h3 style="color:{s["color"]}">{s["titulo"]}</h3><p>Soluciones innovadoras y profesionales</p></div>', unsafe_allow_html=True)

elif pagina == "📰 Noticias":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f'<h2 class="section-title-modern">Noticias</h2>', unsafe_allow_html=True)
    st.markdown('<div class="divider-modern"></div>', unsafe_allow_html=True)
    
    for i in range(4):
        st.markdown(f'<div class="news-modern"><h3>Noticia {i+1}</h3><div class="news-meta">Reciente</div></div>', unsafe_allow_html=True)

elif pagina == "📧 Contacto":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f'<div class="header-modern"><h1>Contáctanos</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Quito** • +593 2 XXXX-XXXX\n**Guayaquil** • +593 4 XXXX-XXXX\n**Cuenca** • +593 7 XXXX-XXXX")
    with col2:
        with st.form("contacto"):
            st.text_input("Nombre")
            st.text_input("Email")
            st.text_area("Mensaje")
            st.form_submit_button("Enviar", use_container_width=True)

st.divider()
st.markdown(f'<div style="text-align:center;color:{theme["text_secondary"]};padding:20px">© 2024 Consultores Enterprise • Dark Mode Enabled</div>', unsafe_allow_html=True)
