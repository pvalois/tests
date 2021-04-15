pipeline {
    agent any 

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
