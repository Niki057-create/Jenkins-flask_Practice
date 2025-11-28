pipeline {
    agent any

    environment {
        // Name of the virtual environment folder
        VENV_DIR = "venv"
        // Python command
        PYTHON = "python3"
    }

    stages {
        stage('Checkout') {
            steps {
                // Jenkins automatically checks out from SCM, but this makes it explicit
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo "Creating virtual environment and installing dependencies..."
                sh """
                    if [ ! -d "${VENV_DIR}" ]; then
                        ${PYTHON} -m venv ${VENV_DIR}
                    fi
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                """
            }
        }

        stage('Test') {
            steps {
                echo "Running pytest..."
                sh """
                    . ${VENV_DIR}/bin/activate
                    pytest
                """
            }
        }

        stage('Deploy') {
            when {
                branch 'main'  // only deploy when main branch builds
            }
            steps {
                echo "Deploying application to staging environment..."

                // NOTE: Simple example deployment on the same VM as Jenkins
                // Adjust the port and command according to your app.py
                sh """
                    . ${VENV_DIR}/bin/activate

                    # Stop any existing app running on port 8000 (simple way)
                    APP_PID=\$(lsof -ti:8000 || true)
                    if [ ! -z "\$APP_PID" ]; then
                        echo "Stopping existing app process \$APP_PID"
                        kill -9 \$APP_PID || true
                    fi

                    # Start the Flask app in background
                    nohup ${PYTHON} app.py > app.log 2>&1 &
                    echo "App started on http://localhost:8000"
                """
            }
        }
    }

    post {
        success {
            echo "Build succeeded!"
            // Email will work after you configure SMTP
            mail to: 'nikithabalaji143@gmail.com',
                 subject: "SUCCESS: Jenkins build \${env.JOB_NAME} #\${env.BUILD_NUMBER}",
                 body: "Good news! The build passed. Check Jenkins for details: \${env.BUILD_URL}"
        }
        failure {
            echo "Build failed!"
            mail to: 'nikithabalaji143@gmail.com',
                 subject: "FAILURE: Jenkins build \${env.JOB_NAME} #\${env.BUILD_NUMBER}",
                 body: "The build failed. Please check console output: \${env.BUILD_URL}"
        }
    }
}

