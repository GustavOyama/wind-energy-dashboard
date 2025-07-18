from src.extract import fetch_geojson_data
from src.transform import add_lat_lon, validate_clean
from src.load import save_geojson, load_geojson, export_to_csv

from pathlib import Path

# 📁 Diretórios
DATA_DIR = Path("data")
RAW_PATH = DATA_DIR / "raw" / "aerogeradores.geojson"
PROCESSED_PATH = DATA_DIR / "processed" / "outputs.csv"

def main():
    # Etapa 1: Extração
    print("🔍 Iniciando extração de dados da API da ANEEL...")
    geojson_data = fetch_geojson_data()

    if not geojson_data:
        print("❌ Nenhum dado foi extraído. Encerrando o processo.")
        return

    # Etapa 2: Salvando os dados brutos
    print("💾 Salvando dados brutos em GeoJSON...")
    save_geojson(geojson_data, str(RAW_PATH))

    # Etapa 3: Carregando como GeoDataFrame
    print("📂 Carregando dados salvos como GeoDataFrame...")
    gdf = load_geojson(str(RAW_PATH))

    if gdf is None or gdf.empty:
        print("❌ GeoDataFrame vazio ou nulo. Encerrando o processo.")
        return

    # Etapa 4: Transformação
    print("🧪 Realizando transformação dos dados...")
    gdf = validate_clean(gdf)
    gdf = add_lat_lon(gdf)

    # Etapa 5: Exportação para CSV
    print("📤 Exportando dados tratados para CSV...")
    export_to_csv(gdf, str(PROCESSED_PATH))

    print("✅ Pipeline concluída com sucesso!")

if __name__ == "__main__":
    main()
