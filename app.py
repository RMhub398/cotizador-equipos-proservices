import streamlit as st
import pandas as pd
import numpy as np

# Configuración de la página
st.set_page_config(
    page_title="Cotizador de Equipos Proservices",
    page_icon="💰",
    layout="wide"
)

# Datos directamente en el código (extraídos de tu Excel)
data = [
    # PGIC
    {
        "Proveedor": "PGIC", "Marca": "STAIRS", "Línea de Producto": "Bombas multietapas horizontales inox AISI 304",
        "Modelo Base": "MXHM / MXH", "Categoría Producto": "Bomba Superficie Inox", "Procedencia": "China",
        "% Desc. Proveedor": 0.4, "Forma de Pago": "Cheques 60 días", 
        "Condición de pago por monto": "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques", "Garantía": "1 año",
        "Buscar Precio en": "App PGIC", "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189",
        "Email": "vcanales@pgic.cl", "Web/App proveedor": "https://b2b.pgic.cl",
        "Teléfono Oficina/ Sino hay respuesta del vendedor": "+56 2 1234 5678",
        "Datos APP": "Usuario: Kimberly / Clave: Operaciones24 / Ver precios en app PGIC"
    },
    {
        "Proveedor": "PGIC", "Marca": "STAIRS", "Línea de Producto": "Bombas sumergibles pozo profundo",
        "Modelo Base": "6SP / 4SP / 8SP", "Categoría Producto": "Bomba Sumergible", "Procedencia": "China",
        "% Desc. Proveedor": 0.38, "Forma de Pago": "Cheques 60 días", 
        "Condición de pago por monto": "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques", "Garantía": "1 año",
        "Buscar Precio en": "App PGIC", "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189",
        "Email": "vcanales@pgic.cl", "Web/App proveedor": "https://b2b.pgic.cl",
        "Teléfono Oficina/ Sino hay respuesta del vendedor": "+56 2 1234 5678",
        "Datos APP": "Usuario: Kimberly / Clave: Operaciones24 / Ver precios en app PGIC"
    },
    # KOSLAN
    {
        "Proveedor": "KOSLAN", "Marca": "PEDROLLO", "Línea de Producto": "Bombas superficie / pozo / drenaje",
        "Modelo Base": "VARIOS", "Categoría Producto": "Bombas Superficie y Sumergibles", "Procedencia": "Italia",
        "% Desc. Proveedor": 0.38, "Forma de Pago": "Cheque / Transferencia 30 días", 
        "Condición de pago por monto": "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques", "Garantía": "3 años",
        "Buscar Precio en": "App Koslan", "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días habiles", "Contacto Vendedor": "Vicente Campos / +56 9 8230 1594",
        "Email": "vcampos@koslan.cl", "Web/App proveedor": "https://wap.koslan.cl/index.php",
        "Teléfono Oficina/ Sino hay respuesta del vendedor": "+56 2 1234 5678",
        "Datos APP": "ID Cliente: 1739"
    },
    # KSB
    {
        "Proveedor": "KSB", "Marca": "KSB", "Línea de Producto": "Bombas Superficiales",
        "Modelos / Descripción": "Grupo Motobomba Emporia PD, CC, HB", "Categoría Producto": "Bombas Superficiales", 
        "Procedencia": "Alemania", "% Desc. Proveedor": 0.57, "Forma de Pago": "Crédito 30-60 días", 
        "Condición de pago por monto": "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques", "Garantía": "1 año",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días habiles", "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Email": "Danny.Fuenmayor@ksb.com", 
        "Web/App proveedor": "https://my.ksb.cl/login.jhtm?noMessage=t&forwardAction=https://my.ksb.cl/product.jhtm?id=1768&cid=",
        "Teléfono Oficina/ Sino hay respuesta del vendedor": "+56 2 1234 5678",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2025"
    },
    # COSMOPLAS
    {
        "Proveedor": "COSMOPLAS", "Marca": "PENTAX", "Línea de Producto": "Bombas periféricas",
        "Modelos / Descripción": "PM45 / CB / CBM / CAM", "Procedencia": "Italia",
        "% Desc. Proveedor": 0.51, "Forma de Pago": "Crédito 30-60 días", 
        "Condición de pago por monto": "sobre 1MM / 2 cheques / sobre 2MM 3 cheques", "Garantía": "1 año",
        "Forma de cotizar": "Por WhatsApp o correo al vendedor", "Contacto Vendedor": "Camila Gómez / +56 9 5343 2057",
        "Email": "cagomez@cosmoplas.com", "Web/App proveedor": "https://cosmoplas.cl",
        "Instrucción de cotización": "Catálogo largo, enviar código", "Stock": "Confirmar stock"
    },
    # FRANKLIN
    {
        "Proveedor": "FRANKLIN", "Marca": "Franklin", "Línea de Producto": "Kit bomba + motor (completo)",
        "Modelos / Descripción": "Serie SS 4\", 6\", 8\", 10\", Fhoton, SubDrive", "Procedencia": "EE.UU.",
        "% Desc. Proveedor": 0.5, "Forma de Pago": "Cheque 30 días", 
        "Condición de pago por monto": "Confirmar según monto", "Garantía": "1 año",
        "Forma de cotizar": "Por catálogo del proveedor", "Contacto Vendedor": "Enzo Garrido / +56 9 3262 2274",
        "Email": "franklinchile@fele.com", "Web/App proveedor": "https://franklinwater.cl",
        "Instrucción de cotización": "Catálogo Franklin PDF Nov 2024", "Stock": "Confirmar stock"
    },
    # HCP
    {
        "Proveedor": "HCP", "Marca": "HCP", "Línea de Producto": "Aguas Servidas",
        "Modelos / Descripción": "Serie AF", "Procedencia": "Taiwanesa",
        "% Desc. Proveedor": 0.3, "Forma de Pago": "Cheque 30 días", 
        "Condición de pago por monto": "Confirmar con ejecutivo", "Garantía": "1 año",
        "Forma de cotizar": "Catálogo PDF + WhatsApp", "Contacto Vendedor": "Cristóbal Canales / +56 9 8770 7441",
        "Email": "N/D", "Web/App proveedor": "N/D",
        "Instrucción de cotización": "Enviar código del modelo", "Stock": "Confirmar stock"
    }
]

