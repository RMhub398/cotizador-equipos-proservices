import os
os.environ["STREAMLIT_SERVER_FILE_WATCHER_TYPE"] = "none"

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Cotizador Grupo Proservices 2026",
    page_icon="💰",
    layout="wide"
)

# =================================================================================
# MATRIZ DE MÁRGENES ACTUALIZADA (2026)
# =================================================================================
MARGENES = [
    {"Tramo": "$1 – $299.999", "Min": 1, "Max": 299999, "Margen": 0.22},
    {"Tramo": "$300.000 – $999.999", "Min": 300000, "Max": 999999, "Margen": 0.185},
    {"Tramo": "$1.000.000 – $1.999.999", "Min": 1_000_000, "Max": 1_999_999, "Margen": 0.18},
    {"Tramo": "$2.000.000 – $2.999.999", "Min": 2_000_000, "Max": 2_999_999, "Margen": 0.175},
    {"Tramo": "$3.000.000 – $4.999.999", "Min": 3_000_000, "Max": 4_999_999, "Margen": 0.17},
    {"Tramo": "SOBRE 5.000.000", "Min": 5_000_000, "Max": float("inf"), "Margen": 0.17}
]

# =================================================================================
# DATOS COMPLETOS DE TODOS LOS PROVEEDORES (CON TODOS LOS MODELOS)
# =================================================================================
PROVEEDORES = [
# =============================================
# LAS BRUJAS (EQUIPOS DE RIEGO) - Todos los modelos completos
# =============================================
{
    "Proveedor": "LAS BRUJAS (EQUIPOS DE RIEGO)", "Marca": "PROPUMPS VERTICAL",
    "Línea de Producto": "Bombas multietapas verticales inox AISI 304",
    "Modelo Base": "ECDLF", "Procedencia": "China", "% Desc. Proveedor": 0.43,
    "Forma de Pago": "Cheques 30 días", "Condición de pago por monto": "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques",
    "Garantía": "1 año", "Buscar Precio en": "App LAS BRUJAS", "Descuento Extra > 1.5MM": "Sí",
    "Monto Activación": 1500000, "Entrega con despacho": "1 día hábil",
    "Contacto Vendedor": "JUAN CARLOS GUTIERREZ / +56 9 68319437",
    "Email": "comunicacionesodoo@equiposderiego.cl",
    "Web PGIC": "https://equiposderiego.b2bcarts.com/login",
    "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: Bombas2024*"
},
{
    "Proveedor": "LAS BRUJAS (EQUIPOS DE RIEGO)", "Marca": "VAREM",
    "Línea de Producto": "Estanques hidroneumáticos", 
    "Modelo Base": "VERTICAL / HORIZONTAL / 10BAR /16BAR", "Procedencia": "Italia", "% Desc. Proveedor": 0.40,
    "Forma de Pago": "Cheques 30 días", "Condición de pago por monto": "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques",
    "Garantía": "1 año", "Buscar Precio en": "App LAS BRUJAS", "Descuento Extra > 1.5MM": "Sí",
    "Monto Activación": 1500000, "Entrega con despacho": "1 día hábil",
    "Contacto Vendedor": "JUAN CARLOS GUTIERREZ / +56 9 68319440",
    "Email": "comunicacionesodoo@equiposderiego.cl",
    "Web PGIC": "https://equiposderiego.b2bcarts.com/login",
    "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: Bombas2024*"
},
{
    "Proveedor": "LAS BRUJAS (EQUIPOS DE RIEGO)", "Marca": "FORAS",
    "Línea de Producto": "Bombas centrífugas, multietapas, drenaje",
    "Modelo Base": "FV/FC/DC/NM/KB", "Procedencia": "Italia", "% Desc. Proveedor": 0.42,
    "Forma de Pago": "Cheques 30 días", "Condición de pago por monto": "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques",
    "Garantía": "1 año", "Buscar Precio en": "App LAS BRUJAS", "Descuento Extra > 1.5MM": "Sí",
    "Monto Activación": 1500000, "Entrega con despacho": "1 día hábil",
    "Contacto Vendedor": "JUAN CARLOS GUTIERREZ / +56 9 68319441",
    "Email": "comunicacionesodoo@equiposderiego.cl",
    "Web PGIC": "https://equiposderiego.b2bcarts.com/login",
    "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: Bombas2024*"
},
{
    "Proveedor": "LAS BRUJAS (EQUIPOS DE RIEGO)", "Marca": "PROPUMPS HORIZONTAL",
    "Línea de Producto": "Bombas centrífugas, multietapas, drenaje",
    "Modelo Base": "HFT/DP/SCM/CM2", "Procedencia": "China", "% Desc. Proveedor": 0.36,
    "Forma de Pago": "Cheques 30 días", "Condición de pago por monto": "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques",
    "Garantía": "1 año", "Buscar Precio en": "App LAS BRUJAS", "Descuento Extra > 1.5MM": "Sí",
    "Monto Activación": 1500000, "Entrega con despacho": "1 día hábil",
    "Contacto Vendedor": "JUAN CARLOS GUTIERREZ / +56 9 68319442",
    "Email": "comunicacionesodoo@equiposderiego.cl",
    "Web PGIC": "https://equiposderiego.b2bcarts.com/login",
    "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: Bombas2024*"
},

    # =============================================
    # PGIC (Todos los modelos completos)
    # =============================================
    {
        "Proveedor": "PGIC", "Marca": "CALPEDA", 
        "Línea de Producto": "Bombas multietapa horizontal inox AISI 304",
        "Modelo Base": "MXHM / MXH", "Procedencia": "Italia", "% Desc. Proveedor": 0.38,
        "Forma de Pago": "Cheques 60 días", "Condición de pago por monto": "sobre 1MM / 2 cheques/ sobre 2MM 3 cheques",
        "Garantía": "1 año", "Buscar Precio en": "App PGIC", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "1 día hábil",
        "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189",
        "Email": "vcanales@pgic.cl", "Web/App proveedor": "https://b2b.pgic.cl",
        "Teléfono Oficina": "+56 2 1234 5678",
        "Datos APP": "Usuario: Kimberly / Clave: Operaciones24"
    },
    {
        "Proveedor": "PGIC", "Marca": "STAIRS", 
        "Línea de Producto": "Bombas sumergibles pozo profundo",
        "Modelo Base": "6SP / 4ST / 8SP", "Procedencia": "China", "% Desc. Proveedor": 0.38,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC", 
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000, 
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "STAIRS", 
        "Línea de Producto": "Bombas multietapa vertical inox AISI 304",
        "Modelo Base": "SB / SBI", "Procedencia": "China", "% Desc. Proveedor": 0.43,
        "Forma de Pago": "Cheques 60 días", "Garantía": "2 años", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0190"
    },
    {
        "Proveedor": "PGIC", "Marca": "AQUASYSTEM", 
        "Línea de Producto": "Estanques hidroneumáticos",
        "Modelo Base": "VERTICAL / HORIZONTAL / 10BAR /16BAR", "Procedencia": "Italia", "% Desc. Proveedor": 0.40,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "MEUDY", 
        "Línea de Producto": "Bombas sumergibles para lodo / contratistas",
        "Modelo Base": "FSM/ KSM /KBZ /KBS/ KBD", "Procedencia": "China", "% Desc. Proveedor": 0.38,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "MEUDY", 
        "Línea de Producto": "Bombas sumergibles aguas servidas",
        "Modelo Base": "U / C /B /G", "Procedencia": "China", "% Desc. Proveedor": 0.40,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "BESTFLOW", 
        "Línea de Producto": "Bombas de pozo / superficie / Variadores y tableros eléctricos",
        "Modelo Base": "VFD / TBF / STAR", "Procedencia": "China", "% Desc. Proveedor": 0.38,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "DRENO", 
        "Línea de Producto": "Bombas para aguas servidas y drenaje",
        "Modelo Base": "AM / AT /COMPATTA", "Procedencia": "Italia", "% Desc. Proveedor": 0.40,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "FRANKLIN", 
        "Línea de Producto": "Motores sumergibles y bombas STAIRS by Franklin",
        "Modelo Base": "4FM / 6FM", "Procedencia": "EE.UU.", "% Desc. Proveedor": 0.38,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "SUBLINE", 
        "Línea de Producto": "Bombas sumergibles de pozo",
        "Modelo Base": "FF / FS", "Procedencia": "Italia", "% Desc. Proveedor": 0.38,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "ELENTEK", 
        "Línea de Producto": "Tableros eléctricos inteligentes y arrancadores",
        "Modelo Base": "TABLEROS CONTROL ELECTRONICOS", "Procedencia": "Italia", "% Desc. Proveedor": 0.36,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "ULMAX", 
        "Línea de Producto": "Bombas verticales multietapas",
        "Modelo Base": "SVMT", "Procedencia": "China", "% Desc. Proveedor": 0.48,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "ULMAX", 
        "Línea de Producto": "Variadores de frecuencia",
        "Modelo Base": "UX", "Procedencia": "China", "% Desc. Proveedor": 0.42,
        "Forma de Pago": "Cheques 60 días", "Garantía": "1 año", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "REGGIO", 
        "Línea de Producto": "Bombas centrífugas, multietapas, drenaje",
        "Modelo Base": "SM / ST /CFM / STF /STO /SSBJ", "Procedencia": "Italia", "% Desc. Proveedor": 0.38,
        "Forma de Pago": "Cheques 60 días", "Garantía": "2 años", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },
    {
        "Proveedor": "PGIC", "Marca": "REGGIO", 
        "Línea de Producto": "Bombas centrífugas Normalizadas",
        "Modelo Base": "SN", "Procedencia": "Italia", "% Desc. Proveedor": 0.50,
        "Forma de Pago": "Cheques 60 días", "Garantía": "2 años", "Buscar Precio en": "App PGIC",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "1 día hábil", "Contacto Vendedor": "Valeska Canales / +56 9 6206 0189"
    },

    # =============================================
    # KOSLAN (Todos los modelos completos)
    # =============================================
    {
        "Proveedor": "KOSLAN", "Marca": "PEDROLLO", 
        "Línea de Producto": "Bombas superficie",
        "Modelo Base": "CPM / CP / 2CPM / HF / F", "Procedencia": "Italia", "% Desc. Proveedor": 0.45,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "3 años", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8608",
        "Email": "smartinez@koslan.cl", "Web/App proveedor": "https://wap.koslan.cl/index.php",
        "Datos APP": "ID Cliente: 1739"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "PEDROLLO", 
        "Línea de Producto": "Bombas sumergible / pozo / aguas servidas / drenaje",
        "Modelo Base": "4SR /4BLOCK /VX /MC", "Procedencia": "Italia", "% Desc. Proveedor": 0.48,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "3 años", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8609",
        "Email": "smartinez@koslan.cl"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "PEDROLLO", 
        "Línea de Producto": "Variadores y tableros eléctricos",
        "Modelo Base": "Serie E1 / E2", "Procedencia": "Italia", "% Desc. Proveedor": 0.40,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "3 años", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8610",
        "Email": "smartinez@koslan.cl",
        "Datos APP": "Arrancadores y tableros configurables"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "FLOWMAK", 
        "Línea de Producto": "Bombas agrícolas, periféricas y sumergibles/ válvulas",
        "Modelo Base": "VARIOS", "Procedencia": "China", "% Desc. Proveedor": 0.38,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "1 año", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8611",
        "Email": "smartinez@koslan.cl",
        "Datos APP": "Uso agrícola y domiciliario"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "MAC3", 
        "Línea de Producto": "Sensores de nivel",
        "Modelo Base": "VARIOS", "Procedencia": "EE.UU.", "% Desc. Proveedor": 0.47,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "1 año", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8612",
        "Email": "smartinez@koslan.cl", "Web/App proveedor": "https://wap.koslan.cl/index.php",
        "Datos APP": "Control de nivel"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "RAIN", 
        "Línea de Producto": "Válvulas solenoides, programadores",
        "Modelo Base": "VARIOS", "Procedencia": "EE.UU.", "% Desc. Proveedor": 0.40,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "1 año", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8612",
        "Email": "smartinez@koslan.cl",
        "Datos APP": "Controladores de riego y electroválvulas"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "KOSLAN", 
        "Línea de Producto": "Tableros eléctricos electronicos",
        "Modelo Base": "DOMINO / SIMPLEX / DUPLEX", "Procedencia": "Chile", "% Desc. Proveedor": 0.38,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "1 año", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8613",
        "Email": "smartinez@koslan.cl",
        "Datos APP": "Tableros armados a medida"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "ZENIT", 
        "Línea de Producto": "Bombas aguas servidas industriales",
        "Modelo Base": "GRBLUE / GRS /GRG / AP / UNIQA", "Procedencia": "Italia", "% Desc. Proveedor": 0.45,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "2 años", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8614",
        "Email": "smartinez@koslan.cl",
        "Datos APP": "Bombas trituradoras y de canal abierto"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "VAREM", 
        "Línea de Producto": "Estanques hidroneumáticos",
        "Modelo Base": "VERTICAL / HORIZONTAL / 10BAR /16BAR", "Procedencia": "Italia", "% Desc. Proveedor": 0.40,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "1 año", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8615",
        "Email": "smartinez@koslan.cl",
        "Datos APP": "Estanques verticales y horizontales certificados"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "LEO", 
        "Línea de Producto": "Bombas superficie y bombas solares",
        "Modelo Base": "LVS / LPP /PQ /3ACM /2ACM /AMS", "Procedencia": "China", "% Desc. Proveedor": 0.45,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "2 años", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8616",
        "Email": "smartinez@koslan.cl", "Web/App proveedor": "https://wap.koslan.cl/index.php",
        "Datos APP": "Uso residencial y riego simple"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "LEO", 
        "Línea de Producto": "Variadores de frecuencia",
        "Modelo Base": "PDH30", "Procedencia": "China", "% Desc. Proveedor": 0.48,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "2 años", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8616",
        "Email": "smartinez@koslan.cl", "Web/App proveedor": "https://wap.koslan.cl/index.php",
        "Datos APP": "Variador de frecuencia PDH30"
    },
    {
        "Proveedor": "KOSLAN", "Marca": "LEO", 
        "Línea de Producto": "Bombas sumergibles",
        "Modelo Base": "LVS / LPP /PQ /3ACM /2ACM /AMS", "Procedencia": "China", "% Desc. Proveedor": 0.47,
        "Forma de Pago": "Transferencia", "Condición de pago por monto": "contado", "Garantía": "2 años", "Buscar Precio en": "App Koslan",
        "Descuento Extra > 1.5MM": "Sí", "Monto Activación": 1500000,
        "Entrega con despacho": "2 días hábiles", "Contacto Vendedor": "Smith Martinez / +56 9 3433 8616",
        "Email": "smartinez@koslan.cl", "Web/App proveedor": "https://wap.koslan.cl/index.php",
        "Datos APP": "Bombas sumergibles"
    },

    # =============================================
    # KSB (Todos los modelos completos)
    # =============================================
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Bombas Superficiales",
        "Modelo Base": "Grupo Motobomba Emporia PD, CC, HB", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.57, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Email": "Danny.Fuenmayor@ksb.com", "Web/App proveedor": "https://my.ksb.cl",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2025"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Bombas Superficiales",
        "Modelo Base": "Grupo Motobomba Emporia CP, GS, GC, GR", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.57, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2026"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Multietapas Verticales",
        "Modelo Base": "Grupo Motobomba MOVITEC B, C", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.57, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2027"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Bombas Normalizadas",
        "Modelo Base": "MegaNorm", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.24, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2028"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Motores Alta Eficiencia",
        "Modelo Base": "Motores IE3 B3", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.24, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2029"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Motores Premium IE4/IE5",
        "Modelo Base": "SupremE", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.24, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2030"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Automatización",
        "Modelo Base": "Pumpdrive R, Pumpdrive 2", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.52, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2031"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Agua Residual",
        "Modelo Base": "Amarex N / ARX / KRT", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.52, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2032"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Accesorios de Montaje",
        "Modelo Base": "Flanges y Bases", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.28, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "No",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9269",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2033"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Agua Residual",
        "Modelo Base": "Clas / Clasvort / Drain Vort / Canal Bi", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.57, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9271",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2035"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Automatización",
        "Modelo Base": "Hyamat V / PD / SPD", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.28, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9273",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2037"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Automatización",
        "Modelo Base": "Delta Compact / Solo / Primo / Eco", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.52, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9274",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2038"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Válvulas Industriales",
        "Modelo Base": "ECOLINE / PROFIT / HERA / SYSTO", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.57, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9275",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2039"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Accesorios",
        "Modelo Base": "Flanges / Bases / Camisas / Cables", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.28, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "No",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9276",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2040"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Bombas Monobloc",
        "Modelo Base": "Megabloc", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.30, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9277",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2041"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Motores Eléctricos",
        "Modelo Base": "IE3 B3", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.24, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9278",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2042"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Motores Eléctricos",
        "Modelo Base": "IE3 JM - Movitec", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.24, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9279",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2043"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Motores Rebobinables",
        "Modelo Base": "UMA / UMC / UMA S", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.24, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9280",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2044"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Motores Encapsulados",
        "Modelo Base": "COM / CWM / PD / PDM", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.24, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9281",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2045"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Bombas de Pozo",
        "Modelo Base": "UPA 200 / 250 / 300 / 350", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.54, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9282",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2046"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Bombas de Pozo",
        "Modelo Base": "Upachrom 75 CN / 100 CN / 150 CC / 200 CC", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.62, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9283",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2047"
    },
    {
        "Proveedor": "KSB", "Marca": "KSB", 
        "Línea de Producto": "Hidroneumáticos / Accesorios",
        "Modelo Base": "Hidroneumáticos + kits / Acoplamientos / Cables", "Procedencia": "Alemania", 
        "% Desc. Proveedor": 0.57, "Forma de Pago": "Crédito 30 días", "Garantía": "2 años",
        "Buscar Precio en": "App KSB", "Descuento Extra > 1.5MM": "Sí",
        "Monto Activación": 1500000, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "Danny Fuenmayor / +56 9 7451 9284",
        "Datos APP": "Usuario: kgonzalez@grupoproservices.cl / Clave: KIMBGON2048"
    },

    # =============================================
    # COSMOPLAS (Todos los modelos completos)
    # =============================================
    {
        "Proveedor": "COSMOPLAS", "Marca": "PENTAX", 
        "Línea de Producto": "Bombas periféricas",
        "Modelo Base": "PM45 / CB / CBM / CAM", "Procedencia": "Italia", "% Desc. Proveedor": 0.51,
        "Forma de Pago": "Crédito 30-60 días", "Garantía": "1 año", 
        "Forma de cotizar": "Por WhatsApp o correo al vendedor",
        "Contacto Vendedor": "Carlos Gómez / +56 9 5343 2057", "Email": "cagomez@cosmoplas.com",
        "Web/App proveedor": "https://cosmoplas.cl", "Instrucción de cotización": "Catálogo largo, enviar código",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "COSMOPLAS", "Marca": "CNP", 
        "Línea de Producto": "Bombas multietapas / centrífugas",
        "Modelo Base": "CHLF / CDLF / ZS 50-32-160", "Procedencia": "China", "% Desc. Proveedor": "Cotizar",
        "Forma de Pago": "Crédito 30-60 días", "Garantía": "1 año", 
        "Forma de cotizar": "Por WhatsApp o correo al vendedor",
        "Contacto Vendedor": "Carlos Gómez / +56 9 5343 2057", "Email": "cagomez@cosmoplas.com",
        "Web/App proveedor": "https://cosmoplas.cl", "Instrucción de cotización": "Catálogo largo, enviar código",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "COSMOPLAS", "Marca": "VAREM", 
        "Línea de Producto": "Estanques hidroneumáticos / sanitarios",
        "Modelo Base": "24L, 60L, 100L, 200L", "Procedencia": "Italia", "% Desc. Proveedor": "Cotizar",
        "Forma de Pago": "Crédito 30-60 días", "Garantía": "1 año", 
        "Forma de cotizar": "Por WhatsApp o correo al vendedor",
        "Contacto Vendedor": "Carlos Gómez / +56 9 5343 2057", "Email": "cagomez@cosmoplas.com",
        "Web/App proveedor": "https://cosmoplas.cl", "Instrucción de cotización": "Catálogo largo, enviar código",
        "Stock": "Confirmar stock"
    },

    # =============================================
    # FRANKLIN (Todos los modelos completos)
    # =============================================
    {
        "Proveedor": "FRANKLIN", "Marca": "Franklin", 
        "Línea de Producto": "Kit bomba + motor (completo)",
        "Modelo Base": "Serie SS 4\", 6\", 8\", 10\", Fhoton, SubDrive", "Procedencia": "EE.UU.", 
        "% Desc. Proveedor": 0.50, "Forma de Pago": "Cheque 30 días", "Garantía": "1 año",
        "Forma de cotizar": "Por catálogo del proveedor", 
        "Contacto Vendedor": "Enzo Garrido / +56 9 3262 2274", "Email": "franklinchile@fele.com",
        "Web/App proveedor": "https://franklinwater.cl", 
        "Instrucción de cotización": "Catálogo Franklin PDF Nov 2024",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "FRANKLIN", "Marca": "Franklin", 
        "Línea de Producto": "Motores y bombas por separado",
        "Modelo Base": "Motores 4\", 6\", 8\", partes hidráulicas", "Procedencia": "EE.UU.", 
        "% Desc. Proveedor": 0.45, "Forma de Pago": "Cheque 30 días", "Garantía": "1 año",
        "Forma de cotizar": "Por catálogo del proveedor",
        "Contacto Vendedor": "Enzo Garrido / +56 9 3262 2274", "Email": "franklinchile@fele.com",
        "Instrucción de cotización": "Cotizar código exacto vía WhatsApp",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "FRANKLIN", "Marca": "Franklin", 
        "Línea de Producto": "Sistemas de bombeo solar",
        "Modelo Base": "Fhoton SolarPAK / SubDrive SolarPAK", "Procedencia": "EE.UU.", 
        "% Desc. Proveedor": 0.50, "Forma de Pago": "Cheque 30 días", "Garantía": "1 año",
        "Forma de cotizar": "Por catálogo del proveedor",
        "Contacto Vendedor": "Enzo Garrido / +56 9 3262 2274", "Email": "franklinchile@fele.com",
        "Instrucción de cotización": "Ingresar código del kit",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "FRANKLIN", "Marca": "Franklin", 
        "Línea de Producto": "Motores sumergibles encapsulados",
        "Modelo Base": "Motores 4\", 6\", 8\" encapsulados NEMA", "Procedencia": "EE.UU.", 
        "% Desc. Proveedor": 0.45, "Forma de Pago": "Cheque 30 días", "Garantía": "1 año",
        "Forma de cotizar": "Por catálogo del proveedor",
        "Contacto Vendedor": "Enzo Garrido / +56 9 3262 2274", "Email": "franklinchile@fele.com",
        "Instrucción de cotización": "Enviar parte exacta a cotizar",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "FRANKLIN", "Marca": "Franklin", 
        "Línea de Producto": "Estanques hidroneumáticos",
        "Modelo Base": "Acero pintado 24L, 60L, 100L, 200L", "Procedencia": "EE.UU.", 
        "% Desc. Proveedor": "Cotizar", "Forma de Pago": "Cheque 30 días", "Garantía": "1 año",
        "Forma de cotizar": "Por catálogo del proveedor",
        "Contacto Vendedor": "Enzo Garrido / +56 9 3262 2274", "Email": "franklinchile@fele.com",
        "Instrucción de cotización": "Confirmar SKU con vendedor",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "FRANKLIN", "Marca": "Franklin", 
        "Línea de Producto": "Accesorios",
        "Modelo Base": "Tableros, conectores, protecciones, sellos", "Procedencia": "EE.UU.", 
        "% Desc. Proveedor": "Cotizar", "Forma de Pago": "Cheque 30 días", "Garantía": "1 año",
        "Forma de cotizar": "Por catálogo del proveedor",
        "Contacto Vendedor": "Enzo Garrido / +56 9 3262 2274", "Email": "franklinchile@fele.com",
        "Instrucción de cotización": "Cotizar con SKU o descripción",
        "Stock": "Confirmar stock"
    },

    # =============================================
    # ESPA - Bombas y Equipos
    # =============================================
    {
        "Proveedor": "ESPA", "Marca": "ESPA",
        "Línea de Producto": "Bombas centrífugas, multietapas, presurización y riego",
        "Modelo Base": "AQUACONTROL / MULTI / TECNOPRES / PRISMA", "Procedencia": "España", "% Desc. Proveedor": 0.40,
        "Forma de Pago": "Cheques 30 días", "Condición de pago por monto": "sobre 1MM / 2 cheques / sobre 2MM 3 cheques",
        "Garantía": "1 año", "Buscar Precio en": "Lista de precios interna ESPA", "Descuento Extra > 1.5MM": "No",
        "Monto Activación": 0, "Entrega con despacho": "2 días hábiles",
        "Contacto Vendedor": "ESPA CHILE / +56 2 2903 8000",
        "Email": "contacto@espachile.cl",
        "Web": "https://www.espachile.cl",
        "Datos APP": "Consultar lista de precios enviada por el proveedor"
    },
 
    # =============================================
    # HCP (Todos los modelos completos)
    # =============================================
    {
        "Proveedor": "HCP", "Marca": "HCP", 
        "Línea de Producto": "Aguas Servidas",
        "Modelo Base": "Serie AF", "Procedencia": "Taiwanesa", "% Desc. Proveedor": 0.30,
        "Forma de Pago": "Cheque 30 días", "Garantía": "1 año", 
        "Forma de cotizar": "Catálogo PDF + WhatsApp",
        "Contacto Vendedor": "Cristóbal Canales / +56 9 8770 7441", "Email": "N/D",
        "Web/App proveedor": "N/D", "Instrucción de cotización": "Enviar código del modelo",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "HCP", "Marca": "HCP", 
        "Línea de Producto": "Lodo / Sólidos",
        "Modelo Base": "Serie LH / LH-C / LH-G / LH-L", "Procedencia": "Taiwanesa", "% Desc. Proveedor": 0.30,
        "Forma de Pago": "Cheque 30 días", "Garantía": "1 año", 
        "Forma de cotizar": "Catálogo PDF + WhatsApp",
        "Contacto Vendedor": "Cristóbal Canales / +56 9 8770 7441", "Email": "N/D",
        "Instrucción de cotización": "Enviar código del modelo",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "HCP", "Marca": "HCP", 
        "Línea de Producto": "Drenaje / Achique",
        "Modelo Base": "Serie AS / ASP / AL", "Procedencia": "Taiwanesa", "% Desc. Proveedor": 0.30,
        "Forma de Pago": "Cheque 30 días", "Garantía": "1 año", 
        "Forma de cotizar": "Catálogo PDF + WhatsApp",
        "Contacto Vendedor": "Cristóbal Canales / +56 9 8770 7441", "Email": "N/D",
        "Instrucción de cotización": "Enviar código del modelo",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "HCP", "Marca": "HCP", 
        "Línea de Producto": "Trituradoras",
        "Modelo Base": "Serie GR / GT", "Procedencia": "Taiwanesa", "% Desc. Proveedor": 0.30,
        "Forma de Pago": "Cheque 30 días", "Garantía": "1 año", 
        "Forma de cotizar": "Catálogo PDF + WhatsApp",
        "Contacto Vendedor": "Cristóbal Canales / +56 9 8770 7441", "Email": "N/D",
        "Instrucción de cotización": "Enviar código del modelo",
        "Stock": "Confirmar stock"
    },
    {
        "Proveedor": "HCP", "Marca": "HCP", 
        "Línea de Producto": "Contra incendios",
        "Modelo Base": "Serie FC", "Procedencia": "Taiwanesa", "% Desc. Proveedor": 0.30,
        "Forma de Pago": "Cheque 30 días", "Garantía": "1 año", 
        "Forma de cotizar": "Catálogo PDF + WhatsApp",
        "Contacto Vendedor": "Cristóbal Canales / +56 9 8770 7441", "Email": "N/D",
        "Instrucción de cotización": "Enviar código del modelo",
        "Stock": "Confirmar stock"
    }
]

