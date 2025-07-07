from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline


STAGE_NAME ="Data Ingestion Stage"
try:
        logger.info(f">>>> stage{STAGE_NAME} started <<<<")
        obj = DataIngestionTraningPipeline()
        obj.main()
        logger.info(f">>> stag{STAGE_NAME} COMPLETED <<<<<\n\n x======x")
except Exception as e:
        logger.exception(e)
        raise e  