import plotly.graph_objects as go
import plotly.express as px

# Configuración de la página
st.set_page_config(
    page_title="miEmpresaACME - Consultoría Gerencial",
    page_icon="🏢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilos CSS personalizados con tema celeste
st.markdown("""
    <style>
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
        }
        
        .service-card {
            background-color: white;
            border-left: 5px solid #0099ff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 153, 255, 0.1);
            margin-bottom: 20px;
        }
        
        .news-card {
            background-color: #e8f4f8;
            padding: 20px;
            border-radius: 8px;
            border: 2px solid #0099ff;
            margin-bottom: 15px;
        }
        
        .contact-form {
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            border: 2px solid #0099ff;
        }
    </style>
""", unsafe_allow_html=True)

# Navegación con sidebar
with st.sidebar:
    st.markdown("""
        <div style="text-align: center; padding: 20px 0;">
            <h2 style="color: #0099ff;">🏢 miEmpresaACME</h2>
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
    # Banner con imagen local
    st.image("fotos/fotoInicio.jpg", use_container_width=True)
    
    st.markdown("""
        <div class="header-section">
            <h1>miEmpresaACME Cía. Ltda.</h1>
            <p style="font-size: 1.2em; margin-top: 10px;">Consultoría Gerencial y Administración de Proyectos</p>
            <p style="font-size: 1em; opacity: 0.95;">Transformando negocios ecuatorianos con soluciones estratégicas</p>
        </div>
    """, unsafe_allow_html=True)
    
    # Dashboard de Métricas Profesional con Gráficos
    st.markdown("""
        <div class="header-section" style="text-align: center; margin-bottom: 30px;">
            <h2>Nuestro Desempeño 2024</h2>
        </div>
    """, unsafe_allow_html=True)
    
    # Fila 1: Métricas principales
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
    
    # Fila 2: Gráficos
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # Gráfico de Proyectos por Año
        fig_proyectos = go.Figure(data=[
            go.Bar(x=['2020', '2021', '2022', '2023', '2024'], 
                   y=[8, 12, 15, 18, 45],
                   marker=dict(color=['#0099ff', '#00ccff', '#0099ff', '#00ccff', '#0099ff']))
        ])
        fig_proyectos.update_layout(
            title="Proyectos por Año",
            xaxis_title="Año",
            yaxis_title="Cantidad",
            hovermode='x unified',
            height=350,
            template="plotly_white",
            showlegend=False
        )
        st.plotly_chart(fig_proyectos, use_container_width=True)
    
    with col2:
        # Gráfico Pie: Sectores
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
    
    # Fila 3: Más gráficos
    col1, col2 = st.columns(2, gap="large")
    
    with col1:
        # Gráfico de Línea: Satisfacción
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
        # Gráfico Donut: Distribución de Servicios
        servicios = ['Diagnóstico', 'Planificación', 'Optimización', 'Capacitación', 'Gestión Cambio']
        distribucion = [20, 25, 20, 18, 17]
        
        fig_servicios = go.Figure(data=[go.Pie(
            labels=servicios, 
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
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("💡 Nuestra Propuesta")
        st.write("""
        En miEmpresaACME creemos que cada empresa es única. Ofrecemos soluciones 
        personalizadas de consultoría gerencial que se adaptan a tus necesidades específicas.
        
        Nuestro enfoque combina experiencia, innovación y conocimiento del mercado ecuatoriano 
        para ayudarte a alcanzar tus objetivos estratégicos.
        """)
    
    with col2:
        st.subheader("🎯 ¿Por qué elegirnos?")
        st.write("""
        ✅ Equipo especializado en consultoría gerencial
        
        ✅ Metodologías probadas internacionalmente
        
        ✅ Experiencia con empresas ecuatorianas
        
        ✅ Resultados medibles y sostenibles
        
        ✅ Atención personalizada
        """)
    
    st.divider()
    
    st.subheader("📞 ¿Listo para transformar tu negocio?")
    st.info("Contáctanos para una consulta inicial sin costo. Estamos listos para ayudarte.")

# ==================== PÁGINA: NOSOTROS ====================
elif pagina == "ℹ️ Nosotros":
    st.image("https://images.unsplash.com/photo-1552664730-d307ca884978?w=1200&q=80", use_container_width=True)
    
    st.markdown("""
        <div class="header-section">
            <h1>Sobre Nosotros</h1>
        </div>
    """, unsafe_allow_html=True)
    
    tab1, tab2, tab3, tab4 = st.tabs(["Historia", "Misión", "Visión", "Valores"])
    
    with tab1:
        st.subheader("📖 Nuestra Historia")
        st.write("""
        miEmpresaACME fue fundada en 2012 por un grupo de profesionales con más de 15 años 
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
        <div class="header-section">
            <h1>Nuestros Servicios</h1>
        </div>
    """, unsafe_allow_html=True)
    
    st.write("""
    En miEmpresaACME ofrecemos un portafolio completo de servicios de consultoría 
    diseñados para satisfacer las necesidades más complejas de tu empresa.
    """)
    
    st.divider()
    
    servicios = [
        {
            "titulo": "Diagnóstico Empresarial",
            "descripcion": "Evaluación integral de tu empresa para identificar fortalezas, debilidades, oportunidades y amenazas.",
            "icon": "🔍"
        },
        {
            "titulo": "Administración de Proyectos",
            "descripcion": "Gestión profesional de proyectos con metodologías PMI/PMBOK. Planificación, ejecución y cierre exitoso.",
            "icon": "📋"
        },
        {
            "titulo": "Planificación Estratégica",
            "descripcion": "Desarrollo de estrategias claras y alcanzables para el crecimiento y consolidación de tu negocio.",
            "icon": "🎯"
        },
        {
            "titulo": "Optimización de Procesos",
            "descripcion": "Análisis y mejora continua de tus procesos operacionales para aumentar eficiencia y reducir costos.",
            "icon": "⚙️"
        },
        {
            "titulo": "Gestión del Cambio",
            "descripcion": "Acompañamiento en procesos de transformación organizacional y cambio cultural.",
            "icon": "🔄"
        },
        {
            "titulo": "Capacitación Ejecutiva",
            "descripcion": "Programas de formación personalizados para líderes y equipos gerenciales.",
            "icon": "📚"
        }
    ]
    
    for servicio in servicios:
        st.markdown(f"""
            <div class="service-card">
                <h3>{servicio['icon']} {servicio['titulo']}</h3>
                <p>{servicio['descripcion']}</p>
            </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("🤔 ¿Cuál es tu necesidad?")
    st.write("Si tienes una necesidad específica no listada, contáctanos. Diseñamos soluciones personalizadas.")

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
            "autor": "Equipo miEmpresaACME"
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
            "autor": "Equipo miEmpresaACME"
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
        **miEmpresaACME Cía. Ltda.**
        
        📍 **Oficina Principal**
        Av. Amazonas N34-451 y Av. Naciones Unidas
        Quito, Ecuador
        
        📞 **Teléfonos:**
        +593 2 XXXX-XXXX
        +593 2 XXXX-XXXX
        
        ✉️ **Correo Electrónico:**
        info@miempresaacme.ec
        contacto@miempresaacme.ec
        
        🌐 **Web:**
        www.miempresaacme.ec
        
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
        <p>© 2024 miEmpresaACME Cía. Ltda. | Consultoría Gerencial y Administración de Proyectos</p>
        <p>Quito - Guayaquil - Cuenca | Ecuador</p>
        <p style="font-size: 0.8em; margin-top: 10px;">Diseño y desarrollo web realizado con Streamlit</p>
    </div>
""", unsafe_allow_html=True)
