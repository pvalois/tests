pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                pip3 install -r requirements.txt
            }
        }
        stage('Test') {
            steps {
                python3 test.py
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
