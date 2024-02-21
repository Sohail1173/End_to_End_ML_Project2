import sys
from Xray.components.data_ingestion import DataIngestionn
from Xray.entity.artifact_entity import DataIngestionArtifact
from Xray.entity.config_entity import DataIngestionConfig
from Xray.exception import XrayException
from Xray.logger import logging


class TrainPipeline:
    def __init__(self):

        self.data_ingestion_config=DataIngestionConfig()

        def start_data_ingestion(self) ->DataIngestionArtifact:
            logging.info("Entered the start_data_ingestion method of ")