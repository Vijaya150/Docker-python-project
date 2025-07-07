pipeline {
    agent { label 'testlabel' }

    environment {
        IMAGE_NAME = 'vijayadarshini/flaskapp'
    }

    stages {

        stage('Git checkout') {
            steps {
                git url: "https://github.com/Vijaya150/Docker-python-project.git"
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-id', passwordVariable: 'docker_password', usernameVariable: 'docker_username')]) {
                    sh '''
                    echo $docker_password | docker login -u $docker_username --password-stdin
                    docker push $IMAGE_NAME
                    '''
                }
            }
        }

        stage('Run Container') {
            steps {
                sh "docker run -d -p 5000:8080 --name flaskapp $IMAGE_NAME"
            }
        }
    }
}

