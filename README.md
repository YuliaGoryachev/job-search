# Job Search Enhanced
This is a stripped down version of a basic "cookie-cutter" Fastapi project, 
taken form here: https://pypi.org/project/FastAPI-Cookiecutter/.
The purpose of this prototype is to simplify my a search with LinkedIn jobs.
The first step is to download the job descriptions from LinkedIn.
Since LinkedIn doesn't allow scraping and doesn't even have a free API, I had to use a Chrome extension.
The steps are:
1. Install the `jobs scraper extension` https://chromewebstore.google.com/detail/jobs-scraper-for-linkedin/jhmlphenakpfjkieogpinommlgjdjnhb
2. Activate the extension - 1st it will ask you to register
3. Do a search in LinkedIn
4. If the extension is activated, a green button “Download Jobs” is visible 
5. Click “Download jobs” 
6. A window will appear. When jobs are ready, click “Export jobs” - it will download a csv file

Note that it will download only 20 first jobs. If you need more, close the first 20 jobs and go back to the previous step. 
Repeat until got the needed number of jobs.

After downloading the jobs, you add extra features, like skills and salary, see the notebook `notebooks/01-Data-Preparation.ipynb`

Most of the examples how to use the different functions to search for interesting roles are in the notebook `notebooks/Linkedin_for_me.ipynb`
There are however two endpoints that can be used.
One endpoint is to get a cover letter for a job specification and a CV.
The other can be used to ask questions about the available jobs and get jobs recommendations.

## Development Requirements

- Python3.10
- Pip
- Poetry (Python Package Manager)

## Installation
if no venv is available, create one with the following commands:
```sh
python -m venv venv
source venv/bin/activate
make install
```
if available activate the venv
## Running Localhost
```sh
cd app
uvicorn main:app --reload
```
- You can call the endpoints from swagger

## Running Tests

`make test`

## Access Swagger Documentation

> <http://localhost:8000/docs>


## Project structure

Files related to application are in the `app` or `tests` directories.
Application parts are:

    app
    |
    | # Fast-API stuff
    ├── api                 - web related stuff.
    │   └── routes          - web routes.
    ├── core                - application configuration, startup events, logging.
    ├── utils               - utilities for this application.
    └── main.py             - FastAPI application creation and configuration.
    |
    | # ML stuff
    ├── data             - where you persist data locally
    ├── notebooks        - Jupyter notebooks. Naming convention is a number (for ordering),
    └── tests            - pytest