# Convertir a DataFrame
df = pd.DataFrame(data)

# Limpiar y estandarizar nombres de columnas
df.columns = df.columns.str.strip()

# Título de la aplicación
st.title("📊 Cotizador de Equipos - Proservices")
st.markdown("---")

# Sidebar para filtros
with st.sidebar:
    st.header("🔍 Filtros")
    
    # 1. Combo box para seleccionar marca
    marca_seleccionada = st.selectbox(
        "1. Selecciona una marca",
        options=sorted(df['Marca'].unique()),
        key="marca"
    )
    
    # 2. Combo box para seleccionar modelo (se actualiza según marca)
    if marca_seleccionada:
        modelos_disponibles = df[df['Marca'] == marca_seleccionada]['Línea de Producto'].unique()
        modelo_seleccionado = st.selectbox(
            "2. Selecciona un modelo",
            options=sorted(modelos_disponibles),
            key="modelo"
        )

# Mostrar información del producto seleccionado
if marca_seleccionada and modelo_seleccionado:
    producto = df[(df['Marca'] == marca_seleccionada) & 
                 (df['Línea de Producto'] == modelo_seleccionado)].iloc[0].to_dict()
    
    # Convertir a Series para manejo más fácil
    producto = pd.Series(producto)
    
    # 3. Mostrar proveedor
    st.subheader(f"Proveedor: {producto['Proveedor']}")
    
    # Dividir en columnas para mejor organización
    col1, col2 = st.columns(2)
    
    with col1:
        # 4-5. Instrucciones para buscar precio
        st.markdown("### 📌 Buscar Precio")
        
        buscar_precio_en = producto.get('Buscar Precio en', producto.get('Forma de cotizar', 'N/D'))
        
        if buscar_precio_en == "N/D" or pd.isna(buscar_precio_en):
            st.warning("⚠️ Contactar al vendedor para obtener precio")
            st.write(f"**Contacto:** {producto['Contacto Vendedor']}")
            st.write(f"**Email:** {producto['Email']}")
            st.write(f"**Teléfono:** {producto.get('Teléfono Oficina/ Sino hay respuesta del vendedor', 'N/D')}")
        else:
            st.success(f"🔍 Buscar precio en: **{buscar_precio_en}**")
            web_proveedor = producto.get('Web/App proveedor', 'N/D')
            if web_proveedor != 'N/D' and not pd.isna(web_proveedor):
                st.markdown(f"🌐 [Acceder al sitio del proveedor]({web_proveedor})")
            if 'Datos APP' in producto and not pd.isna(producto['Datos APP']):
                st.info(f"🔑 Datos de acceso: {producto['Datos APP']}")
        
        # 12. Garantía y procedencia
        st.markdown("### 📝 Especificaciones")
        st.write(f"**Garantía:** {producto['Garantía']}")
        st.write(f"**Procedencia:** {producto['Procedencia']}")
        
        # Mostrar modelo base si existe
        if 'Modelo Base' in producto and not pd.isna(producto['Modelo Base']):
            st.write(f"**Modelo:** {producto['Modelo Base']}")
        elif 'Modelos / Descripción' in producto and not pd.isna(producto['Modelos / Descripción']):
            st.write(f"**Modelos:** {producto['Modelos / Descripción']}")
    
    with col2:
        # 6. Ingresar precio de lista
        st.markdown("### 💵 Ingresar Precio")
        precio_lista = st.number_input(
            "Precio de lista ($):",
            min_value=0.0,
            step=1000.0,
            key="precio_lista"
        )
        
        # 6. Mostrar descuento del proveedor
        descuento_proveedor = producto.get('% Desc. Proveedor', None)
        
        if descuento_proveedor is not None and not pd.isna(descuento_proveedor):
            st.markdown(f"**Descuento del proveedor:** {descuento_proveedor*100:.2f}%")
            
            # Calcular precio con descuento base
            precio_con_descuento = precio_lista * (1 - descuento_proveedor)
            
            # 7. Descuento adicional para montos > 1.5M
            descuento_extra_disponible = producto.get('Descuento Extra > 1.5MM', 'No') == 'Sí'
            
            if precio_con_descuento > 1500000 and descuento_extra_disponible:
                st.success("🎉 Puedes solicitar descuento adicional (compra > $1.5M)")
                descuento_adicional = st.slider(
                    "Descuento adicional (%):",
                    min_value=0.0,
                    max_value=30.0,
                    value=5.0,
                    step=0.5,
                    key="descuento_extra"
                ) / 100
                
                precio_final = precio_con_descuento * (1 - descuento_adicional)
                descuento_total = 1 - ((1 - descuento_proveedor) * (1 - descuento_adicional))
            else:
                precio_final = precio_con_descuento
                descuento_total = descuento_proveedor
            
            # Mostrar resultados
            if precio_lista > 0:
                st.markdown("### 📊 Resultados")
                
                # 8. Costo
                st.write(f"**Costo:** ${precio_final:,.2f}")
                
                # 9. Margen de contribución
                precio_venta = st.number_input(
                    "Precio de venta al cliente ($):",
                    min_value=0.0,
                    value=precio_final * 1.2,  # 20% de margen por defecto
                    step=1000.0,
                    key="precio_venta"
                )
                
                margen_valor = precio_venta - precio_final
                margen_porcentaje = (margen_valor / precio_venta) * 100 if precio_venta > 0 else 0
                
                st.write(f"**Margen de contribución:** ${margen_valor:,.2f} ({margen_porcentaje:.2f}%)")
                
                # 10. Descuento a mostrar en cotización
                descuento_cotizacion = (1 - (precio_venta / precio_lista)) * 100 if precio_lista > 0 else 0
                st.write(f"**Descuento a aplicar en cotización:** {descuento_cotizacion:.2f}%")
                
                # 11. Precio de venta
                st.success(f"**Precio final de venta:** ${precio_venta:,.2f}")
        
        else:
            st.warning("Este proveedor requiere cotización directa con el vendedor")

# Footer
st.markdown("---")
st.markdown("**Proservices** - Sistema de cotización de equipos")
