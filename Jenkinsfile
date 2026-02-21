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
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests with coverage...'
                sh '''
                    . venv/bin/activate
                    pytest tests/ --cov=app --cov-report=xml --cov-report=term-missing -v
                '''
            }
            post {
                always {
                    // Publish coverage report if the plugin is installed
                    echo 'Tests complete.'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Deploy (Local)') {
            steps {
                echo 'Deploying container locally...'
                sh '''
                    docker stop jenkins-demo || true
                    docker rm   jenkins-demo || true
                    docker run -d --name jenkins-demo -p 5000:5000 ${IMAGE_NAME}:${IMAGE_TAG}
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
            sh 'rm -rf venv'
        }
    }
}
