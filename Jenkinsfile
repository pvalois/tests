pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
              script {
                sh """
                docker build . -t 192.168.1.63:5000/flask1
                docker image push 192.168.1.63:5000/flask1:latest
                """
              }
            }
        }
        stage('Deploy') {
            steps {
              script {
                sh """
                kubectl apply -f deploy/deploy.yaml 
                """
              }
            }
        }
    }
}
