pipeline {
    agent { docker { image 'python:3.5.1' } }

    stages {
        stage('Build') {
            steps {
              script {
                sh """
                docker build . -t flask1
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
