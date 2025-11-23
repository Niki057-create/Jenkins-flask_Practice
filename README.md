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

