import os
import requests
import zipfile 
from pathlib import Path
from drink_quality_prediction import logger
from drink_quality_prediction.utils.common import get_size
from drink_quality_prediction.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            response = requests.get(self.config.source_URL, stream=True)
            response.raise_for_status()

            with open(self.config.local_data_file, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)

            logger.info(f"Downloaded successfully: {self.config.local_data_file}")

        else:
            logger.info(
                f"File already exists of size: {get_size(Path(self.config.local_data_file))}"
            )

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
        logger.info(f"File extracted at : {unzip_path} and size is : {get_size(Path(unzip_path))}")