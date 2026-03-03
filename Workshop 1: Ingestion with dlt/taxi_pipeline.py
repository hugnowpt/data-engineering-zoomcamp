import dlt
import requests

BASE_URL = "https://us-central1-dlthub-analytics.cloudfunctions.net/data_engineering_zoomcamp_api"

@dlt.resource(name="nyc_taxi_data")
def taxi_data():
    page = 1

    while True:
        response = requests.get(BASE_URL, params={"page": page})
        response.raise_for_status()

        data = response.json()

        if not data:
            break

        yield data
        page += 1


def run_pipeline():
    pipeline = dlt.pipeline(
        pipeline_name="taxi_pipeline",
        destination="duckdb",
        dataset_name="nyc_taxi"
    )

    load_info = pipeline.run(taxi_data())
    print(load_info)


if __name__ == "__main__":
    run_pipeline()