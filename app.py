pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/Kiran-coplot/python-jenkins.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || echo "No dependencies to install"'
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 app.py'
            }
        }
    }
}

