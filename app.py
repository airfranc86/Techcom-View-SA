"""
TechComView SA - Dashboard Interactivo
Aplicación completa con todas las funcionalidades en una sola página
"""

import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from typing import List, Dict, Union, cast


# Configuración de la página
st.set_page_config(
    page_title="TechComView SA - Panel Interactivo",
    page_icon="📡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Cargar datos con caché
@st.cache_data
def load_data():
    """Carga datos expandidos de torres celulares de América Latina"""
    try:
        # Intentar cargar dataset expandido
        df = pd.read_csv('data/expanded_telecom_data.csv')
        st.success(f"✅ Dataset expandido cargado: {len(df)} países")
        return df
    except FileNotFoundError:
        # Fallback a datos hardcodeados originales
        st.info("📊 Usando dataset original (10 países)")
        data = {
            'country': ['Argentina', 'Bolivia', 'Brasil', 'Chile', 'Colombia',
                       'Ecuador', 'Paraguay', 'Perú', 'Uruguay', 'Venezuela'],
            'total_cells': [327143, 56487, 1903025, 208660, 285266,
                           85699, 50093, 204598, 28974, 101353],
            'gsm': [55074, 11131, 330817, 32244, 68817,
                   23942, 8737, 43202, 6376, 27667],
            'umts': [211738, 36367, 1268672, 140895, 178647,
                    52415, 36814, 121898, 18716, 69319],
            'lte': [60331, 8987, 303366, 35521, 37798,
                   9337, 4542, 39498, 3882, 4108],
            'nr': [0, 2, 170, 0, 2,
                  0, 0, 0, 0, 0],
            'population_millions': [45.4, 11.8, 215.3, 19.1, 51.5,
                                   17.6, 7.3, 33.0, 3.4, 28.4],
            'latitude': [-34.6118, -16.2902, -14.2350, -35.6751, 4.7110,
                        -1.8312, -23.4425, -9.1900, -32.5228, 6.4238],
            'longitude': [-58.3960, -63.5887, -51.9253, -71.5430, -74.0721,
                         -78.1834, -58.4438, -75.0152, -55.7658, -66.5897],
            'region': ['South America'] * 10
        }
        return pd.DataFrame(data)

# Calcular métricas globales
@st.cache_data
def calculate_metrics(dataframe):
    """Calcula estadísticas agregadas"""
    total_towers = dataframe['total_cells'].sum()
    total_5g = dataframe['nr'].sum()
    total_4g = dataframe['lte'].sum()
    total_3g = dataframe['umts'].sum()
    total_2g = dataframe['gsm'].sum()

    return {
        'total': total_towers,
        '5g': total_5g,
        '4g': total_4g,
        '3g': total_3g,
        '2g': total_2g,
        '5g_pct': (total_5g / total_towers * 100) if total_towers > 0 else 0,
        '4g_pct': (total_4g / total_towers * 100) if total_towers > 0 else 0
    }


# Cargar datos
df = load_data()

# ========== INTERFAZ PRINCIPAL ==========

# Header
st.title("📡 TechComView SA - Dashboard Unificado")
st.markdown("### Análisis Completo de Infraestructura de Telecomunicaciones - América Latina")
st.markdown("---")

# ========== SIDEBAR PROFESIONAL ==========
with st.sidebar:
    # Header con logo y título
    st.markdown("""
    <div style='text-align: center; padding: 1rem 0;'>
        <h2 style='color: #1f77b4; margin: 0;'>📡 TechComView SA</h2>
        <p style='color: #666; margin: 0.5rem 0; font-size: 0.9rem;'>Dashboard Unificado Interactivo</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # Filtros avanzados
    st.markdown("### 🔍 Filtros Avanzados")

    # Filtro por región
    if 'region' in df.columns:
        available_regions = df['region'].unique()
        selected_regions = st.multiselect(
            "🌎 Seleccionar Regiones:",
            options=available_regions,
            default=available_regions,
            help="Selecciona las regiones a analizar"
        )
        
        # Filtrar países por región seleccionada
        if selected_regions:
            available_countries = df[df['region'].isin(selected_regions)]['country'].unique()
        else:
            available_countries = df['country'].unique()
    else:
        available_countries = df['country'].unique()
        selected_regions = []

    # Filtro por país
    selected_countries = st.multiselect(
        "🌍 Seleccionar Países:",
        options=available_countries,
        default=available_countries,
        help="Selecciona los países a analizar"
    )

    # Filtro por tecnología
    tech_filter = st.selectbox(
        "📡 Tecnología Principal:",
        options=['Todas', '2G (GSM)', '3G (UMTS)', '4G (LTE)', '5G (NR)'],
        help="Filtrar por tecnología específica"
    )


    st.markdown("---")

    # Análisis rápido
    st.markdown("### ⚡ Análisis Rápido")

    if st.button("🏆 Top 3 Países", help="Mostrar solo los 3 países con más torres"):
        selected_countries = df.nlargest(3, 'total_cells')['country'].tolist()
        st.rerun()

    if st.button("🚀 Solo 5G", help="Mostrar países con infraestructura 5G"):
        selected_countries = df[df['nr'] > 0]['country'].tolist()
        st.rerun()

    if st.button("📊 Todos", help="Mostrar todos los países"):
        selected_countries = df['country'].unique().tolist()
        st.rerun()

    st.markdown("---")

    # Información del dataset
    st.markdown("### 📋 Información del Dataset")

    with st.expander("🔍 Detalles Técnicos", expanded=False):
        st.markdown("""
        **Fuente:** OpenCelliD
        **Actualización:** Octubre 2025
        **Cobertura:** 28 países
        **Tecnologías:** 2G, 3G, 4G, 5G
        **Precisión:** Datos de torres lógicas
        """)

    with st.expander("📈 Métricas Clave", expanded=False):
        sidebar_5g = df['nr'].sum()
        sidebar_4g = df['lte'].sum()
        sidebar_3g = df['umts'].sum()
        sidebar_2g = df['gsm'].sum()
        total_cells = df['total_cells'].sum()

        st.metric("5G", f"{sidebar_5g:,}", 
                 f"{sidebar_5g/total_cells*100:.2f}%")
        st.metric("4G", f"{sidebar_4g:,}", 
                 f"{sidebar_4g/total_cells*100:.1f}%")
        st.metric("3G", f"{sidebar_3g:,}", 
                 f"{sidebar_3g/total_cells*100:.1f}%")
        st.metric("2G", f"{sidebar_2g:,}", 
                 f"{sidebar_2g/total_cells*100:.1f}%")

    st.markdown("---")

    # Footer
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.8rem;'>
        <p>📡 TechComView SA</p>
        <p>Dashboard Unificado v1.0</p>
    </div>
    """, unsafe_allow_html=True)

# Aplicar filtros del sidebar
filtered_df = df[df['country'].isin(selected_countries)].copy()

# Aplicar filtro por región si está disponible
if selected_regions and 'region' in df.columns:
    filtered_df = filtered_df[filtered_df['region'].isin(selected_regions)].copy()


# Recalcular métricas con datos filtrados
filtered_metrics = calculate_metrics(filtered_df)

# ========== MÉTRICAS PRINCIPALES ==========
st.markdown("## 📊 Resumen Regional")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="🗼 Total Torres",
        value=f"{filtered_metrics['total']:,}",
        delta=f"{len(filtered_df)} países"
    )

