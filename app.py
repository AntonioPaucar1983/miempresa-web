import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import base64
import random

st.set_page_config(
    page_title="Consultores Enterprise. S. A.",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

if 'dark_mode' not in st.session_state:
    st.session_state.dark_mode = False

if 'visitas' not in st.session_state:
    st.session_state.visitas = 200

if 'usuarios_online' not in st.session_state:
    st.session_state.usuarios_online = random.randint(10, 25)

# Incrementar visitas
st.session_state.visitas += 1
# Variar usuarios en línea
if random.random() > 0.7:
    st.session_state.usuarios_online = random.randint(10, 25)

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
        
        @keyframes slideInDown {{
            from {{
                opacity: 0;
                transform: translateY(-30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @keyframes slideInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @keyframes fadeInScale {{
            from {{
                opacity: 0;
                transform: scale(0.9);
            }}
            to {{
                opacity: 1;
                transform: scale(1);
            }}
        }}
        
        @keyframes pulse {{
            0% {{
                transform: scale(1);
                opacity: 1;
            }}
            50% {{
                transform: scale(1.05);
                opacity: 0.8;
            }}
            100% {{
                transform: scale(1);
                opacity: 1;
            }}
        }}
        
        @keyframes glow {{
            0%, 100% {{
                box-shadow: 0 0 10px rgba({theme['accent_1']}, 0.3);
            }}
            50% {{
                box-shadow: 0 0 20px rgba({theme['accent_1']}, 0.6);
            }}
        }}
        
        @keyframes countUp {{
            from {{
                opacity: 0;
                transform: translateY(-10px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @keyframes float {{
            0%, 100% {{
                transform: translateY(0px);
            }}
            50% {{
                transform: translateY(-10px);
            }}
        }}
        
        .header-modern {{
            background: linear-gradient(135deg, {theme['accent_1']} 0%, {theme['accent_2']} 100%);
            padding: 80px 40px;
            border-radius: 20px;
            text-align: center;
            margin-bottom: 50px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
            animation: slideInDown 0.8s ease-out;
            position: relative;
            overflow: hidden;
        }}
        
        .header-modern::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 30% 50%, rgba(255,255,255,0.1), transparent);
            pointer-events: none;
        }}
        
        .header-modern h1 {{
            font-size: 3.2em;
            font-weight: 900;
            margin: 0;
            color: white;
            text-shadow: 0 5px 15px rgba(0,0,0,0.2);
            position: relative;
            z-index: 1;
            animation: slideInDown 1s ease-out;
        }}
        
        .header-modern p {{
            color: rgba(255,255,255,0.95);
            font-size: 1.2em;
            margin-top: 10px;
            font-weight: 500;
            position: relative;
            z-index: 1;
            animation: slideInUp 1s ease-out 0.2s backwards;
        }}
        
        .stats-bar {{
            display: flex;
            gap: 30px;
            justify-content: center;
            margin: 30px 0;
            animation: slideInUp 1s ease-out 0.4s backwards;
        }}
        
        .stat-item {{
            background: {theme['bg_secondary']};
            padding: 20px 30px;
            border-radius: 12px;
            border: 2px solid {theme['accent_1']};
            text-align: center;
            animation: fadeInScale 0.8s ease-out;
            transition: all 0.3s ease;
        }}
        
        .stat-item:hover {{
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba({theme['accent_1']}, 0.2);
            border-color: {theme['accent_2']};
        }}
        
        .stat-number {{
            font-size: 32px;
            font-weight: 900;
            background: linear-gradient(135deg, {theme['accent_1']}, {theme['accent_2']});
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: countUp 1s ease-out;
        }}
        
        .stat-label {{
            font-size: 12px;
            color: {theme['text_secondary']};
            font-weight: 600;
            text-transform: uppercase;
            margin-top: 8px;
            letter-spacing: 1px;
        }}
        
        .online-badge {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
            padding: 8px 16px;
            border-radius: 50px;
            font-size: 13px;
            font-weight: 600;
            animation: pulse 2s infinite;
        }}
        
        .online-dot {{
            width: 8px;
            height: 8px;
            background: #10b981;
            border-radius: 50%;
            animation: pulse 2s infinite;
        }}
        
        .proposito-moderno {{
            background: linear-gradient(135deg, {theme['accent_3']} 0%, {theme['accent_4']} 100%);
            padding: 80px 50px;
            border-radius: 20px;
            text-align: center;
            margin: 60px 0;
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.15);
            animation: slideInUp 1s ease-out;
            position: relative;
            overflow: hidden;
        }}
        
        .proposito-moderno::before {{
            content: '';
            position: absolute;
            top: -50%;
            right: -50%;
            width: 200%;
            height: 200%;
            background: radial-gradient(circle, rgba(255,255,255,0.05) 1px, transparent 1px);
            background-size: 50px 50px;
            animation: float 20s linear infinite;
        }}
        
        .proposito-moderno h2 {{
            color: white;
            font-size: 2.5em;
            font-weight: 900;
            margin-bottom: 30px;
            position: relative;
            z-index: 1;
        }}
        
        .proposito-moderno h3 {{
            color: white;
            font-size: 1.8em;
            line-height: 1.6;
            font-weight: 700;
            margin: 0;
            position: relative;
            z-index: 1;
        }}
        
        .metric-modern {{
            background: {theme['bg_secondary']};
            padding: 35px;
            border-radius: 16px;
            border: 2px solid {theme['accent_1']};
            text-align: center;
            animation: fadeInScale 0.8s ease-out;
            transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
        }}
        
        .metric-modern:hover {{
            transform: translateY(-20px) scale(1.05);
            box-shadow: 0 30px 60px rgba(0, 0, 0, 0.2);
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
        
        .service-modern {{
            background: {theme['bg_secondary']};
            padding: 30px;
            border-radius: 16px;
            border-left: 5px solid;
            margin-bottom: 20px;
            animation: slideInUp 0.6s ease-out;
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
        
        .project-modern {{
            background: {theme['bg_secondary']};
            padding: 30px;
            border-radius: 16px;
            margin-bottom: 20px;
            border-top: 4px solid {theme['accent_2']};
            animation: slideInUp 0.6s ease-out;
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
        
        .section-title {{
            font-size: 2.8em;
            font-weight: 900;
            text-align: center;
            margin: 50px 0 15px 0;
            color: {theme['accent_1']};
            animation: slideInDown 0.8s ease-out;
        }}
        
        .section-subtitle {{
            font-size: 1.1em;
            text-align: center;
            color: {theme['text_secondary']};
            margin-bottom: 40px;
            font-weight: 500;
            animation: slideInUp 0.8s ease-out;
        }}
        
        .cta-section {{
            background: linear-gradient(135deg, {theme['accent_1']} 0%, {theme['accent_2']} 100%);
            padding: 60px 40px;
            border-radius: 20px;
            text-align: center;
            margin: 50px 0;
            color: white;
            animation: slideInUp 1s ease-out;
            position: relative;
            overflow: hidden;
        }}
        
        .cta-section::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: radial-gradient(circle at 30% 50%, rgba(255,255,255,0.1), transparent);
            pointer-events: none;
        }}
        
        .cta-section h3 {{
            font-size: 1.8em;
            margin-top: 0;
            margin-bottom: 10px;
            color: white;
            position: relative;
            z-index: 1;
        }}
        
        .cta-section p {{
            font-size: 1.05em;
            opacity: 0.95;
            color: white;
            margin: 0;
            position: relative;
            z-index: 1;
        }}
        
        @media (max-width: 768px) {{
            .header-modern h1 {{
                font-size: 2em;
            }}
            .header-modern {{
                padding: 40px 20px;
                margin-bottom: 30px;
            }}
            .stats-bar {{
                flex-direction: column;
                gap: 15px;
            }}
        }}
    </style>
""", unsafe_allow_html=True)

with st.sidebar:
    col1, col2 = st.columns([3, 1])
    with col2:
        if st.button("🌙" if not st.session_state.dark_mode else "☀️", key="theme_btn"):
            st.session_state.dark_mode = not st.session_state.dark_mode
            st.rerun()
    
    with col1:
        try:
            with open("fotos/logoEmpresa.jpg", "rb") as logo_file:
                logo_data = base64.b64encode(logo_file.read()).decode()
                st.markdown(f"""
                    <div style="
                        background: {theme['bg_secondary']};
                        border: 2px solid {theme['accent_1']};
                        border-radius: 16px;
                        padding: 20px;
                        text-align: center;
                        animation: slideInDown 0.8s ease-out;
                        transition: all 0.3s ease;
                    ">
                        <img src="data:image/jpeg;base64,{logo_data}" style="
                            width: 160px;
                            height: auto;
                            object-fit: contain;
                            filter: {'brightness(1.3)' if st.session_state.dark_mode else 'brightness(1)'};
                            margin-bottom: 12px;
                            animation: float 3s ease-in-out infinite;
                        ">
                        <p style="
                            color: {theme['text_secondary']};
                            font-size: 0.85em;
                            margin: 8px 0 0 0;
                            font-weight: 500;
                        ">Consultores Enterprise</p>
                    </div>
                """, unsafe_allow_html=True)
        except Exception as e:
            st.markdown(f"""
                <div style="background: {theme['bg_secondary']}; border: 2px solid {theme['accent_1']}; border-radius: 16px; padding: 20px; text-align: center; animation: slideInDown 0.8s ease-out;">
                    <h2 style="color: {theme['accent_1']}; margin: 0; font-size: 1.6em;">CE</h2>
                    <p style="color: {theme['text_secondary']}; font-size: 0.8em; margin: 8px 0 0 0;">Moderna</p>
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
    
    st.markdown(f"""
        <div class="stats-bar">
            <div class="stat-item">
                <div class="stat-number">{st.session_state.visitas}</div>
                <div class="stat-label">Visitas Hoy</div>
            </div>
            <div class="stat-item">
                <div class="online-badge">
                    <div class="online-dot"></div>
                    {st.session_state.usuarios_online}+ En línea
                </div>
            </div>
            <div class="stat-item">
                <div class="stat-number">45+</div>
                <div class="stat-label">Proyectos Activos</div>
            </div>
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
            animation: slideInUp 0.8s ease-out;
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
            "archivo": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=500&q=80",
            "titulo": "Liderazgo Ejecutivo",
            "desc": "Nuestros gerentes aportan visión estratégica y experiencia comprobada.",
            "tipo": "url"
        },
        {
            "archivo": "https://images.unsplash.com/photo-1504384308090-c894fdcc538d?w=500&q=80",
            "titulo": "Ingeniería de Soluciones",
            "desc": "Ingenieros especializados que diseñan y ejecutan soluciones complejas.",
            "tipo": "url"
        },
        {
            "archivo": "fotos/consultoras.jpg",
            "titulo": "Consultoría Especializada",
            "desc": "Consultores con expertise en diversos sectores económicos.",
            "tipo": "local"
        }
    ]
    
    cols = [col1, col2, col3]
    for idx, (col, person) in enumerate(zip(cols, equipo)):
        with col:
            try:
                if person["tipo"] == "url":
                    st.markdown(f"""
                        <div style="
                            background: {theme['bg_secondary']};
                            border-radius: 16px;
                            overflow: hidden;
                            border: 2px solid {theme['accent_1']};
                            animation: fadeInScale 0.8s ease-out;
                        ">
                            <img src="{person['archivo']}" style="width:100%; height:300px; object-fit:cover;">
                            <div style="padding: 25px;">
                                <h3 style="color: {theme['accent_1']}; margin-top: 0; font-size: 1.2em;">{person['titulo']}</h3>
                                <p style="color: {theme['text_secondary']}; line-height: 1.6; margin: 0; font-size: 0.95em;">{person['desc']}</p>
                            </div>
                        </div>
                    """, unsafe_allow_html=True)
                else:
                    with open(person["archivo"], "rb") as f:
                        img_data = base64.b64encode(f.read()).decode()
                        st.markdown(f"""
                            <div style="
                                background: {theme['bg_secondary']};
                                border-radius: 16px;
                                overflow: hidden;
                                border: 2px solid {theme['accent_1']};
                                animation: fadeInScale 0.8s ease-out;
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
                    <div style="background: {theme['bg_secondary']}; border-radius: 16px; padding: 40px; border: 2px solid {theme['accent_1']}; text-align: center;">
                        <p style="color: {theme['text_secondary']};">📷 Imagen no encontrada</p>
                        <h3 style="color: {theme['accent_1']};">{person['titulo']}</h3>
                    </div>
                """, unsafe_allow_html=True)

elif pagina == "💼 Servicios":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f'<h2 class="section-title">Nuestros Servicios</h2>', unsafe_allow_html=True)
    st.divider()
    
    servicios = [
        {"titulo": "🔍 Diagnóstico Empresarial", "color": theme['accent_1'], "desc": "Evaluación integral para identificar oportunidades", "foto": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=300&q=80"},
        {"titulo": "📋 Administración de Proyectos", "color": theme['accent_2'], "desc": "Gestión profesional con metodologías PMI/PMBOK", "foto": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=300&q=80"},
        {"titulo": "🎯 Planificación Estratégica", "color": theme['accent_3'], "desc": "Estrategias claras para crecimiento sostenible", "foto": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=300&q=80"},
        {"titulo": "⚙️ Optimización de Procesos", "color": theme['accent_4'], "desc": "Mejora continua para eficiencia y reducción de costos", "foto": "https://images.unsplash.com/photo-1454165804606-c3d57bc86b40?w=300&q=80"},
        {"titulo": "🔄 Gestión del Cambio", "color": theme['accent_1'], "desc": "Transformación organizacional y cultural", "foto": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=300&q=80"},
        {"titulo": "📚 Capacitación Ejecutiva", "color": theme['accent_2'], "desc": "Programas personalizados para líderes", "foto": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=300&q=80"}
    ]
    
    for s in servicios:
        st.markdown(f'''
            <div class="service-modern" style="border-left-color:{s["color"]}; display: flex; gap: 20px;">
                <div style="flex: 0 0 120px;">
                    <img src="{s["foto"]}" style="width: 120px; height: 100px; object-fit: cover; border-radius: 12px;">
                </div>
                <div style="flex: 1;">
                    <h3 style="color:{s["color"]}; margin-top: 0;">{s["titulo"]}</h3>
                    <p>{s["desc"]}</p>
                </div>
            </div>
        ''', unsafe_allow_html=True)

elif pagina == "🚀 Proyectos":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f'<h2 class="section-title">Nuestros Proyectos</h2>', unsafe_allow_html=True)
    st.markdown(f'<p class="section-subtitle">Casos de éxito y transformaciones realizadas</p>', unsafe_allow_html=True)
    st.divider()
    
    proyectos = [
        {"titulo": "Manufactura: Aumento 45% de Productividad", "fecha": "Ago 2024", "desc": "Empresa manufacturera en Cuenca logró aumentar productividad significativamente", "foto": "https://images.unsplash.com/photo-1565043666747-69f6646db940?w=300&q=80"},
        {"titulo": "Servicios: Optimización de Procesos", "fecha": "Jul 2024", "desc": "Reducción de tiempos operacionales en 35% mediante reingeniería", "foto": "https://images.unsplash.com/photo-1552664730-d307ca884978?w=300&q=80"},
        {"titulo": "Educación: Transformación Digital", "fecha": "Jun 2024", "desc": "Centro educativo implementó sistema integral de gestión digital", "foto": "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=300&q=80"},
        {"titulo": "Comercio: Estrategia de Expansión", "fecha": "May 2024", "desc": "Empresa comercial expandió operaciones a 3 nuevas ciudades", "foto": "https://images.unsplash.com/photo-1556740738-b6a63e27c4df?w=300&q=80"}
    ]
    
    for p in proyectos:
        st.markdown(f"""
            <div class="project-modern" style="display: flex; gap: 20px;">
                <div style="flex: 0 0 120px;">
                    <img src="{p["foto"]}" style="width: 120px; height: 100px; object-fit: cover; border-radius: 12px;">
                </div>
                <div style="flex: 1;">
                    <h3 style="margin-top: 0;">{p['titulo']}</h3>
                    <div class="project-meta">📅 {p['fecha']}</div>
                    <p style="color:{theme['text_secondary']}; margin-bottom:0;">{p['desc']}</p>
                </div>
            </div>
        """, unsafe_allow_html=True)

elif pagina == "📧 Contacto":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    st.markdown(f'<div class="header-modern"><h1>Contáctanos</h1><p>Estamos listos para ayudarte</p></div>', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        st.markdown(f"""
            <h3 style="color:{theme['text_primary']}; margin-top:0; font-size: 1.4em;">📍 Ubicaciones</h3>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="background: {theme['bg_secondary']}; padding: 20px; border-radius: 12px; margin-bottom: 15px; animation: slideInUp 0.6s ease-out;">
                <p style="color:{theme['text_primary']}; font-weight: 700; margin: 0 0 10px 0;"><strong>Quito</strong></p>
                <p style="color:{theme['text_secondary']}; font-size:0.95em; margin: 0;">Av. Amazonas N34-451</p>
                <p style="color:{theme['text_secondary']}; font-size:0.95em; margin: 5px 0 0 0;">📞 +593 2 XXXX-XXXX</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="background: {theme['bg_secondary']}; padding: 20px; border-radius: 12px; margin-bottom: 15px; animation: slideInUp 0.7s ease-out;">
                <p style="color:{theme['text_primary']}; font-weight: 700; margin: 0 0 10px 0;"><strong>Guayaquil</strong></p>
                <p style="color:{theme['text_secondary']}; font-size:0.95em; margin: 0;">Parque Empresarial</p>
                <p style="color:{theme['text_secondary']}; font-size:0.95em; margin: 5px 0 0 0;">📞 +593 4 XXXX-XXXX</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="background: {theme['bg_secondary']}; padding: 20px; border-radius: 12px; margin-bottom: 25px; animation: slideInUp 0.8s ease-out;">
                <p style="color:{theme['text_primary']}; font-weight: 700; margin: 0 0 10px 0;"><strong>Cuenca</strong></p>
                <p style="color:{theme['text_secondary']}; font-size:0.95em; margin: 0;">Av. Gran Colombia</p>
                <p style="color:{theme['text_secondary']}; font-size:0.95em; margin: 5px 0 0 0;">📞 +593 7 XXXX-XXXX</p>
            </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <h3 style="color:{theme['text_primary']}; margin-top:25px; margin-bottom:15px; font-size: 1.2em;">📱 Redes Sociales</h3>
        """, unsafe_allow_html=True)
        
        col_social1, col_social2, col_social3, col_social4 = st.columns(4)
        
        with col_social1:
            st.markdown(f"""
                <a href="https://facebook.com" target="_blank" style="
                    display: inline-block;
                    background: linear-gradient(135deg, {theme['accent_1']} 0%, {theme['accent_2']} 100%);
                    color: white;
                    width: 50px;
                    height: 50px;
                    border-radius: 50%;
                    text-align: center;
                    line-height: 50px;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 24px;
                    transition: all 0.3s ease;
                    animation: fadeInScale 0.6s ease-out;
                ">📘</a>
            """, unsafe_allow_html=True)
        
        with col_social2:
            st.markdown(f"""
                <a href="https://instagram.com" target="_blank" style="
                    display: inline-block;
                    background: linear-gradient(135deg, {theme['accent_3']} 0%, {theme['accent_4']} 100%);
                    color: white;
                    width: 50px;
                    height: 50px;
                    border-radius: 50%;
                    text-align: center;
                    line-height: 50px;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 24px;
                    animation: fadeInScale 0.7s ease-out;
                ">📷</a>
            """, unsafe_allow_html=True)
        
        with col_social3:
            st.markdown(f"""
                <a href="https://linkedin.com" target="_blank" style="
                    display: inline-block;
                    background: linear-gradient(135deg, {theme['accent_2']} 0%, {theme['accent_1']} 100%);
                    color: white;
                    width: 50px;
                    height: 50px;
                    border-radius: 50%;
                    text-align: center;
                    line-height: 50px;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 24px;
                    animation: fadeInScale 0.8s ease-out;
                ">🔗</a>
            """, unsafe_allow_html=True)
        
        with col_social4:
            st.markdown(f"""
                <a href="https://twitter.com" target="_blank" style="
                    display: inline-block;
                    background: linear-gradient(135deg, {theme['accent_1']} 0%, {theme['accent_3']} 100%);
                    color: white;
                    width: 50px;
                    height: 50px;
                    border-radius: 50%;
                    text-align: center;
                    line-height: 50px;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 20px;
                    animation: fadeInScale 0.9s ease-out;
                ">𝕏</a>
            """, unsafe_allow_html=True)
        
        st.markdown(f"""
            <div style="background: linear-gradient(135deg, {theme['accent_2']} 0%, {theme['accent_1']} 100%); padding: 25px; border-radius: 12px; margin-top: 25px; text-align: center; animation: slideInUp 1s ease-out;">
                <p style="color: white; font-size: 1.05em; margin-bottom: 12px;"><strong>💬 Contáctanos por WhatsApp</strong></p>
                <a href="https://wa.me/593XXXXXXXXXX?text=Hola%2C%20me%20interesa%20conocer%20m%C3%A1s%20sobre%20sus%20servicios" target="_blank" style="
                    display: inline-block;
                    background: white;
                    color: {theme['accent_2']};
                    padding: 12px 30px;
                    border-radius: 50px;
                    text-decoration: none;
                    font-weight: 700;
                ">📱 Iniciar Chat</a>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <h3 style="color:{theme['text_primary']}; margin-top:0; font-size: 1.4em;">📧 Formulario de Contacto</h3>
        """, unsafe_allow_html=True)
        
        with st.form("contacto_form"):
            nombre = st.text_input("👤 Nombre Completo", placeholder="Tu nombre", label_visibility="collapsed")
            email = st.text_input("📧 Email", placeholder="tu@email.com", label_visibility="collapsed")
            telefono = st.text_input("📞 Teléfono", placeholder="+593 9 XXXX-XXXX", label_visibility="collapsed")
            empresa = st.text_input("🏢 Empresa", placeholder="Nombre de tu empresa", label_visibility="collapsed")
            asunto = st.selectbox("🎯 Asunto", ["Selecciona un asunto", "Consulta de Servicios", "Diagnóstico Empresarial", "Administración de Proyectos", "Planificación Estratégica", "Otro"], label_visibility="collapsed")
            mensaje = st.text_area("💭 Mensaje", placeholder="Cuéntanos cómo podemos ayudarte...", height=100, label_visibility="collapsed")
            
            col_submit1, col_submit2 = st.columns(2)
            with col_submit1:
                enviado = st.form_submit_button("✉️ Enviar Mensaje", use_container_width=True)
            with col_submit2:
                st.form_submit_button("🔄 Limpiar", use_container_width=True)
            
            if enviado and nombre and email and telefono and mensaje:
                st.success("✅ ¡Mensaje enviado exitosamente! Nos pondremos en contacto pronto.")
            elif enviado and not (nombre and email and telefono and mensaje):
                st.error("⚠️ Por favor completa todos los campos requeridos.")
        
        st.markdown(f"""
            <div style="background: {theme['bg_secondary']}; padding: 20px; border-radius: 12px; margin-top: 20px; border-left: 4px solid {theme['accent_2']};animation: slideInUp 1s ease-out;">
                <p style="color:{theme['text_primary']}; font-weight: 700; margin-top: 0;"><strong>⏰ Horarios de Atención</strong></p>
                <p style="color:{theme['text_secondary']}; font-size: 0.95em; margin: 8px 0;"><strong>Lunes - Viernes:</strong> 8:00 AM - 6:00 PM</p>
                <p style="color:{theme['text_secondary']}; font-size: 0.95em; margin: 8px 0;"><strong>Sábado:</strong> 9:00 AM - 1:00 PM</p>
                <p style="color:{theme['text_secondary']}; font-size: 0.95em; margin: 8px 0 0 0;"><strong>Domingo:</strong> Cerrado</p>
            </div>
        """, unsafe_allow_html=True)

st.divider()

# CHATBOT DE IA FLOTANTE
st.markdown(f"""
    <style>
        .chat-button-container {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            z-index: 100;
        }}
        
        .chat-button {{
            background: linear-gradient(135deg, {theme['accent_1']} 0%, {theme['accent_2']} 100%);
            color: white;
            border: none;
            padding: 14px 24px;
            border-radius: 12px;
            font-size: 16px;
            font-weight: 700;
            cursor: pointer;
            box-shadow: 0 10px 35px rgba(0, 0, 0, 0.3);
            animation: slideInUp 0.6s ease-out;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        
        .chat-button:hover {{
            transform: translateY(-3px);
            box-shadow: 0 15px 45px rgba(0, 0, 0, 0.4);
        }}
        
        .chat-button:active {{
            transform: translateY(-1px);
        }}
        
        .chat-container {{
            position: fixed;
            bottom: 100px;
            right: 30px;
            width: 400px;
            height: 580px;
            background: {theme['bg_secondary']};
            border: 2px solid {theme['accent_1']};
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
            display: flex;
            flex-direction: column;
            z-index: 99;
            animation: slideInUp 0.4s ease-out;
        }}
        
        .chat-header {{
            background: linear-gradient(135deg, {theme['accent_1']} 0%, {theme['accent_2']} 100%);
            color: white;
            padding: 20px;
            border-radius: 18px 18px 0 0;
            text-align: center;
            font-weight: 700;
            font-size: 16px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        
        .close-btn {{
            background: rgba(255, 255, 255, 0.2);
            color: white;
            border: none;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            cursor: pointer;
            font-size: 20px;
            transition: all 0.3s ease;
        }}
        
        .close-btn:hover {{
            background: rgba(255, 255, 255, 0.4);
        }}
        
        .chat-messages {{
            flex: 1;
            overflow-y: auto;
            padding: 20px;
            display: flex;
            flex-direction: column;
            gap: 15px;
        }}
        
        .chat-message {{
            display: flex;
            gap: 10px;
            animation: slideInUp 0.3s ease-out;
        }}
        
        .chat-message.user {{
            justify-content: flex-end;
        }}
        
        .chat-bubble {{
            max-width: 75%;
            padding: 12px 16px;
            border-radius: 12px;
            font-size: 0.9em;
            line-height: 1.4;
            word-wrap: break-word;
        }}
        
        .chat-message.assistant .chat-bubble {{
            background: {theme['bg_primary']};
            color: {theme['text_primary']};
            border-left: 3px solid {theme['accent_2']};
        }}
        
        .chat-message.user .chat-bubble {{
            background: linear-gradient(135deg, {theme['accent_1']}, {theme['accent_2']});
            color: white;
            border-radius: 12px 0 12px 12px;
        }}
        
        .chat-input-area {{
            padding: 15px;
            border-top: 1px solid rgba({theme['accent_1']}, 0.2);
            display: flex;
            gap: 10px;
        }}
        
        .chat-input {{
            flex: 1;
            padding: 10px 15px;
            border: 1px solid {theme['accent_1']};
            border-radius: 8px;
            background: {theme['bg_primary']};
            color: {theme['text_primary']};
            font-size: 0.9em;
            font-family: inherit;
        }}
        
        .chat-input:focus {{
            outline: none;
            border-color: {theme['accent_2']};
            box-shadow: 0 0 10px rgba({theme['accent_2']}, 0.3);
        }}
        
        .chat-send {{
            background: linear-gradient(135deg, {theme['accent_1']}, {theme['accent_2']});
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }}
        
        .chat-send:hover {{
            transform: scale(1.05);
            box-shadow: 0 5px 15px rgba({theme['accent_1']}, 0.3);
        }}
        
        @media (max-width: 500px) {{
            .chat-container {{
                width: calc(100vw - 20px);
                height: 400px;
                bottom: 100px;
                right: 10px;
            }}
            
            .chat-button {{
                padding: 12px 20px;
                font-size: 14px;
            }}
        }}
    </style>
""", unsafe_allow_html=True)

# Sistema de chat con JavaScript para manejar el modal
st.markdown(f"""
    <div class="chat-button-container">
        <button class="chat-button" onclick="document.getElementById('chatModal').style.display = document.getElementById('chatModal').style.display === 'flex' ? 'none' : 'flex'">
            💬 Chat Bot
        </button>
        
        <div id="chatModal" style="display: none; position: fixed; bottom: 100px; right: 30px; width: 400px; height: 580px; background: {theme['bg_secondary']}; border: 2px solid {theme['accent_1']}; border-radius: 20px; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3); flex-direction: column; z-index: 99; animation: slideInUp 0.4s ease-out;">
            <div class="chat-header">
                🤖 Asistente IA
                <button class="close-btn" onclick="document.getElementById('chatModal').style.display='none'">✕</button>
            </div>
            
            <div class="chat-messages" id="chatMessages"></div>
            
            <div class="chat-input-area">
                <input type="text" class="chat-input" id="userInput" placeholder="Escribe tu pregunta..." onkeypress="if(event.key==='Enter') sendMessage()">
                <button class="chat-send" onclick="sendMessage()">Enviar</button>
            </div>
        </div>
    </div>
    
    <script>
        // Respuestas del chatbot
        const respuestas = {{
            "diagnóstico": "Nuestro Diagnóstico Empresarial es una evaluación integral de tu negocio. Identificamos fortalezas, debilidades, oportunidades y amenazas. Perfecto para empresas que buscan mejorar su desempeño. ¿Te gustaría más información?",
            "proyectos": "Tenemos experiencia en administración de proyectos usando metodologías PMI/PMBOK. Hemos completado 45+ proyectos exitosos con empresas de diversos sectores. ¿Cuál es tu tipo de proyecto?",
            "servicios": "Ofrecemos 6 servicios principales: Diagnóstico Empresarial, Administración de Proyectos, Planificación Estratégica, Optimización de Procesos, Gestión del Cambio y Capacitación Ejecutiva. ¿Cuál te interesa?",
            "contacto": "¡Excelente! Puedes contactarnos a través del formulario en la sección Contacto, o directamente por WhatsApp. También tenemos oficinas en Quito, Guayaquil y Cuenca. ¿Prefieres agendar una consulta?",
            "precio": "Los precios varían según el alcance y complejidad del proyecto. Te recomendaría agendar una llamada gratuita para darte una cotización personalizada. ¿Te interesa?",
            "equipo": "Contamos con un equipo multidisciplinario de gerentes, ingenieros y consultores especializados en diversos sectores. Todos con más de 10 años de experiencia. ¿Hay algo específico que quieras saber?",
            "hola": "¡Hola! Bienvenido a Consultores Enterprise. Soy tu asistente de IA. Puedo ayudarte con información sobre nuestros servicios, proyectos, o agendar una consulta. ¿Qué necesitas?",
            "ayuda": "Estoy aquí para ayudarte con preguntas sobre nuestros servicios, metodologías, equipo, o para conectarte con nuestro equipo comercial. ¿Qué deseas saber?",
        }};
        
        // Inicializar chat
        let messages = [
            {{"role": "assistant", "content": "¡Hola! 👋 Soy el asistente de Consultores Enterprise. ¿En qué puedo ayudarte hoy? Puedo responder sobre nuestros servicios, proyectos o agendar una consulta."}}
        ];
        
        // Mostrar mensaje inicial
        displayMessages();
        
        function sendMessage() {{
            const input = document.getElementById('userInput');
            const userMessage = input.value.trim();
            
            if (!userMessage) return;
            
            // Agregar mensaje del usuario
            messages.push({{"role": "user", "content": userMessage}});
            input.value = '';
            
            // Generar respuesta
            const userLower = userMessage.toLowerCase();
            let response = null;
            
            for (const [keyword, answer] of Object.entries(respuestas)) {{
                if (userLower.includes(keyword)) {{
                    response = answer;
                    break;
                }}
            }}
            
            if (!response) {{
                response = "Gracias por tu pregunta. Para obtener una respuesta más personalizada, te recomendaría contactar directamente a nuestro equipo. ¿Deseas que te ayude a agendar una consulta o tienes otra pregunta?";
            }}
            
            // Agregar respuesta del asistente
            messages.push({{"role": "assistant", "content": response}});
            
            // Mostrar mensajes
            displayMessages();
            
            // Scroll automático
            setTimeout(() => {{
                document.getElementById('chatMessages').scrollTop = document.getElementById('chatMessages').scrollHeight;
            }}, 100);
        }}
        
        function displayMessages() {{
            const chatMessages = document.getElementById('chatMessages');
            chatMessages.innerHTML = '';
            
            messages.forEach(msg => {{
                const div = document.createElement('div');
                div.className = 'chat-message ' + msg.role;
                
                const bubble = document.createElement('div');
                bubble.className = 'chat-bubble';
                bubble.textContent = msg.content;
                
                div.appendChild(bubble);
                chatMessages.appendChild(div);
            }});
            
            // Scroll al final
            chatMessages.scrollTop = chatMessages.scrollHeight;
        }}
    </script>
""", unsafe_allow_html=True)

st.markdown(f'<div style="text-align:center;color:{theme["text_secondary"]};padding:20px;font-size:0.9em;">© 2024 Consultores Enterprise • Dark Mode ✓ • Versión 2.0 Moderna</div>', unsafe_allow_html=True)
