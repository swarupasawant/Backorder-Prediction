from Backorder.entity.config_entity import DataIngestionConfig
from Backorder.config.configuration import Configuration
from Backorder.component.data_ingestion import DataIngestion
import sys,os
from Backorder.exception import BackorderException
from Backorder.logger import logging
from Backorder.entity.artifact_entity import DataIngestionArtifact



class Pipeline:
    # experiment: Experiment = Experiment(*([None] * 11))
    # experiment_file_path = None

    def __init__(self, config: Configuration = Configuration() ) -> None:
        try:
            self.config = config
        except Exception as e:
            raise BackorderException(e, sys) from e

    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            print(24,data_ingestion)
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise BackorderException(e, sys) from e

    def run_pipeline(self):
        try:
            # data_ingestion
            data_ingestion_artifact = self.start_data_ingestion()
        except Exception as e:
            raise BackorderException(e, sys) from e
