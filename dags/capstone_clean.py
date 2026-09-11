from datetime import datetime

from airflow import DAG
from airflow.models import Variable
from airflow.providers.docker.operators.docker import DockerOperator

TAG = "pyspark"
USER = "ahmed-youssef1"

default_args = {
    "owner": "airflow",
    "retries": 0,
}

with DAG(
    "capstone_clean",
    default_args=default_args,
    description="Clean StackOverflow data and write it to S3",
    start_date=datetime(2024, 1, 1),
    schedule=None,  # trigger manually
    catchup=False,
) as dag:
    clean = DockerOperator(
        task_id="clean",
        image="capstone-llm",
        container_name="capstone_clean",
        api_version="auto",
        auto_remove="force",
        command=f"python3 -m capstonellm.tasks.clean --env local --tag {TAG} --user {USER}",
        docker_url="unix://var/run/docker.sock",
        network_mode="bridge",
        mount_tmp_dir=False,
        # pass AWS credentials into the container so it can read/write S3
        environment={
        },
    )