# Convertir a DataFrame
df_proveedores = pd.DataFrame(PROVEEDORES)
df_margenes = pd.DataFrame(MARGENES)

# =================================================================================
# FUNCIONES PRINCIPALES
# =================================================================================
def calcular_margen(costo):
    """Determina el margen basado en los nuevos rangos."""
    costo = round(costo)  # 👈 redondea para que encaje bien en los tramos
    for _, row in df_margenes.iterrows():
        if row['Min'] <= costo <= row['Max']:
            return row['Margen']
    return df_margenes['Margen'].iloc[-1]  # 👈 usa el último margen como respaldo

def valor_valido(valor):
    """Retorna True si el dato existe y no es NaN/N/D."""
    return pd.notna(valor) and str(valor).strip() not in ["", "N/D", "nan", "None"]

def generar_link_contacto(producto):
    """Genera link de WhatsApp o email según el proveedor."""
    contacto = producto.get('Contacto Vendedor', '')
    forma_cotizar = producto.get('Forma de cotizar', '')

    if valor_valido(contacto) and "WhatsApp" in str(forma_cotizar):
        numero = str(contacto).split('+')[-1].strip().replace(' ', '')
        return f"https://wa.me/{numero}"
    elif valor_valido(producto.get('Email')):
        return f"mailto:{producto['Email']}"
    return None

