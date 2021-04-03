pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
              script {
                sh """
                pip3 install -r requirements.txt
                """
              }
            }
        }
        stage('Test') {
            steps {
              script {
                sh """
                python3 test.py
                """
              }
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
