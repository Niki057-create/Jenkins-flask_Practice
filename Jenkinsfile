pipeline {
    agent any

    environment {
        VENV_DIR  = "${WORKSPACE}/venv"
        PYTHON    = "${VENV_DIR}/bin/python"
        PIP       = "${VENV_DIR}/bin/pip"

        // You can adjust these for your MongoDB & secret
        MONGO_URI  = "mongodb://localhost:27017/studentdb"
        SECRET_KEY = "supersecretkey"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Creating virtual environment and installing dependencies"
                sh '''
                    set -e
                    # create venv
                    python3 -m venv "$VENV_DIR"

                    # install dependencies into that venv
                    "$PIP" install --upgrade pip
                    "$PIP" install -r requirements.txt

                    # make sure pytest is installed in venv
                    "$PIP" install pytest
                '''
            }
        }

        stage('Test') {
            steps {
                echo "Running unit tests with pytest"
                sh '''
                    set -e
                    # activate the venv and run pytest
                    . "$VENV_DIR/bin/activate"
                    pytest
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
                    export MONGO_URI="$MONGO_URI"
                    export SECRET_KEY="$SECRET_KEY"

                    # Start the app with nohup so it keeps running
                    nohup "$PYTHON" app.py > flask_app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Build and deployment succeeded!'
            // email disabled for now (SMTP not configured)
        }
        failure {
            echo 'Build or deployment failed!'
            // email disabled for now (SMTP not configured)
        }
    }
}

