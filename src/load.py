# Funções de carregamento de dados
import json
import os
import geopandas as gpd

def save_geojson(data: dict, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"📁 GeoJSON salvo em {path}")

def export_to_csv(gdf: gpd.GeoDataFrame, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    try:
        df = gdf.drop(columns=["X", "Y", "VERSAO", "geometry"],errors="ignore")
        df.to_csv(path, index=False)
        print(f"💾 CSV salvo em {path}")
    except Exception as e:
        print(f"❌ Erro ao salvar CSV: {e}")


def load_geojson(path: str) -> gpd.GeoDataFrame:
    try:
        gdf = gpd.read_file(path)
        print(f"📊 GeoDataFrame carregado com {len(gdf)} registros.")
        return gdf
    except Exception as e:
        print(f"❌ Erro ao carregar GeoJSON: {e}")
        return None

