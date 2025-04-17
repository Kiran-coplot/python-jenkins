pipeline {
    agent any

    environment {
        PYTHON = 'python3'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/Kiran-coplot/python-jenkins'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '${PYTHON} -m pip install --upgrade pip'
                sh '${PYTHON} -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '${PYTHON} -m pytest'
            }
        }

        stage('Run App') {
            steps {
                sh '${PYTHON} main.py'
            }
        }
    }
}

