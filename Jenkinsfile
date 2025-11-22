pipeline {
    agent any

    environment {
        VENV_DIR = "${WORKSPACE}/venv"
        PYTHON   = "${VENV_DIR}/bin/python"
        PIP      = "${VENV_DIR}/bin/pip"

        // You can adjust these for your MongoDB & secret
        MONGO_URI = "mongodb+srv://nikithabalaji143:Angel0507@nikitha.0qzb5fk.mongodb.net/"
        SECRET_KEY = "supersecretkey"
    }

    stages {
        stage('Checkout') {
            steps {
                // Jenkins will automatically use the repo you configure in the job
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Creating virtual environment and installing dependencies"
                sh '''
                    set -e
                    python3 -m venv "${VENV_DIR}"
                    "${PIP}" install --upgrade pip
                    "${PIP}" install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Running unit tests with pytest"
                sh '''
                    set -e
                    "${VENV_DIR}/bin/pytest"
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo "Deploying Flask app to staging environment"

                sh '''
                    set -e

                    # Stop any existing app.py process (ignore errors)
                    pkill -f "app.py" || true

                    echo "Starting Flask app in background on port 8000"

                    # Export env vars for the app
                    export MONGO_URI="${MONGO_URI}"
                    export SECRET_KEY="${SECRET_KEY}"

                    # Start the app with nohup so it keeps running
                    nohup "${PYTHON}" app.py > flask_app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Build and deployment succeeded!'
            mail to: 'your-email@example.com',
                 subject: "Jenkins Success: ${JOB_NAME} #${BUILD_NUMBER}",
                 body: """Good news!

The Jenkins job "${JOB_NAME}" build #${BUILD_NUMBER} completed SUCCESSFULLY.

Repository: ${GIT_URL}
Branch:    ${GIT_BRANCH}

– Jenkins
"""
        }
        failure {
            echo 'Build or deployment failed!'
            mail to: 'your-email@example.com',
                 subject: "Jenkins FAILED: ${JOB_NAME} #${BUILD_NUMBER}",
                 body: """Oops!

The Jenkins job "${JOB_NAME}" build #${BUILD_NUMBER} has FAILED.

Please check the Jenkins console log for details:
${BUILD_URL}console

– Jenkins
"""
        }
    }
}
