"""
TechComView SA - Dashboard Interactivo de Telecomunicaciones

Dashboard unificado para análisis de infraestructura de telecomunicaciones
en América Latina y el Caribe.

Autor: TechComView SA
Versión: 2.1.0 - MVP MIT
"""

__version__ = "2.1.0"
__author__ = "TechComView SA"
__email__ = "franciscoaucar@ajconsultingit.com"
__license__ = "MIT"
__description__ = "Dashboard interactivo para análisis de infraestructura de telecomunicaciones"

# Imports principales
import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración por defecto
DEFAULT_CONFIG = {
    "page_title": "TechComView SA - Dashboard Unificado",
    "page_icon": "📡",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Información del proyecto
PROJECT_INFO = {
    "name": "TechComView SA",
    "version": __version__,
    "description": __description__,
    "author": __author__,
    "license": __license__,
    "repository": "https://github.com/airfranc86/Techcom-View-SA",
    "documentation": "https://github.com/airfranc86/Techcom-View-SA#readme"
}

# Configuración de datos
DATA_CONFIG = {
    "supported_regions": [
        "South America",
        "Central America", 
        "Caribbean",
        "North America"
    ],
    "supported_technologies": ["2G", "3G", "4G", "5G"],
    "data_columns": [
        "country", "total_cells", "gsm", "umts", "lte", "nr",
        "population_millions", "latitude", "longitude", "region"
    ]
}

# Configuración del mapa
MAP_CONFIG = {
    "default_color_scale": "Turbo",
    "default_map_style": "carto-darkmatter",
    "default_zoom": 3,
    "default_center": {"lat": -15, "lon": -60}
}

def get_version():
    """Retorna la versión del proyecto."""
    return __version__

def get_project_info():
    """Retorna información completa del proyecto."""
    return PROJECT_INFO.copy()

def get_data_config():
    """Retorna configuración de datos."""
    return DATA_CONFIG.copy()

def get_map_config():
    """Retorna configuración del mapa."""
    return MAP_CONFIG.copy()

# Mensaje de bienvenida
def welcome_message():
    """Muestra mensaje de bienvenida del proyecto."""
    return f"""
    🚀 Bienvenido a {PROJECT_INFO['name']} v{__version__}
    
    📡 Dashboard interactivo para análisis de telecomunicaciones
    🌍 {len(DATA_CONFIG['supported_regions'])} regiones soportadas
    📊 {len(DATA_CONFIG['supported_technologies'])} tecnologías analizadas
    
    🔗 Repositorio: {PROJECT_INFO['repository']}
    📄 Licencia: {PROJECT_INFO['license']}
    """
