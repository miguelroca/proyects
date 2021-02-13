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

        stage('') {
          steps {
            powershell 'docker images'
          }
        }

      }
    }

  }
}