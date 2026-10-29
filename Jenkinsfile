
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\saisr\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
        DOCKER_IMAGE = 'saisri12/vehicle-rental'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out from GitHub.'
            }
        }

        stage('Check Python') {
            steps {
                bat '"%PYTHON%" --version'
                bat '"%PYTHON%" -m pip --version'
            }
        }

        stage('Check Docker') {
            steps {
                bat 'docker --version'
                bat 'docker info'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"%PYTHON%" -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat '"%PYTHON%" -m unittest -v test_app.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE%:%BUILD_NUMBER% .'
                bat 'docker tag %DOCKER_IMAGE%:%BUILD_NUMBER% %DOCKER_IMAGE%:latest'
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USERNAME',
                    passwordVariable: 'DOCKER_PASSWORD'
                )]) {
                    bat 'powershell -NoProfile -Command "$env:DOCKER_PASSWORD | docker login --username $env:DOCKER_USERNAME --password-stdin"'

                    bat 'docker push %DOCKER_IMAGE%:%BUILD_NUMBER%'
                    bat 'docker push %DOCKER_IMAGE%:latest'

                    bat 'docker logout'
                }
            }
        }
    }

    post {
        success {
            echo 'Vehicle Rental tests passed and Docker images were published!'
        }
        failure {
            echo 'Pipeline failed. Check the Console Output.'
        }
    }
}
