# Ml-with-flow
import dagshub
dagshub.init(repo_owner='gehlotatharv3', repo_name='Ml-with-flow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)

  Dags@2026#

export MLFLOW_TRACKING_URI = https://dagshub.com/gehlotatharv3/Ml-with-flow.mlflow/
MLFLOW_TRACKING_USERNAME = gehlotatharv3
MLFLOW_TRACKING_PASSWORD = Dags@2026#