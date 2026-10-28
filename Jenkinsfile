
pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Users\\saisr\\AppData\\Local\\Programs\\Python\\Python313\\python.exe'
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
    }

    post {
        success {
            echo 'Vehicle Rental application tests passed!'
        }
        failure {
            echo 'Pipeline failed. Check the Console Output.'
        }
    }
}
