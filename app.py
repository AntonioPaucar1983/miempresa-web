import streamlit as st
from datetime import datetime
import plotly.graph_objects as go
import plotly.express as px
import base64

# Configuración de la página
st.set_page_config(
    page_title="Consultores Enterprise. S. A. - Consultoría Gerencial",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados con tema celeste - MEJORADO
st.markdown("""
    <style>
        /* Responsive Design */
        @media (max-width: 768px) {
            .header-section {
                padding: 20px 10px !important;
            }
            .header-section h1 {
                font-size: 1.8em !important;
            }
            .propósito-section h2 {
                font-size: 1.8em !important;
            }
            .propósito-section h3 {
                font-size: 1.3em !important;
            }
        }
        
        :root {
            --color-primary: #0099ff;
            --color-secondary: #00ccff;
            --color-dark: #0d3b66;
            --color-light: #e8f4f8;
        }
        
        .main {
            background-color: #f5f9fb;
        }
        
        .header-section {
            background: linear-gradient(135deg, #0099ff 0%, #00ccff 100%);
            color: white;
            padding: 40px 20px;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(0, 153, 255, 0.2);
        }
        
        .header-section h1 {
            margin: 0;
            font-size: 2.5em;
            font-weight: bold;
        }
        
        .propósito-section {
            background: linear-gradient(135deg, #0d3b66 0%, #0099ff 100%);
            padding: 60px 40px;
            border-radius: 15px;
            text-align: center;
            margin: 40px 0;
            box-shadow: 0 8px 20px rgba(0, 153, 255, 0.2);
        }
        
        .propósito-section h2 {
            color: white;
            font-size: 2.5em;
            margin-bottom: 20px;
            font-weight: bold;
        }
        
        .propósito-section h3 {
            color: #00ccff;
            font-size: 1.8em;
            line-height: 1.6;
            margin: 0;
            font-weight: bold;
        }
        
        .service-card {
            background-color: white;
            border-left: 6px solid #0099ff;
            padding: 25px;
            border-radius: 10px;
            box-shadow: 0 2px 8px rgba(0, 153, 255, 0.15);
            margin-bottom: 20px;
            transition: all 0.3s ease;
        }
        
        .service-card:hover {
            box-shadow: 0 8px 20px rgba(0, 153, 255, 0.3);
            transform: translateY(-5px);
        }
        
        .news-card {
            background-color: #e8f4f8;
            padding: 20px;
            border-radius: 8px;
            border: 2px solid #0099ff;
            margin-bottom: 15px;
            transition: all 0.3s ease;
        }
        
        .news-card:hover {
            box-shadow: 0 4px 12px rgba(0, 153, 255, 0.2);
            transform: translateY(-2px);
        }
        
        .contact-form {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            border: 2px solid #0099ff;
        }
        
        .metric-card {
            background: linear-gradient(135deg, #0099ff 0%, #00ccff 100%);
            color: white;
            padding: 30px;
            border-radius: 12px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0, 153, 255, 0.3);
            transition: transform 0.3s ease;
        }
        
        .metric-card:hover {
            transform: scale(1.05);
        }
        
        .metric-value {
            font-size: 48px;
            font-weight: bold;
            margin: 15px 0;
        }
        
        .metric-label {
            font-size: 16px;
            opacity: 0.95;
            margin-bottom: 10px;
        }
        
        .metric-delta {
            font-size: 13px;
            opacity: 0.85;
            margin-top: 10px;
        }
        
        .cta-button {
            display: inline-block;
            background: linear-gradient(135deg, #0099ff 0%, #00ccff 100%);
            color: white;
            padding: 15px 40px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            margin: 10px 5px;
            transition: all 0.3s ease;
            box-shadow: 0 4px 15px rgba(0, 153, 255, 0.3);
        }
        
        .cta-button:hover {
            transform: translateY(-3px);
            box-shadow: 0 8px 25px rgba(0, 153, 255, 0.4);
        }
        
        .section-title {
            color: #0099ff;
            font-size: 2.2em;
            margin-bottom: 10px;
            font-weight: bold;
            text-align: center;
        }
        
        .section-subtitle {
            color: #666;
            font-size: 1.1em;
            text-align: center;
            margin-bottom: 30px;
        }
        
        /* Imágenes responsive */
        img {
            max-width: 100%;
            height: auto;
            display: block;
        }
    </style>
""", unsafe_allow_html=True)

# Navegación con sidebar
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <h2 style="color: #0099ff;">🏢 Consultores Enterprise</h2>
            <p style="color: #666; font-size: 0.9em;">Consultoría Gerencial y Administración de Proyectos</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    pagina = st.radio(
        "Navegación",
        ["🏠 Inicio", "ℹ️ Nosotros", "💼 Servicios", "📰 Noticias", "📧 Contacto"],
        index=0
    )

# ==================== PÁGINA: INICIO ====================
if pagina == "🏠 Inicio":
    import base64
    
    st.markdown("""
        <div class="header-section" style="text-align: center; margin-bottom: 20px;">
            <h1>Consultores Enterprise. S. A.</h1>
            <p style="font-size: 1.1em;">Consultoría Gerencial y Administración de Proyectos</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Carrusel automático de imágenes
    if 'imagen_index' not in st.session_state:
        st.session_state.imagen_index = 0
    
    fotos = [
        "fotos/fotoInicio.jpg",
        "fotos/fotoInicio1.jpg",
        "fotos/fotoInicio2.jpg",
        "fotos/fotoInicio3.jpg",
        "fotos/fotoInicio4.jpg"
    ]
    
    carousel_html = """
    <style>
        .carousel {
            position: relative;
            width: 100%;
            margin: 0 auto;
            overflow: hidden;
            border-radius: 10px;
            box-shadow: 0 4px 15px rgba(0, 153, 255, 0.3);
            max-height: 500px;
        }
        
        .carousel-inner {
            display: flex;
            animation: slide 25s infinite;
        }
        
        .carousel-item {
            min-width: 100%;
            flex: 0 0 100%;
            overflow: hidden;
        }
        
        .carousel-item img {
            width: 100%;
            height: 500px;
            object-fit: cover;
            display: block;
        }
        
        @keyframes slide {
            0% { transform: translateX(0); }
            20% { transform: translateX(0); }
            25% { transform: translateX(-100%); }
            45% { transform: translateX(-100%); }
            50% { transform: translateX(-200%); }
            70% { transform: translateX(-200%); }
            75% { transform: translateX(-300%); }
            95% { transform: translateX(-300%); }
            100% { transform: translateX(-400%); }
        }
        
        .carousel-counter {
            position: absolute;
            bottom: 20px;
            left: 50%;
            transform: translateX(-50%);
            background-color: rgba(0, 153, 255, 0.9);
            color: white;
            padding: 10px 20px;
            border-radius: 20px;
            font-weight: bold;
            z-index: 10;
        }
    </style>
    
    <div class="carousel">
        <div class="carousel-inner">
    """
    
    for foto in fotos:
        try:
            with open(foto, "rb") as img_file:
                img_base64 = base64.b64encode(img_file.read()).decode()
                carousel_html += f'<div class="carousel-item"><img src="data:image/jpeg;base64,{img_base64}" alt="Foto"></div>'
        except:
            carousel_html += f'<div class="carousel-item" style="background-color: #e8f4f8; display: flex; align-items: center; justify-content: center;"><p>Imagen no encontrada</p></div>'
    
    carousel_html += """
        </div>
        <div class="carousel-counter">Galería automática - 5 fotos</div>
    </div>
    """
    
    st.markdown(carousel_html, unsafe_allow_html=True)
    
    st.divider()
    
    # SECCIÓN: PROPÓSITO/MISIÓN
    st.markdown("""
        <div class="propósito-section">
            <h2>NUESTRO PROPÓSITO</h2>
            <h3>"ASESORAMOS TUS SUEÑOS<br>
                IMPULSAMOS TUS PROYECTOS<br>
                TRANSFORMAMOS TU EMPRESA"</h3>
        </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # Dashboard de Métricas
    st.markdown("""
        <div style="text-align: center; margin: 50px 0;">
            <h2 class="section-title">Nuestro Desempeño 2024</h2>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-label">📊 Proyectos Completados</div>
                <div class="metric-value">45+</div>
                <div class="metric-delta">↑ 15 este año</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-label">😊 Clientes Satisfechos</div>
                <div class="metric-value">32</div>
                <div class="metric-delta">✓ En Ecuador</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
            <div class="metric-card">
                <div class="metric-label">📈 Años de Experiencia</div>
                <div class="metric-value">12</div>
                <div class="metric-delta">✓ En el mercado</div>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # Gráficos
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        fig_proyectos = go.Figure(data=[
            go.Bar(x=['2020', '2021', '2022', '2023', '2024'], 
                   y=[8, 12, 15, 18, 45],
                   marker=dict(color=['#0099ff', '#00ccff', '#0099ff', '#00ccff', '#0099ff']))
        ])
        fig_proyectos.update_layout(
            title="Proyectos Completados por Año",
            xaxis_title="Año",
            yaxis_title="Cantidad",
            hovermode='x unified',
            height=350,
            template="plotly_white",
            showlegend=False
        )
        st.plotly_chart(fig_proyectos, use_container_width=True)
    
    with col2:
        sectores = ['Manufactura', 'Servicios', 'Educación', 'Público', 'Comercio']
        valores = [8, 10, 6, 5, 3]
        
        fig_sectores = go.Figure(data=[go.Pie(labels=sectores, values=valores,
                                               marker=dict(colors=['#0099ff', '#00ccff', '#005fa3', '#0077cc', '#00d4ff']))])
        fig_sectores.update_layout(
            title="Clientes por Sector",
            height=350,
            showlegend=True
        )
        st.plotly_chart(fig_sectores, use_container_width=True)
    
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        meses = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']
        satisfaccion = [88, 90, 89, 92, 93, 91, 94, 95, 93, 96, 97, 98]
        
        fig_satisfaccion = go.Figure()
        fig_satisfaccion.add_trace(go.Scatter(x=meses, y=satisfaccion, mode='lines+markers',
                                              line=dict(color='#0099ff', width=3),
                                              marker=dict(size=8, color='#00ccff')))
        fig_satisfaccion.update_layout(
            title="Índice de Satisfacción de Clientes (%)",
            xaxis_title="Mes",
            yaxis_title="Porcentaje",
            height=350,
            template="plotly_white",
            hovermode='x unified'
        )
        st.plotly_chart(fig_satisfaccion, use_container_width=True)
    
    with col2:
        servicios_list = ['Diagnóstico', 'Planificación', 'Optimización', 'Capacitación', 'Gestión Cambio']
        distribucion = [20, 25, 20, 18, 17]
        
        fig_servicios = go.Figure(data=[go.Pie(
            labels=servicios_list, 
            values=distribucion,
            hole=.4,
            marker=dict(colors=['#0099ff', '#00ccff', '#005fa3', '#0077cc', '#00d4ff'])
        )])
        fig_servicios.update_layout(
            title="Distribución de Servicios Prestados",
            height=350
        )
        st.plotly_chart(fig_servicios, use_container_width=True)
    
    st.divider()
    
    # CTA destacado
    st.markdown("""
        <div style="text-align: center; padding: 40px; background-color: #e8f4f8; border-radius: 10px; margin: 30px 0;">
            <h3 style="color: #0099ff; margin-top: 0;">¿Listo para transformar tu empresa?</h3>
            <p style="color: #555; font-size: 1.1em;">Descubre cómo nuestras soluciones pueden impulsar el crecimiento de tu negocio</p>
        </div>
    """, unsafe_allow_html=True)

# ==================== PÁGINA: NOSOTROS ====================
elif pagina == "ℹ️ Nosotros":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    
    st.markdown("""
        <div class="header-section">
            <h1>Sobre Consultores Enterprise. S. A.</h1>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Historia", "Misión", "Visión", "Valores"])
    
    with tab1:
        st.subheader("📖 Nuestra Historia")
        st.write("""
        Consultores Enterprise fue fundada en 2012 por un grupo de profesionales con más de 15 años 
        de experiencia en consultoría gerencial en Latinoamérica. 
        
        Inicialmente comenzamos como una pequeña consultora en Quito, enfocados en empresas 
        medianas. Con el paso de los años, hemos crecido y ahora trabajamos con empresas 
        de diversos sectores: manufactura, servicios, comercio, educación e instituciones públicas.
        
        Nuestra trayectoria se caracteriza por:
        - Soluciones innovadoras y adaptadas a cada cliente
        - Resultados comprobados y sostenibles
        - Relaciones de largo plazo con nuestros clientes
        - Inversión continua en capacitación de nuestro equipo
        """)
    
    with tab2:
        st.subheader("🎯 Misión")
        st.write("""
        Proporcionar soluciones integrales de consultoría gerencial que permitan a las 
        empresas ecuatorianas mejorar su competitividad, eficiencia operacional y 
        rentabilidad, mediante metodologías comprobadas y un equipo de profesionales 
        altamente calificado.
        """)
    
    with tab3:
        st.subheader("👁️ Visión")
        st.write("""
        Ser el socio estratégico preferido de las empresas ecuatorianas en materia de 
        consultoría gerencial, reconocidos por la calidad de nuestro trabajo, la 
        innovación de nuestras propuestas y el impacto positivo en el crecimiento 
        de nuestros clientes.
        """)
    
    with tab4:
        st.subheader("💎 Valores Corporativos")
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("""
            **Integridad**
            Actuamos con honestidad y transparencia en todas nuestras relaciones.
            
            **Excelencia**
            Nos comprometemos con la calidad en cada proyecto que realizamos.
            
            **Innovación**
            Buscamos constantemente nuevas formas de agregar valor a nuestros clientes.
            """)
        
        with col2:
            st.write("""
            **Responsabilidad**
            Cumplimos nuestros compromisos y somos accountables por nuestros resultados.
            
            **Colaboración**
            Trabajamos en equipo con nuestros clientes como verdaderos socios.
            
            **Sostenibilidad**
            Buscamos crear valor duradero y responsable.
            """)

# ==================== PÁGINA: SERVICIOS ====================
elif pagina == "💼 Servicios":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    
    st.markdown("""
        <div style="text-align: center; margin: 50px 0;">
            <h2 class="section-title">Nuestros Servicios</h2>
            <p class="section-subtitle">Soluciones integrales diseñadas para tu éxito</p>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    Ofrecemos un portafolio completo de servicios de consultoría estratégica, diseñados para 
    transformar tu negocio y llevar tu empresa al siguiente nivel.
    """)
    
    st.divider()
    
    servicios = [
        {
            "titulo": "🔍 Diagnóstico Empresarial",
            "descripcion": "Evaluación integral de tu empresa para identificar fortalezas, debilidades, oportunidades y amenazas.",
            "color": "#0099ff"
        },
        {
            "titulo": "📋 Administración de Proyectos",
            "descripcion": "Gestión profesional de proyectos con metodologías PMI/PMBOK. Planificación, ejecución y cierre exitoso.",
            "color": "#00ccff"
        },
        {
            "titulo": "🎯 Planificación Estratégica",
            "descripcion": "Desarrollo de estrategias claras y alcanzables para el crecimiento y consolidación de tu negocio.",
            "color": "#0077cc"
        },
        {
            "titulo": "⚙️ Optimización de Procesos",
            "descripcion": "Análisis y mejora continua de tus procesos operacionales para aumentar eficiencia y reducir costos.",
            "color": "#005fa3"
        },
        {
            "titulo": "🔄 Gestión del Cambio",
            "descripcion": "Acompañamiento en procesos de transformación organizacional y cambio cultural.",
            "color": "#0099ff"
        },
        {
            "titulo": "📚 Capacitación Ejecutiva",
            "descripcion": "Programas de formación personalizados para líderes y equipos gerenciales.",
            "color": "#00ccff"
        }
    ]
    
    for servicio in servicios:
        st.markdown(f"""
            <div class="service-card" style="border-left-color: {servicio['color']};">
                <h3 style="color: {servicio['color']}; margin-top: 0;">{servicio['titulo']}</h3>
                <p style="color: #555; line-height: 1.6;">{servicio['descripcion']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
        <div style="text-align: center; padding: 40px; background-color: #e8f4f8; border-radius: 10px; margin: 30px 0;">
            <h3 style="color: #0099ff; margin-top: 0;">¿Necesitas un servicio personalizado?</h3>
            <p style="color: #555;">Contáctanos para discutir tus necesidades específicas y diseñar una solución a medida</p>
        </div>
    """, unsafe_allow_html=True)

# ==================== PÁGINA: NOTICIAS ====================
elif pagina == "📰 Noticias":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    
    st.markdown("""
        <div class="header-section">
            <h1>Blog de Noticias</h1>
        </div>
    """, unsafe_allow_html=True)
    
    noticias = [
        {
            "titulo": "5 Tendencias de Administración de Proyectos en 2024",
            "fecha": "15 de septiembre, 2024",
            "contenido": "La administración de proyectos evoluciona constantemente. En este artículo exploramos las tendencias más importantes que están transformando la forma en que gestionamos proyectos en Ecuador.",
            "autor": "Equipo Consultores Enterprise"
        },
        {
            "titulo": "Transformación Digital: Más que una moda",
            "fecha": "8 de septiembre, 2024",
            "contenido": "La transformación digital no es solo tecnología. Descubre cómo las empresas ecuatorianas están aprovechando la transformación para mejorar competitividad y eficiencia.",
            "autor": "Dra. María González"
        },
        {
            "titulo": "Casos de Éxito: Empresa Manufacturera aumenta 30% en Productividad",
            "fecha": "1 de septiembre, 2024",
            "contenido": "Conoce cómo una empresa del sector manufacturero en Cuenca logró aumentar su productividad en 30% gracias a nuestro programa de optimización de procesos.",
            "autor": "Ing. Carlos Rodríguez"
        },
        {
            "titulo": "Liderazgo Efectivo en Tiempos de Incertidumbre",
            "fecha": "25 de agosto, 2024",
            "contenido": "¿Cómo los líderes pueden mantener equipos motivados en épocas de cambio? Compartimos estrategias probadas que funcionan en el contexto ecuatoriano.",
            "autor": "Equipo Consultores Enterprise"
        }
    ]
    
    for noticia in noticias:
        st.markdown(f"""
            <div class="news-card">
                <h3>{noticia['titulo']}</h3>
                <p style="font-size: 0.9em; color: #0099ff; margin: 10px 0;">📅 {noticia['fecha']} | ✍️ {noticia['autor']}</p>
                <p>{noticia['contenido']}</p>
                <a href="#" style="color: #0099ff; font-weight: bold; text-decoration: none;">Leer más →</a>
            </div>
        """, unsafe_allow_html=True)

# ==================== PÁGINA: CONTACTO ====================
elif pagina == "📧 Contacto":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    
    st.markdown("""
        <div class="header-section">
            <h1>Contáctanos</h1>
        </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📍 Información de Contacto")
        
        st.write("""
        **Consultores Enterprise. S. A.**
        
        📍 **Oficina Principal**
        Av. Amazonas N34-451 y Av. Naciones Unidas
        Quito, Ecuador
        
        📞 **Teléfonos:**
        +593 2 XXXX-XXXX
        +593 2 XXXX-XXXX
        
        ✉️ **Correo Electrónico:**
        info@consultor-enterprise.ec
        contacto@consultor-enterprise.ec
        
        🌐 **Web:**
        www.consultor-enterprise.ec
        
        ⏰ **Horarios de Atención:**
        Lunes - Viernes: 8:00 AM - 6:00 PM
        Sábado: 9:00 AM - 1:00 PM
        """)
    
    with col2:
        st.subheader("✍️ Formulario de Contacto")
        
        with st.form("formulario_contacto"):
            nombre = st.text_input("Nombre Completo")
            empresa = st.text_input("Empresa")
            email = st.text_input("Correo Electrónico")
            telefono = st.text_input("Teléfono")
            
            asunto_options = [
                "Consulta General",
                "Solicitud de Cotización",
                "Diagnóstico Empresarial",
                "Administración de Proyectos",
                "Planificación Estratégica",
                "Otro"
            ]
            asunto = st.selectbox("Asunto", asunto_options)
            
            mensaje = st.text_area("Mensaje", height=150)
            
            enviado = st.form_submit_button("📬 Enviar Mensaje", use_container_width=True)
            
            if enviado:
                if nombre and email and mensaje:
                    st.success("✅ ¡Mensaje enviado exitosamente! Nos contactaremos pronto.")
                    st.balloons()
                else:
                    st.error("⚠️ Por favor completa los campos requeridos.")
    
    st.divider()
    
    st.subheader("🏢 Sucursales")
    
    sucursales = [
        {
            "ciudad": "Quito",
            "direccion": "Av. Amazonas N34-451",
            "telefono": "+593 2 XXXX-XXXX"
        },
        {
            "ciudad": "Guayaquil",
            "direccion": "Av. Francisco de Orellana",
            "telefono": "+593 4 XXXX-XXXX"
        },
        {
            "ciudad": "Cuenca",
            "direccion": "Calle Larga",
            "telefono": "+593 7 XXXX-XXXX"
        }
    ]
    
    col1, col2, col3 = st.columns(3)
    
    for idx, sucursal in enumerate(sucursales):
        with [col1, col2, col3][idx]:
            st.info(f"""
            **{sucursal['ciudad']}**
            
            📍 {sucursal['direccion']}
            
            📞 {sucursal['telefono']}
            """)

# Footer
st.divider()
st.markdown("""
    <div style="text-align: center; padding: 20px; color: #666; font-size: 0.9em;">
        <p>© 2024 Consultores Enterprise. S. A. | Consultoría Gerencial y Administración de Proyectos</p>
        <p>Quito - Guayaquil - Cuenca | Ecuador</p>
        <p style="font-size: 0.8em; margin-top: 10px;">Diseño y desarrollo web realizado con Streamlit</p>
    </div>
""", unsafe_allow_html=True)
