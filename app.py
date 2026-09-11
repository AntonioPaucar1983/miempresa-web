import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import base64

st.set_page_config(
    page_title="Consultores Enterprise. S. A.",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

LIGHT_MODE = {
    "bg_primary": "#ffffff",
    "bg_secondary": "#f8f9ff",
    "text_primary": "#0f1419",
    "text_secondary": "#64748b",
    "accent_1": "#6366f1",
    "accent_2": "#06b6d4",
    "accent_3": "#8b5cf6",
    "accent_4": "#ec4899"
}

DARK_MODE = {
    "bg_primary": "#0f1419",
    "bg_secondary": "#1a1f2e",
    "text_primary": "#ffffff",
    "text_secondary": "#e2e8f0",
    "accent_1": "#c4b5fd",
    "accent_2": "#67e8f9",
    "accent_3": "#d8b4fe",
    "accent_4": "#f472b6"
}

theme = DARK_MODE if st.session_state.dark_mode else LIGHT_MODE

st.markdown(f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800;900&family=Inter:wght@300;400;500;600;700&display=swap');
        
        * {{
            font-family: 'Inter', 'Poppins', sans-serif;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        
        html, body {{
            background-color: {theme['bg_primary']};
            color: {theme['text_primary']};
        }}
        
        [data-testid="stAppViewContainer"] {{
            background-color: {theme['bg_primary']};
            color: {theme['text_primary']};
        }}
        
        [data-testid="stSidebar"] {{
            background-color: {theme['bg_secondary']};
        }}
        
        h1, h2, h3, h4, h5, h6 {{
            font-family: 'Poppins', sans-serif;
            font-weight: 700;
            color: {theme['text_primary']};
        }}
        
        p, span, div {{
            color: {theme['text_primary']};
        }}
        
        .header-modern {{
            background: linear-gradient(135deg, {theme['accent_1']} 0%, {theme['accent_2']} 100%);
            padding: 60px 40px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 50px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
        }}
        
        .header-modern h1 {{
            font-size: 3.2em;
            font-weight: 900;
            margin: 0;
            color: white;
            text-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }}
        
        .header-modern p {{
            color: rgba(255,255,255,0.95);
            font-size: 1.2em;
            margin-top: 10px;
            font-weight: 500;
        }}
        
        @media (max-width: 768px) {{
            .header-modern h1 {{
                font-size: 2em;
            }}
            .header-modern p {{
                font-size: 1em;
            }}
            .header-modern {{
                padding: 40px 20px;
                margin-bottom: 30px;
            }}
        }}
        
        .proposito-moderno {{
            background: linear-gradient(135deg, {theme['accent_3']} 0%, {theme['accent_4']} 100%);
            padding: 60px 40px;
            border-radius: 20px;
            text-align: center;
            margin: 60px 0;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.15);
        }}
        
        .proposito-moderno h2 {{
            color: white;
            font-size: 2.5em;
            font-weight: 900;
            margin-bottom: 30px;
        }}
        
        .proposito-moderno h3 {{
            color: white;
            font-size: 1.8em;
            line-height: 1.6;
            font-weight: 700;
            margin: 0;
        }}
        
        @media (max-width: 768px) {{
            .proposito-moderno {{
                padding: 40px 20px;
                margin: 40px 0;
            }}
            .proposito-moderno h2 {{
                font-size: 1.8em;
            }}
            .proposito-moderno h3 {{
                font-size: 1.3em;
            }}
        }}
        
        .metric-modern {{
            background: {theme['bg_secondary']};
            padding: 35px;
            border-radius: 16px;
            border: 2px solid {theme['accent_1']};
            text-align: center;
            transition: all 0.4s ease;
        }}
        
        .metric-modern:hover {{
            transform: translateY(-15px);
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.15);
            border-color: {theme['accent_2']};
        }}
        
        .metric-value {{
            font-size: 52px;
            font-weight: 900;
            color: {theme['accent_1']};
            margin: 15px 0;
            font-family: 'Poppins', sans-serif;
        }}
        
        .metric-label {{
            font-size: 14px;
            color: {theme['text_secondary']};
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}
        
        @media (max-width: 768px) {{
            .metric-modern {{
                padding: 20px;
            }}
            .metric-value {{
                font-size: 38px;
            }}
            .metric-label {{
                font-size: 12px;
            }}
        }}
        
        .service-modern {{
            background: {theme['bg_secondary']};
            padding: 30px;
            border-radius: 16px;
            border-left: 5px solid;
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }}
        
        .service-modern:hover {{
            transform: translateX(8px) translateY(-8px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        }}
        
        .service-modern h3 {{
            margin-top: 0;
            font-size: 1.3em;
            font-weight: 700;
            margin-bottom: 10px;
        }}
        
        .service-modern p {{
            font-size: 0.95em;
            line-height: 1.6;
            margin: 0;
            color: {theme['text_secondary']};
        }}
        
        @media (max-width: 768px) {{
            .service-modern {{
                padding: 20px;
            }}
            .service-modern h3 {{
                font-size: 1.1em;
            }}
            .service-modern p {{
                font-size: 0.9em;
            }}
        }}
        
        .project-modern {{
            background: {theme['bg_secondary']};
            padding: 30px;
            border-radius: 16px;
            margin-bottom: 20px;
            border-top: 4px solid {theme['accent_2']};
            transition: all 0.3s ease;
        }}
        
        .project-modern:hover {{
            transform: translateY(-8px);
            box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
        }}
        
        .project-modern h3 {{
            margin-top: 0;
            font-size: 1.3em;
            color: {theme['text_primary']};
            font-weight: 700;
        }}
        
        .project-meta {{
            font-size: 0.9em;
            color: {theme['text_secondary']};
            margin: 10px 0;
        }}
        
        @media (max-width: 768px) {{
            .project-modern {{
                padding: 20px;
            }}
            .project-modern h3 {{
                font-size: 1.1em;
            }}
        }}
        
        .section-title {{
            font-size: 2.8em;
            font-weight: 900;
            text-align: center;
            margin: 50px 0 15px 0;
            color: {theme['accent_1']};
        }}
        
        .section-subtitle {{
            font-size: 1.1em;
            text-align: center;
            color: {theme['text_secondary']};
            margin-bottom: 40px;
            font-weight: 500;
        }}
        
        @media (max-width: 768px) {{
            .section-title {{
                font-size: 1.8em;
                margin: 30px 0 10px 0;
            }}
            .section-subtitle {{
                font-size: 0.95em;
                margin-bottom: 25px;
            }}
        }}
        
        .cta-section {{
            background: linear-gradient(135deg, {theme['accent_1']} 0%, {theme['accent_2']} 100%);
            padding: 50px 40px;
            border-radius: 20px;
            text-align: center;
            margin: 50px 0;
            color: white;
        }}
        
        .cta-section h3 {{
            font-size: 1.8em;
            margin-top: 0;
            margin-bottom: 10px;
            color: white;
        }}
        
        .cta-section p {{
            font-size: 1.05em;
            opacity: 0.95;
            color: white;
            margin: 0;
        }}
        
        @media (max-width: 768px) {{
            .cta-section {{
                padding: 35px 20px;
                margin: 35px 0;
            }}
            .cta-section h3 {{
                font-size: 1.4em;
            }}
            .cta-section p {{
                font-size: 0.95em;
            }}
        }}
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🌙" if not st.session_state.dark_mode else "☀️"):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()
    
    with col1:
        st.markdown(f"""
            <div style="text-align: center; padding: 20px 0;">
                <h2 style="color: {theme['accent_1']}; margin: 0; font-size: 1.6em;">CE</h2>
                <p style="color: {theme['text_secondary']}; font-size: 0.8em; margin: 0;">Moderna</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()

pagina = st.sidebar.radio(
    "Navegación",
    ["🏠 Inicio", "ℹ️ Nosotros", "💼 Servicios", "🚀 Proyectos", "📧 Contacto"],
    label_visibility="collapsed"
)

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
            margin: 40px auto;
            overflow: hidden;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
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
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 10px 20px;
            border-radius: 50px;
            font-weight: 600;
            z-index: 10;
            font-size: 0.9em;
        }}
        @media (max-width: 768px) {{
            .carousel {{
                max-height: 300px;
                margin: 20px auto;
            }}
            .carousel-item img {{
                height: 300px;
            }}
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
            carousel_html += f'<div class="carousel-item" style="background:{theme["bg_secondary"]};display:flex;align-items:center;justify-content:center;"><p style="color:{theme["text_secondary"]}">Imagen no encontrada</p></div>'
    
    carousel_html += '</div><div class="carousel-counter">Galería • 5 fotos</div></div>'
    st.markdown(carousel_html, unsafe_allow_html=True)
    
    st.markdown(f"""
        <div class="proposito-moderno">
            <h2>NUESTRO PROPÓSITO</h2>
            <h3>"ASESORAMOS TUS SUEÑOS<br>IMPULSAMOS TUS PROYECTOS<br>TRANSFORMAMOS TU EMPRESA"</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown(f'<h2 class="section-title">Desempeño 2024</h2>', unsafe_allow_html=True)
    
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
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        fig = go.Figure(data=[go.Bar(x=['2020','2021','2022','2023','2024'], y=[8,12,15,18,45], marker_color=theme['accent_1'], text=['8','12','15','18','45'], textposition='outside')])
        fig.update_layout(title="Crecimiento de Proyectos", template="plotly_dark" if st.session_state.dark_mode else "plotly_white", showlegend=False, height=350, font=dict(family="Poppins", color=theme['text_primary']))
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        fig = go.Figure(data=[go.Pie(labels=['Manufactura','Servicios','Educación','Público','Comercio'], values=[8,10,6,5,3], marker=dict(colors=[theme['accent_1'], theme['accent_2'], theme['accent_3'], theme['accent_4'], theme['accent_1']]))])
        fig.update_layout(title="Clientes por Sector", height=350, font=dict(family="Poppins", color=theme['text_primary']))
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
        st.markdown(f"<p style='font-size:1.05em; color:{theme['text_primary']};'>Fundada en 2012, somos líderes en consultoría gerencial con presencia en principales ciudades del Ecuador.</p>", unsafe_allow_html=True)
    with tab2:
        st.markdown(f"<p style='font-size:1.05em; color:{theme['text_primary']};'>Proporcionar soluciones integrales que mejoren competitividad y eficiencia operacional.</p>", unsafe_allow_html=True)
    with tab3:
        st.markdown(f"<p style='font-size:1.05em; color:{theme['text_primary']};'>Ser el socio estratégico preferido de empresas ecuatorianas.</p>", unsafe_allow_html=True)
    with tab4:
        st.markdown(f"<p style='font-size:1.05em; color:{theme['text_primary']}; line-height:2;'><strong>Integridad</strong> • <strong>Excelencia</strong> • <strong>Innovación</strong><br><strong>Responsabilidad</strong> • <strong>Colaboración</strong> • <strong>Sostenibilidad</strong></p>", unsafe_allow_html=True)
    
    st.divider()
    st.markdown(f"<h2 class='section-title'>Nuestro Equipo</h2>", unsafe_allow_html=True)
    st.markdown(f"<p class='section-subtitle'>Profesionales comprometidos con tu éxito</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    equipo = [
        {
            "archivo": "https://images.unsplash.com/photo-1560264357-8d9766d45b4f?w=500&q=80",
            "titulo": "Liderazgo Ejecutivo",
            "desc": "Nuestros gerentes aportan visión estratégica y experiencia comprobada. Con más de 15 años en consultoría, dirigen cada proyecto con excelencia y compromiso hacia resultados transformadores para tu empresa.",
            "tipo": "url"
        },
        {
            "archivo": "https://images.unsplash.com/photo-1581092162562-40038f81b11c?w=500&q=80",
            "titulo": "Ingeniería de Soluciones",
            "desc": "Ingenieros especializados que diseñan y ejecutan soluciones complejas. Combinan metodologías avanzadas con innovación tecnológica para resolver los desafíos más exigentes de tu negocio.",
            "tipo": "url"
        },
        {
            "archivo": "fotos/consultoras.jpg",
            "titulo": "Consultoría Especializada",
            "desc": "Consultores con expertise en diversos sectores económicos. Aportan perspectivas frescas y estrategias probadas que aceleran la transformación y crecimiento de tu organización.",
            "tipo": "local"
        }
    ]
    
    cols = [col1, col2, col3]
    
    for idx, (col, person) in enumerate(zip(cols, equipo)):
        with col:
            try:
                # Si es URL de internet
                if person["tipo"] == "url":
                    st.markdown(f"""
                        <div style="
                            background: {theme['bg_secondary']};
                            border-radius: 16px;
                            overflow: hidden;
                            border: 2px solid {theme['accent_1']};
                            transition: all 0.3s ease;
                        ">
                            <img src="{person['archivo']}" style="width:100%; height:300px; object-fit:cover;">
                            <div style="padding: 25px;">
                                <h3 style="color: {theme['accent_1']}; margin-top: 0; font-size: 1.2em;">{person['titulo']}</h3>
                                <p style="color: {theme['text_secondary']}; line-height: 1.6; margin: 0; font-size: 0.95em;">{person['desc']}</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                # Si es archivo local
                else:
                    with open(person["archivo"], "rb") as f:
                        img_data = base64.b64encode(f.read()).decode()
                        st.markdown(f"""
                            <div style="
                                background: {theme['bg_secondary']};
                                border-radius: 16px;
                                overflow: hidden;
                                border: 2px solid {theme['accent_1']};
                                transition: all 0.3s ease;
                            ">
                                <img src="data:image/jpeg;base64,{img_data}" style="width:100%; height:300px; object-fit:cover;">
                                <div style="padding: 25px;">
                                    <h3 style="color: {theme['accent_1']}; margin-top: 0; font-size: 1.2em;">{person['titulo']}</h3>
                                    <p style="color: {theme['text_secondary']}; line-height: 1.6; margin: 0; font-size: 0.95em;">{person['desc']}</p>
                                </div>
                            </div>
                        """, unsafe_allow_html=True)
            except:
                st.markdown(f"""
                    <div style="
                        background: {theme['bg_secondary']};
                        border-radius: 16px;
                        padding: 40px;
                        border: 2px solid {theme['accent_1']};
                        text-align: center;
                    ">
                        <p style="color: {theme['text_secondary']};">📷 Imagen no encontrada</p>
                        <h3 style="color: {theme['accent_1']}; margin-top: 15px;">{person['titulo']}</h3>
                        <p style="color: {theme['text_secondary']}; font-size: 0.9em;">{person['desc']}</p>
                    </div>
                """, unsafe_allow_html=True)

elif pagina == "💼 Servicios":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f'<h2 class="section-title">Nuestros Servicios</h2>', unsafe_allow_html=True)
    st.divider()
    
    servicios = [
        {"titulo": "🔍 Diagnóstico Empresarial", "color": theme['accent_1'], "desc": "Evaluación integral para identificar oportunidades"},
        {"titulo": "📋 Administración de Proyectos", "color": theme['accent_2'], "desc": "Gestión profesional con metodologías PMI/PMBOK"},
        {"titulo": "🎯 Planificación Estratégica", "color": theme['accent_3'], "desc": "Estrategias claras para crecimiento sostenible"},
        {"titulo": "⚙️ Optimización de Procesos", "color": theme['accent_4'], "desc": "Mejora continua para eficiencia y reducción de costos"},
        {"titulo": "🔄 Gestión del Cambio", "color": theme['accent_1'], "desc": "Transformación organizacional y cultural"},
        {"titulo": "📚 Capacitación Ejecutiva", "color": theme['accent_2'], "desc": "Programas personalizados para líderes"}
    ]
    
    for s in servicios:
        st.markdown(f'<div class="service-modern" style="border-left-color:{s["color"]}"><h3 style="color:{s["color"]}">{s["titulo"]}</h3><p>{s["desc"]}</p></div>', unsafe_allow_html=True)

elif pagina == "🚀 Proyectos":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f'<h2 class="section-title">Nuestros Proyectos</h2>', unsafe_allow_html=True)
    st.markdown(f'<p class="section-subtitle">Casos de éxito y transformaciones realizadas</p>', unsafe_allow_html=True)
    st.divider()
    
    proyectos = [
        {"titulo": "Manufactura: Aumento 45% de Productividad", "fecha": "Ago 2024", "desc": "Empresa manufacturera en Cuenca logró aumentar productividad significativamente"},
        {"titulo": "Servicios: Optimización de Procesos", "fecha": "Jul 2024", "desc": "Reducción de tiempos operacionales en 35% mediante reingeniería"},
        {"titulo": "Educación: Transformación Digital", "fecha": "Jun 2024", "desc": "Centro educativo implementó sistema integral de gestión digital"},
        {"titulo": "Comercio: Estrategia de Expansión", "fecha": "May 2024", "desc": "Empresa comercial expandió operaciones a 3 nuevas ciudades"}
    ]
    
    for p in proyectos:
        st.markdown(f"""
            <div class="project-modern">
                <h3>{p['titulo']}</h3>
                <div class="project-meta">📅 {p['fecha']}</div>
                <p style="color:{theme['text_secondary']}; margin-bottom:0;">{p['desc']}</p>
            </div>
        """, unsafe_allow_html=True)

elif pagina == "📧 Contacto":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f'<div class="header-modern"><h1>Contáctanos</h1></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
            <h3 style="color:{theme['text_primary']}; margin-top:0;">📍 Ubicaciones</h3>
            <p style="color:{theme['text_secondary']}; font-size:0.95em;"><strong>Quito</strong><br>Av. Amazonas • +593 2 XXXX-XXXX</p>
            <p style="color:{theme['text_secondary']}; font-size:0.95em;"><strong>Guayaquil</strong><br>Parque Empresarial • +593 4 XXXX-XXXX</p>
            <p style="color:{theme['text_secondary']}; font-size:0.95em;"><strong>Cuenca</strong><br>Av. Gran Colombia • +593 7 XXXX-XXXX</p>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"<h3 style='color:{theme['text_primary']}; margin-top:0;'>📧 Formulario</h3>", unsafe_allow_html=True)
        with st.form("contacto"):
            st.text_input("Nombre", label_visibility="collapsed", placeholder="Tu nombre")
            st.text_input("Email", label_visibility="collapsed", placeholder="Tu email")
            st.text_area("Mensaje", height=120, label_visibility="collapsed", placeholder="Tu mensaje")
            st.form_submit_button("Enviar Mensaje", use_container_width=True)

st.divider()
st.markdown(f'<div style="text-align:center;color:{theme["text_secondary"]};padding:20px;font-size:0.9em;">© 2024 Consultores Enterprise • Dark Mode ✓</div>', unsafe_allow_html=True)