def obtener_web(producto):
    """Busca la web aunque el proveedor use distintas claves en la matriz."""
    for campo in ['Web/App proveedor', 'Web PGIC', 'Web']:
        valor = producto.get(campo)
        if valor_valido(valor):
            return valor
    return None

# =================================================================================
# INTERFAZ DE USUARIO (STREAMLIT)
# =================================================================================
st.title("📊 Cotizador Grupo Proservices By Rodrigo Muñoz")
st.markdown("---")

# Sidebar: Filtros
with st.sidebar:
    st.header("🔍 Filtros")
    proveedor = st.selectbox("Proveedor", df_proveedores['Proveedor'].unique())
    
    # Filtros anidados
    marcas = df_proveedores[df_proveedores['Proveedor'] == proveedor]['Marca'].unique()
    marca = st.selectbox("Marca", marcas)
    
    lineas = df_proveedores[(df_proveedores['Proveedor'] == proveedor) & 
                           (df_proveedores['Marca'] == marca)]['Línea de Producto'].unique()
    linea = st.selectbox("Línea de Producto", lineas)
    
    # Obtener productos que coinciden con proveedor, marca y línea
    productos_filtrados = df_proveedores[
        (df_proveedores['Proveedor'] == proveedor) & 
        (df_proveedores['Marca'] == marca) & 
        (df_proveedores['Línea de Producto'] == linea)
    ]

    # Si hay más de un modelo dentro de la misma línea, permitir seleccionarlo
    if len(productos_filtrados) > 1:
        modelos = productos_filtrados['Modelo Base'].fillna('Sin modelo definido').astype(str).tolist()
        modelo_seleccionado = st.selectbox("Modelo / Serie", modelos)
        producto = productos_filtrados[
            productos_filtrados['Modelo Base'].fillna('Sin modelo definido').astype(str) == modelo_seleccionado
        ].iloc[0].to_dict()
    else:
        producto = productos_filtrados.iloc[0].to_dict()

