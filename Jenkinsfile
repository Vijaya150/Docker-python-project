pipeline {
agent any
 
  environment {
        IMAGE_NAME = 'vijayadarshini/flaskapp'
    }
 
 stages{

  stage('Git checkout'){
  steps{
  git url:"https://github.com/Vijaya150/Docker-python-project.git"
}
}

 stage('Build Docker Image'){
 steps{
  script {
 sh "docker build -t $IMAGE_NAME ."
 }
 }
}
 }
 }


