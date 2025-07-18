# Funções de transformação de dados
import geopandas as gpd

def add_lat_lon(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Adiciona colunas LATITUDE e LONGITUDE convertendo o CRS para WGS84.
    """
    gdf = gdf.to_crs(epsg=4326)
    gdf["LATITUDE"] = gdf.geometry.y
    gdf["LONGITUDE"] = gdf.geometry.x
    return gdf

def validate_clean(gdf: gpd.GeoDataFrame) -> gpd.GeoDataFrame:
    """
    Remove duplicados e geometrias nulas.
    """
    before = len(gdf)
    gdf = gdf.drop_duplicates()
    gdf = gdf[gdf.geometry.notnull()]
    after = len(gdf)
    print(f"🧹 Registros após limpeza: {after} (removidos {before - after})")
    return gdf
