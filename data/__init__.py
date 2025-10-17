"""
Módulo de datos para TechComView SA

Contiene datasets de telecomunicaciones para países de América Latina y el Caribe.
"""

import pandas as pd
import os
from typing import Optional, Dict, Any

# Configuración de archivos de datos
DATA_FILES = {
    "expanded": "expanded_telecom_data.csv",
    "original": "south_america_cells.csv"
}

def get_data_path(filename: str) -> str:
    """
    Obtiene la ruta completa de un archivo de datos.
    
    Args:
        filename: Nombre del archivo
        
    Returns:
        Ruta completa del archivo
    """
    current_dir = os.path.dirname(__file__)
    return os.path.join(current_dir, filename)

def load_expanded_data() -> Optional[pd.DataFrame]:
    """
    Carga el dataset expandido con 28 países.
    
    Returns:
        DataFrame con datos expandidos o None si hay error
    """
    try:
        file_path = get_data_path(DATA_FILES["expanded"])
        if os.path.exists(file_path):
            return pd.read_csv(file_path)
        return None
    except Exception:
        return None

def load_original_data() -> Optional[pd.DataFrame]:
    """
    Carga el dataset original con 10 países de Sudamérica.
    
    Returns:
        DataFrame con datos originales o None si hay error
    """
    try:
        file_path = get_data_path(DATA_FILES["original"])
        if os.path.exists(file_path):
            return pd.read_csv(file_path)
        return None
    except Exception:
        return None

def get_available_datasets() -> Dict[str, bool]:
    """
    Verifica qué datasets están disponibles.
    
    Returns:
        Diccionario con estado de cada dataset
    """
    return {
        "expanded": os.path.exists(get_data_path(DATA_FILES["expanded"])),
        "original": os.path.exists(get_data_path(DATA_FILES["original"]))
    }

def get_data_info() -> Dict[str, Any]:
    """
    Obtiene información sobre los datasets disponibles.
    
    Returns:
        Diccionario con información de los datasets
    """
    info = {
        "available_datasets": get_available_datasets(),
        "total_countries": 0,
        "regions": set(),
        "technologies": ["2G", "3G", "4G", "5G"]
    }
    
    # Intentar cargar datos expandidos primero
    df = load_expanded_data()
    if df is None:
        df = load_original_data()
    
    if df is not None:
        info["total_countries"] = len(df)
        if "region" in df.columns:
            info["regions"] = set(df["region"].unique())
    
    return info
