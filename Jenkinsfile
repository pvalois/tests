pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
              script {
                sh """
                docker build . -t 192.168.1.63:5000/flask1
                docker image push http://192.168.1.63:5000/flask1:latest
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
