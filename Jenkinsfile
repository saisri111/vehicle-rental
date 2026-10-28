
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code retrieved from GitHub.'
            }
        }

        stage('Check Python') {
            steps {
                bat 'python --version'
                bat 'python -m pip --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m unittest -v test_app.py'
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
