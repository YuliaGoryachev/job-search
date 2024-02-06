# Job Search Enhanced

A prototype to simplify job search with Linkedin jobs.
The first step is to download the job descriptions from Linkedin.
Since Linkedin doesn't allow scraping and doesn't even have a free API, I had to use a chrome extension.
The steps are:
1. Install the `jobs scraper extension` https://chromewebstore.google.com/detail/jobs-scraper-for-linkedin/jhmlphenakpfjkieogpinommlgjdjnhb
2. Activate the extension - 1st it will ask you to register
3. Do a search in Linkedin
4. If the extension is activated, a green button “Download Jobs” is visible. 
5. Click “Download jobs”. 
6. A window will appear. When jobs are ready, click “Export jobs” - it will download a csv file

Note that it will download only 20 first jobs. If you need more, close the first 20 jobs and go back to the previous step. 
Repeat until got the needed number of jobs.

After downloading the jobs, you add extra features, like skills and salary, see the notebook `notebooks/01-Data-Preparation.ipynb`

## Development Requirements

- Python3.11.0
- Pip
- Poetry (Python Package Manager)

### M.L Model Environment

```sh
MODEL_PATH=./ml/model/
MODEL_NAME=model.pkl
```

### Update `/predict`

To update your machine learning model, add your `load` and `method` [change here](app/api/routes/predictor.py#L19) at `predictor.py`

## Installation

```sh
python -m venv venv
source venv/bin/activate
make install
```

## Runnning Localhost

`make run`

## Deploy app

`make deploy`

## Running Tests

`make test`

## Access Swagger Documentation

> <http://localhost:8080/docs>

## Access Redocs Documentation

> <http://localhost:8080/redoc>

## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

    app
    |
    | # Fast-API stuff
    ├── api                 - web related stuff.
    │   └── routes          - web routes.
    ├── core                - application configuration, startup events, logging.
    ├── models              - pydantic models for this application.
    ├── services            - logic that is not just crud related.
    ├── main-aws-lambda.py  - [Optional] FastAPI application for AWS Lambda creation and configuration.
    └── main.py             - FastAPI application creation and configuration.
    |
    | # ML stuff
    ├── data             - where you persist data locally
    │   ├── interim      - intermediate data that has been transformed.
    │   ├── processed    - the final, canonical data sets for modeling.
    │   └── raw          - the original, immutable data dump.
    │
    ├── notebooks        - Jupyter notebooks. Naming convention is a number (for ordering),
    |
    ├── ml               - modelling source code for use in this project.
    │   ├── __init__.py  - makes ml a Python module
    │   ├── pipeline.py  - scripts to orchestrate the whole pipeline
    │   │
    │   ├── data         - scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features     - scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   └── model        - scripts to train models and make predictions
    │       ├── predict_model.py
    │       └── train_model.py
    │
    └── tests            - pytest