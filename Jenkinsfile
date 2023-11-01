pipeline {

  environment {
    registry = "muthubharathi740/flask"
    registry_mysql = "muthubharathi740/mysql"
    dockerImage = ""
  }

  agent any
    stages {
  
    stage('Checkout Source') {
      steps {
        git 'https://github.com/muthubharathi740/Docker-Project.git'
      }
    }

    stage('Build image') {
      steps{
        script {
          dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }

    stage('Push flask Image') {
      steps{
        script {
          withdockerRegistry( [ credentialsId: "dockerhub2", url: "" ] ) {
            dockerImage.push()
          }
        }
      }
    }

    stage('current') {
      steps{
        dir("${env.WORKSPACE}/mysql"){
          sh "pwd"
          }
      }
   }
   stage('Build mysql image') {
     steps{
       withDockerRegistry([ credentialsId: "dockerhub2", url: "" ]) {
       sh 'docker build -t "muthubharathi740/mysql:$BUILD_NUMBER"  "$WORKSPACE"/mysql'

         
        sh 'docker push "muthubharathi740/mysql:$BUILD_NUMBER"'
        }
      } 
   }
    stage('Push mysql Image') {
      steps{
        script {
          withdockerRegistry ([ credentialsId: "dockerhub2", url: "" ] ) {
            dockerImage.push("registry_mysql")
          }
        }
      }
    }
      stage('Deploy App') {
      steps {
        script {
          kubernetesDeploy(configs: "frontend.yaml", kubeconfigId: "kube")
        }
      }
    }

  }

}
