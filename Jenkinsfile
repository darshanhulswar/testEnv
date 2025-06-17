pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY = credentials('AWS_ACCESS_KEY ') // if using Jenkins credentials
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY ') // if using Jenkins credentials
        AWS_REGION = credentials('AWS_REGION ') // if using Jenkins credentials
        BUCKET_NAME = credentials('BUCKET_NAME ') // if using Jenkins credentials
    }

    stages {
        stage('git checkout') {
            steps {
                git url: 'https://github.com/darshanhulswar/testEnv.git', branch: 'main'
            }
        }
        stage('Print Env') {
            steps {
                sh '''
                echo "Access Key is: ${env.AWS_ACCESS_KEY}"
                echo "Access Key is: ${env.AWS_SECRET_ACCESS_KEY}"
                echo "Access Key is: ${env.AWS_REGION}"
                echo "Access Key is: ${env.BUCKET_NAME}"
                '''
            }
        }

        stage("build and tag") {
            steps {
                sh '''
                    docker build -t envtest:1 .
                '''
            }
        }

         stage("run") {
            steps {
                sh '''
                    docker run -it -d --name envtest -p 9002:8501 envtest:1
                '''
            }
        }
    }
}
