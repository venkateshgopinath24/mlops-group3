# mlops-group3
Repository for MLOps Project

Folder Structure 
================

> The project structure is described as follows:

    .
    ├── data                    # Data Collected (alternatively `dataset`)
    ├── docs                    # Documentation files (alternatively `doc`)
    ├── environments_setup      # Setup files for GCP (alternatively `setup` or `build`)
    ├── images                  # Images used (alternatively `assets`)
    ├── models                  # Models used
    ├── src                     # Source files (alternatively `lib` or `app`)
    ├── pipeline                # Code to run the airflow pipeline in Docker
    ├── LICENSE
    └── README.md


## Steps to run the Pipeline

- Move to the **pipeline** directory
- With the **pipeline** directory as your working directory, run the following command to start airflow in docker one after the other:

```bash
docker compose up airflow-init
```
This command initializes the database and services needed to start and run the airflow webserver, scheduler, etc.

```bash
docker compose up
```
This service starts the airflow services in various containers.
To open the Airflow UI, open the following link in your browser:
[http://0.0.0.0:8080/home](http://0.0.0.0:8080/home)

### How to contribute to the the pipeline (How to develop your own dags)

The dags, logs, plugins and secrets folders are copied into the container and are updated in real-time. Any changes you make to the files inside these folders will reflect inside the container.

So by modifying the code inside the dags folder, we can add and develop varous dags. For instance, we can add a new dag which can download the data and preprocess it inside the dags folder and it will automatically be picked up airflow's services.