from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngestionTraningPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from mlProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from mlProject.pipeline.stage_04_model_trainer import ModelTrainerTrainingPipeline

STAGE_NAME ="Data Ingestion Stage"
try:
        logger.info(f">>>> stage{STAGE_NAME} started <<<<")
        obj = DataIngestionTraningPipeline()
        obj.main()
        logger.info(f">>> stag{STAGE_NAME} COMPLETED <<<<<\n\n x======x")
except Exception as e:
        logger.exception(e)
        raise e  

STAGE_NAME ="Data Validation Stage"
try:
        logger.info(f">>>> stage{STAGE_NAME} started <<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>> stag{STAGE_NAME} COMPLETED <<<<<\n\n x======x")
except Exception as e:
        logger.exception(e)
        raise e  


STAGE_NAME ="Data Transformation Stage"
try:
        logger.info(f">>>> stage{STAGE_NAME} started <<<<")
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f">>> stag{STAGE_NAME} COMPLETED <<<<<\n\n x======x")
except Exception as e:
        logger.exception(e)
        raise e  


STAGE_NAME ="Model Trainer stage"
try:
        logger.info(f">>>> stage{STAGE_NAME} started <<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>> stag{STAGE_NAME} COMPLETED <<<<<\n\n x======x")
except Exception as e:
        logger.exception(e)
        raise e  