with col2:
    st.metric(
        label="📶 Cobertura 5G",
        value=f"{filtered_metrics['5g']:,}",   
    )

with col3:
    st.metric(
        label="📡 Cobertura 4G",
        value=f"{filtered_metrics['4g']:,}",
    )

with col4:
    if not filtered_df.empty and len(filtered_df) > 0:
        max_idx = filtered_df['total_cells'].idxmax()
        leader_country = filtered_df.loc[max_idx, 'country']
        leader_towers = filtered_df['total_cells'].max()
    else:
        leader_country = "N/A"
        leader_towers = 0

    st.metric(
        label="🏆 Líder Regional",
        value=leader_country,
        delta=f"{leader_towers:,} torres"
    )

st.markdown("---")

# ========== VISUALIZACIONES ==========

col_left, col_right = st.columns(2)

with col_left:
    st.markdown("### 🏅 Top Países - Total de Torres")

    # Ordenar y tomar top países (máximo 5)
    top_countries = filtered_df.nlargest(min(5, len(filtered_df)), 'total_cells')

    if not top_countries.empty:
        # Gráfico de barras
        fig_bar = px.bar(
            top_countries,
            x='total_cells',
            y='country',
            orientation='h',
            color='total_cells',
            color_continuous_scale='Blues',
            labels={'total_cells': 'Antenas', 'country': 'País'}
        )
        fig_bar.update_layout(
            showlegend=False,
            height=400,
            yaxis={'categoryorder': 'total ascending'},
            width=None  # Eliminar width explícitamente
        )
        st.plotly_chart(fig_bar, use_container_width=True, config={
            'displayModeBar': True,
            'displaylogo': False,
            'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
        })
    else:
        st.info("No hay datos que coincidan con los filtros seleccionados")

