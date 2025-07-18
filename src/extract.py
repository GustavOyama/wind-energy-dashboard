# Funções de extração de dados
import requests

def fetch_geojson_data(
    url: str = "https://sigel.aneel.gov.br/arcgis/rest/services/PORTAL/WFS/MapServer/0/query",
    batch_size: int = 1000,
    timeout: int = 30,
) -> dict:
    all_features = []
    offset = 0

    while True:
        params = {
            "where": "1=1",
            "outFields": "*",
            "f": "geojson",
            "resultOffset": offset,
            "resultRecordCount": batch_size
        }

        try:
            print(f" Coletando registros a partir do offset {offset}...")
            response = requests.get(url, params=params, timeout=timeout)
            response.raise_for_status()
            data = response.json()
            features = data.get("features", [])

            if not features:
                print(" Coleta concluída.")
                break

            all_features.extend(features)
            offset += batch_size

        except requests.exceptions.RequestException as e:
            print(f" Erro na página {offset}: {e}")
            break

    print(f" Total de registros coletados: {len(all_features)}")
    return {"type": "FeatureCollection", "features": all_features} if all_features else None
