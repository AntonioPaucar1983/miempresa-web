# miEmpresaACME - Página Web Demo

Página web profesional para miEmpresaACME Cía. Ltda. - Consultoría Gerencial y Administración de Proyectos.

Desarrollada con **Streamlit** y lista para publicar en **Streamlit Cloud**.

---

## 📋 Contenido de la Aplicación

La aplicación incluye las siguientes secciones:

- **🏠 Inicio**: Presentación de la empresa con métricas clave
- **ℹ️ Nosotros**: Historia, misión, visión y valores
- **💼 Servicios**: Portafolio completo de servicios ofrecidos
- **📰 Noticias**: Blog con artículos y casos de éxito
- **📧 Contacto**: Formulario de contacto e información de sucursales

---

## 🚀 Pasos para Publicar en Streamlit Cloud

### Paso 1: Preparar tu Repositorio en GitHub

1. **Crear un nuevo repositorio en GitHub**
   - Ve a https://github.com/new
   - Nombra el repositorio: `miempresaacme-web` (o el nombre que prefieras)
   - Selecciona "Public" para que sea visible
   - Crea el repositorio

2. **Clonar el repositorio en tu computadora**
   ```bash
   git clone https://github.com/tu-usuario/miempresaacme-web.git
   cd miempresaacme-web
   ```

3. **Copiar los archivos**
   - Coloca los archivos `app.py` y `requirements.txt` en la carpeta del repositorio

4. **Hacer el primer commit**
   ```bash
   git add app.py requirements.txt
   git commit -m "Inicial: Página web miEmpresaACME con Streamlit"
   git push origin main
   ```

---

### Paso 2: Publicar en Streamlit Cloud (GRATIS ✅)

1. **Ir a Streamlit Cloud**
   - Ve a https://streamlit.io/cloud
   - Haz clic en "Sign up"

2. **Conectar tu GitHub**
   - Selecciona tu cuenta de GitHub
   - Autoriza a Streamlit Cloud

3. **Crear la aplicación**
   - Haz clic en "New app"
   - Selecciona:
     - **Repository**: tu-usuario/miempresaacme-web
     - **Branch**: main
     - **Main file path**: app.py
   - Haz clic en "Deploy"

4. **¡Listo! 🎉**
   - Streamlit Cloud te generará una URL pública
   - Cada vez que hagas `git push`, la aplicación se actualiza automáticamente

---

## 💻 Para Ejecutar Localmente

Si quieres ver la página en tu computadora antes de publicar:

```bash
# Instalar dependencias
pip install -r requirements.txt

# Ejecutar la aplicación
streamlit run app.py
```

Luego abre tu navegador en: http://localhost:8501

---

## ✏️ Personalizar la Información

Para cambiar la información de la empresa, edita `app.py`:

- **Teléfonos**: Busca `+593 2 XXXX-XXXX` y reemplaza
- **Correos**: Busca `info@miempresaacme.ec` y reemplaza
- **Direcciones**: Busca "Av. Amazonas" y actualiza
- **Contenido**: Modifica los textos de historia, misión, servicios, etc.
- **Colores**: Los colores celestes están en la sección `<style>`, puedes cambiar los códigos hex

---

## 🎨 Colores Celestes Utilizados

- **Primario**: #0099ff (Azul cielo fuerte)
- **Secundario**: #00ccff (Cyan)
- **Oscuro**: #0d3b66 (Azul oscuro)
- **Claro**: #e8f4f8 (Azul muy claro)

---

## 📱 Características

✅ Diseño responsivo (funciona en móvil, tablet y desktop)
✅ Navegación por sidebar
✅ Formulario de contacto funcional
✅ Tema celeste profesional
✅ Carga rápida
✅ Sin costo de hosting
✅ Actualizaciones automáticas con Git

---

## 🔗 URLs Importantes

- **Streamlit Cloud**: https://streamlit.io/cloud
- **Documentación Streamlit**: https://docs.streamlit.io
- **GitHub**: https://github.com

---

## 📞 Soporte

Para cambios adicionales, simplemente:
1. Edita `app.py`
2. Haz `git push`
3. Streamlit Cloud se actualiza automáticamente

---

**¡Tu página está lista para impresionar a clientes!** 🚀