# Sección principal
st.subheader(f"📦 {producto['Marca']} - {producto['Línea de Producto']}")
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📋 Especificaciones")
    st.write(f"**Proveedor:** {producto['Proveedor']}")
    st.write(f"**Modelo:** {producto['Modelo Base']}")
    st.write(f"**Procedencia:** {producto['Procedencia']}")
    st.write(f"**Garantía:** {producto['Garantía']}")
    
    # Mostrar contacto (con link si es posible)
    contacto_link = generar_link_contacto(producto)
    if contacto_link:
        st.markdown(f"**Contacto:** [📩 {producto['Contacto Vendedor']}]({contacto_link})")
    else:
        st.write(f"**Contacto:** {producto['Contacto Vendedor']}")

    # Mostrar sitio web del proveedor (si existe)
    web_proveedor = obtener_web(producto)
    if web_proveedor:
        st.markdown(f"🌐 **Sitio del proveedor:** [Abrir]({web_proveedor})")

    # Mostrar datos de acceso (si existen)
    if valor_valido(producto.get('Datos APP')):
        st.markdown(f"🔑 **Datos de acceso:** {producto['Datos APP']}")


with col2:
    st.markdown("### 💵 Precios")
    precio_lista = st.number_input("Precio de lista (CLP):", min_value=0, step=1000)
    
    if precio_lista > 0:
        # Calcular descuentos
        descuento_es_numerico = isinstance(producto['% Desc. Proveedor'], (int, float)) and pd.notna(producto['% Desc. Proveedor'])
        descuento_proveedor = float(producto['% Desc. Proveedor']) if descuento_es_numerico else 0
        precio_con_descuento = precio_lista * (1 - descuento_proveedor)
        
        # Costo final: se aplica únicamente el descuento normal del proveedor
        precio_final = precio_con_descuento

        # Calcular margen real y precio de venta aplicando factor correcto
        margen = calcular_margen(precio_lista)
        precio_venta = precio_final / (1 - margen)

 

        # Mostrar resumen de cotización con todos los datos solicitados
        st.markdown("### 🧾 Resumen de Cotización")

        # Precio lista ingresado por usuario
        st.info(f"**Precio de lista (ingresado por el usuario):** ${precio_lista:,.0f} CLP")

        # Descuento del proveedor
        if descuento_es_numerico:
            st.info(f"**Porcentaje de descuento del proveedor:** {descuento_proveedor * 100:.2f}%")
        else:
            st.warning("**Descuento del proveedor:** Cotizar valor final con vendedor (no se aplica descuento automático).")

        # Costo real
        st.success(f"**Costo del producto (con descuento proveedor):** ${precio_final:,.0f} CLP")

        # Margen aplicado
        st.success(f"**Margen de ganancia Proservices aplicado:** {margen*100:.1f}%")

        # Precio de venta sugerido
        st.success(f"**Precio de venta sugerido (neto al cliente):** ${precio_venta:,.0f} CLP")

        # Descuento al cliente visible
        descuento_visible = 1 - (precio_venta / precio_lista)
        st.error(f"**Descuento a mostrar en la cotización:** {descuento_visible*100:.2f}%")

      


# Gráfico de nuevos márgenes (sidebar)
with st.sidebar:
    st.markdown("### 📊 Márgenes 2026")
    fig, ax = plt.subplots(figsize=(5, 3))
    ax.bar(df_margenes['Tramo'], df_margenes['Margen'] * 100, color='#4CAF50')
    ax.set_ylabel("Margen (%)")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown(f"**Proservices** - © {datetime.now().year} | Versión GrupoProservices by Rodrigo Muñoz 2026")


