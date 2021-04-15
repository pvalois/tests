pipeline {
    agent { docker { image 'python:3.5.1' } }

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
        stage('Building image') {
            steps{
              script {
                docker.build registry + ":$BUILD_NUMBER"
              }
            }
        } 
    }
}