with col_right:
    st.markdown("### 📡 Distribución por Tecnología")

    # Preparar datos para gráfico de torta
    tech_data = {
        'Tecnología': ['2G (GSM)', '3G (UMTS)', '4G (LTE)', '5G (NR)'],
        'Torres': [filtered_metrics['2g'], filtered_metrics['3g'], filtered_metrics['4g'], filtered_metrics['5g']]
    }
    tech_df = pd.DataFrame(tech_data)

    # Gráfico de torta
    fig_pie = px.pie(
        tech_df,
        values='Torres',
        names='Tecnología',
        color_discrete_sequence=px.colors.sequential.RdBu
    )
    fig_pie.update_traces(textposition='inside', textinfo='percent+label')
    fig_pie.update_layout(height=400, width=None)  # Eliminar width explícitamente
    st.plotly_chart(fig_pie, use_container_width=True, config={
        'displayModeBar': True,
        'displaylogo': False,
        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
    })

st.markdown("---")

# ========== MAPA INTERACTIVO ==========
st.markdown("## 🗺️ Mapa Interactivo")

# Configuración fija del mapa
color_scale = 'Turbo'
map_style = 'carto-darkmatter'

if not filtered_df.empty and 'latitude' in filtered_df.columns and 'longitude' in filtered_df.columns:
    # Determinar columna de datos según filtro
    size_col = 'total_cells'
    title_suffix = 'Total de Antenas'

    if tech_filter == '2G (GSM)':
        size_col = 'gsm'
        title_suffix = 'Antenas 2G'
    elif tech_filter == '3G (UMTS)':
        size_col = 'umts'
        title_suffix = 'Antenas 3G'
    elif tech_filter == '4G (LTE)':
        size_col = 'lte'
        title_suffix = 'Antenas 4G'
    elif tech_filter == '5G (NR)':
        size_col = 'nr'
        title_suffix = 'Antenas 5G'

    # Crear gráfico de dispersión geográfico
    fig_map = px.scatter_mapbox(
        filtered_df,
        lat='latitude',
        lon='longitude',
        size=size_col,
        color=size_col,
        hover_name='country',
        hover_data={
            'total_cells': True,
            'gsm': True,
            'umts': True,
            'lte': True,
            'nr': True,
            'latitude': False,
            'longitude': False
        },
        color_continuous_scale=color_scale,
        size_max=60,
        mapbox_style=map_style,
        zoom=3,
        center={'lat': -15, 'lon': -60},
        title=f"Mapa de {title_suffix} en {selected_regions[0]}",
        labels={size_col: 'Antenas'}
    )

    fig_map.update_layout(
        height=600,
        width=None,  # Eliminar width explícitamente
        margin={'r': 0, 't': 30, 'l': 0, 'b': 0},
        coloraxis_colorbar=dict(
            title="Antenas",
            tickmode="linear",
            tick0=0,
            dtick=50000,
            len=0.8,
            thickness=20,
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="rgba(0,0,0,0.2)",
            borderwidth=1
        )
    )

    st.plotly_chart(fig_map, use_container_width=True, config={
        'displayModeBar': True,
        'displaylogo': False,
        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
    })
else:
    st.info("No hay datos de coordenadas disponibles para mostrar el mapa")

st.markdown("---")

# ========== COMPARATIVAS ==========
st.markdown("## 📈 Comparativas entre Países")

comparison_type = st.selectbox(
    "Tipo de comparación:",
    options=['Total de Torres', 'Por Tecnología', 'Por Población', 'Ranking 5G']
)

if comparison_type == 'Total de Torres':
    st.markdown("### 📊 Comparativa Total de Torres")

    # Gráfico de barras
    fig = px.bar(
        filtered_df,
        x='country',
        y='total_cells',
        title="Total de Antenas por País",
        color='total_cells',
        color_continuous_scale='Blues',
        labels={'total_cells': 'Total de Antenas', 'country': 'País'}
    )
    fig.update_layout(height=500, width=None)  # Eliminar width explícitamente
    st.plotly_chart(fig, use_container_width=True, config={
        'displayModeBar': True,
        'displaylogo': False,
        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
    })

