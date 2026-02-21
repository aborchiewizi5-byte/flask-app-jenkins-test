pipeline {
    agent any

    environment {
        IMAGE_NAME = "jenkins-demo-app"
        IMAGE_TAG  = "latest"
    }

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate.bat
                    python -m pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
    steps {
        echo 'Running tests with coverage...'
        bat '''
            call venv\\Scripts\\activate.bat
            pytest tests/ --cov=app --cov-report=xml --cov-report=term-missing -v --rootdir=.
        '''
    }
}

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t %IMAGE_NAME%:%IMAGE_TAG% ."
            }
        }

        stage('Deploy (Local)') {
            steps {
                echo 'Deploying container locally...'
                bat '''
                    docker stop jenkins-demo 2>nul || exit /b 0
                    docker rm   jenkins-demo 2>nul || exit /b 0
                    docker run -d --name jenkins-demo -p 5000:5000 %IMAGE_NAME%:%IMAGE_TAG%
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline succeeded! App is running on port 5000."
        }
        failure {
            echo "Pipeline failed. Check the logs above."
        }
        always {
            bat 'if exist venv rmdir /s /q venv 2>nul & exit /b 0'
        }
    }
}
