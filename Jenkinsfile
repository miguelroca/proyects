pipeline {
  agent any
  stages {
    stage('Inicio_Environment') {
      steps {
        echo 'Iniciando proyecto'
        powershell 'SET'
      }
    }

    stage('Docker_Environment') {
      parallel {
        stage('Docker_Environment') {
          steps {
            powershell 'docker -v'
          }
        }

        stage('Docker_Images') {
          steps {
            powershell 'docker images'
          }
        }

      }
    }

    stage('Build') {
      steps {
        powershell 'docker build -t miguelroca/app3layer:2.0 .'
      }
    }

  }
}