elif comparison_type == 'Por Tecnología':
    st.markdown("### 📡 Comparativa por Tecnología")

    # Gráfico de barras apiladas
    tech_data = filtered_df[['country', 'gsm', 'umts', 'lte', 'nr']].set_index('country')

    fig = px.bar(
        tech_data.T,
        title="Distribución de Tecnologías por País",
        labels={'value': 'Número de Antenas', 'index': 'Tecnología'},
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig.update_layout(height=500, width=None)  # Eliminar width explícitamente
    st.plotly_chart(fig, use_container_width=True, config={
        'displayModeBar': True,
        'displaylogo': False,
        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
    })

elif comparison_type == 'Por Población':
    st.markdown("### 👥 Análisis por Población")
    
    if 'population_millions' in filtered_df.columns:
        # Calcular densidad de torres por millón de habitantes
        filtered_df['towers_per_million'] = (filtered_df['total_cells'] / filtered_df['population_millions']).round(0)

        # Gráfico de dispersión
        fig = px.scatter(
            filtered_df,
            x='population_millions',
            y='towers_per_million',
            size='total_cells',
            color='country',
            title="Densidad de Antenas vs Población",
            labels={
                'population_millions': 'Población (millones)',
                'towers_per_million': 'Antenas por millón de habitantes'
            },
            hover_data=['total_cells', 'gsm', 'umts', 'lte', 'nr']
        )
        fig.update_layout(height=500, width=None)  # Eliminar width explícitamente
        st.plotly_chart(fig, use_container_width=True, config={
        'displayModeBar': True,
        'displaylogo': False,
        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
    })
    else:
        st.info("No hay datos de población disponibles")

elif comparison_type == 'Ranking 5G':
    st.markdown("### 🚀 Ranking de Infraestructura 5G")

    # Ordenar por 5G
    g5_ranking = filtered_df.sort_values('nr', ascending=False)

    # Gráfico de barras 5G
    fig = px.bar(
        g5_ranking,
        x='country',
        y='nr',
        title="Infraestructura 5G por País",
        color='nr',
        color_continuous_scale='Purples',
        labels={'nr': 'Antenas 5G', 'country': 'País'}
    )
    fig.update_layout(height=500, width=None)  # Eliminar width explícitamente
    st.plotly_chart(fig, use_container_width=True, config={
        'displayModeBar': True,
        'displaylogo': False,
        'modeBarButtonsToRemove': ['pan2d', 'lasso2d', 'select2d']
    })

st.markdown("---")

# ========== TABLA DETALLADA ==========
st.markdown("### 📋 Datos Detallados por País")

if not filtered_df.empty:
    # Preparar tabla para mostrar
    display_df = filtered_df.copy()
    
    # Seleccionar columnas base que siempre existen
    base_columns = ['country', 'total_cells', 'gsm', 'umts', 'lte', 'nr']
    columns_to_show = [col for col in base_columns if col in display_df.columns]
    
    # Agregar población si está disponible
    if 'population_millions' in display_df.columns:
        columns_to_show.append('population_millions')
    
    # Crear DataFrame con solo las columnas disponibles
    display_df = display_df[columns_to_show].copy()
    
    # Crear nombres de columnas dinámicamente
    column_names = ['País', 'Total de Antenas', '2G', '3G', '4G', '5G']
    if 'population_millions' in columns_to_show:
        column_names.append('Población (M)')
    
    display_df.columns = column_names
    display_df = display_df.sort_values('Total de Antenas', ascending=False)
    
    # Formatear números con separadores de miles
    for col in ['Total de Antenas', '2G', '3G', '4G', '5G']:
        if col in display_df.columns:
            display_df[col] = display_df[col].apply(lambda x: f"{x:,}")
    
    # Formatear población si existe
    if 'Población (M)' in display_df.columns:
        display_df['Población (M)'] = display_df['Población (M)'].apply(lambda x: f"{x:.1f}M")
    
    
    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )
else:
    st.warning("⚠️ No hay datos que coincidan con los filtros seleccionados")
    st.info("💡 Intenta ajustar los filtros en el sidebar para ver más países")

# ========== INSIGHTS ==========
st.markdown("---")
st.markdown("### 💡 Insights Clave")

col1, col2, col3 = st.columns(3)

with col1:
    if not filtered_df.empty and len(filtered_df) > 0:
        # Obtener el índice del país con más torres
        max_idx = filtered_df['total_cells'].idxmax()
        leader = filtered_df.loc[max_idx]
        leader_pct = (leader['total_cells'] / filtered_metrics['total'] * 100) if filtered_metrics['total'] > 0 else 0
        st.success(f"""
        **{leader['country']} domina la selección**
        - {leader_pct:.1f}% del total de antenas
        - {leader['nr']:,} antenas 5G
        """)
    else:
        st.info("No hay datos para mostrar")

with col2:
    if filtered_metrics['5g'] > 0:
        st.warning(f"""
        **5G en desarrollo**
        - {filtered_metrics['5g']:,} antenas 5G en selección
        - {filtered_metrics['5g_pct']:.2f}% del total
        """)
    else:
        st.warning("**Sin infraestructura 5G** en la selección actual")

with col3:
    dominant_tech = max(['2g', '3g', '4g', '5g'], key=lambda x: filtered_metrics[x])
    dominant_pct = (filtered_metrics[dominant_tech] / filtered_metrics['total'] * 100) if filtered_metrics['total'] > 0 else 0
    tech_names = {'2g': '2G', '3g': '3G', '4g': '4G', '5g': '5G'}
    st.info(f"""
    **{tech_names[dominant_tech]} es dominante**
    - {dominant_pct:.1f}% de la infraestructura
    - Tecnología más desplegada
    """)

# ========== FOOTER ==========
st.markdown("---")
st.caption("📡 TechComView SA | Datos: OpenCelliD | Dashboard Unificado v2.1.0")
st.caption("Todas las funcionalidades integradas en una sola interfaz interactiva")
