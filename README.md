## CI/CD with Jenkins

## TASK 1: 1. Jenkins CI CD pipeline for flask application

This project is configured with a Jenkins CI/CD pipeline for the Flask application.

### Prerequisites

- Jenkins server (e.g., Ubuntu VM)
- Java 17+
- Python 3 and pip
- Git
- (Optional) MongoDB instance for the application
- Access to GitHub

### Pipeline Overview

The pipeline is defined in the `Jenkinsfile` at the root of the repository.

Stages:

1. **Checkout**
   - Jenkins checks out the latest code from the `main` branch of this repository.

2. **Build**
   - Creates a Python virtual environment inside the Jenkins workspace.
   - Installs all dependencies from `requirements.txt` using `pip`.

3. **Test**
   - Runs unit tests using `pytest`.
   - The tests are located in the `tests/` directory.
   - If any test fails, the pipeline stops and deployment does not happen.

4. **Deploy**
   - If tests pass, the Flask application is started as a "staging" server on the Jenkins machine.
   - Environment variables such as `MONGO_URI` and `SECRET_KEY` are set before starting the app.
   - The app is started with `nohup` so it continues running in the background.

### Triggers

- The Jenkins job is configured with a **GitHub webhook**.
- Whenever a commit is pushed to the `main` branch, GitHub sends a webhook to Jenkins, which triggers a new build.

### Notifications

- Jenkins is configured with SMTP (e.g., Gmail).
- The pipeline uses the `mail` step in the `post` section:
  - Sends an email when the build **succeeds**.
  - Sends an email when the build **fails**.
- Emails include the job name, build number, and a link to the Jenkins build logs.

### How to Run the Pipeline

1. Ensure Jenkins is running and configured with the correct Git repository and credentials.
2. Push any change to the `main` branch.
3. Jenkins will:
   - Checkout the code
   - Build and install dependencies
   - Run tests
   - Deploy the application (if tests pass)
4. Check the Jenkins console output and your email for the build status.



## Task 2 - GitHub Actions CI/CD Workflow

This repository includes a CI/CD pipeline implemented using **GitHub Actions**.

### Branches

- `main` – main development branch
- `staging` – used for staging deployments

### Workflow File

The workflow is defined in `.github/workflows/ci-cd.yml`.

### Triggers

- **Push to `staging` branch**
  - Runs the `build-and-test` job.
  - If tests pass, runs `deploy-staging` job, which simulates deployment to a staging environment and uploads a staging build as a workflow artifact.

- **Release published**
  - When a GitHub release is published, the workflow runs the same `build-and-test` job.
  - If tests pass, it runs `deploy-production`, which simulates deployment to a production environment and uploads a production build as an artifact.

### Jobs and Steps

1. **build-and-test**
   - Checks out the code.
   - Sets up Python 3.10.
   - Installs dependencies from `requirements.txt` using `pip`.
   - Installs `pytest`.
   - Runs the test suite with `pytest`.

2. **deploy-staging**
   - Runs only for pushes to the `staging` branch.
   - Prepares the application for staging by copying files into a `deploy-staging` directory.
   - Uploads the directory as a `flask-app-staging` artifact.

3. **deploy-production**
   - Runs only when a GitHub release is published.
   - Prepares the application for production by copying files into a `deploy-production` directory.
   - Uploads the directory as a `flask-app-production` artifact.

### Environment Secrets

The workflow uses **GitHub Secrets** to store sensitive configuration:

- `MONGO_URI` – MongoDB connection string.
- `SECRET_KEY` – Flask secret key.

These are configured in:

`Repository Settings → Secrets and variables → Actions`.

Inside the workflow, the secrets are available as environment variables and are **not** stored in the code:

```yaml
env:
  MONGO_URI: ${{ secrets.MONGO_URI }}
  SECRET_KEY: ${{ secrets.SECRET_KEY }}

## Branch Strategy

Branch			Purpose
staging			CI/CD staging deployment tests
main			Production deployment + release workflow


### Merge staging into main (critical step)
git fetch --all
git checkout staging
git push origin staging


git checkout main
git pull origin main
git merge staging


git push origin main


## Production Deployment Trigger

Go to GitHub → Releases → Draft a new release

Tag example: v1.0.0

Title: My First Production Release

Click Publish release

This runs the deploy-production job automatically.


## Rerunning jobs

In GitHub Actions UI, open any workflow → click Re-run all jobs when needed.

📸 Workflow Example Result (Successful Run)

Build & Test ✔️

Deploy Staging ✔️

Deploy Production ✔️

Two artifacts visible in list: flask-staging & flask-production
