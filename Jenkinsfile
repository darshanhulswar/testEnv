pipeline {
    agent any

    environment {
        AWS_ACCESS_KEY = credentials('AWS_ACCESS_KEY') // fixed trailing space
        AWS_SECRET_ACCESS_KEY = credentials('AWS_SECRET_ACCESS_KEY') // fixed
        AWS_REGION = credentials('AWS_REGION') // fixed
        BUCKET_NAME = credentials('BUCKET_NAME') // fixed
    }

    stages {
        stage('Git Checkout') {
            steps {
                git url: 'https://github.com/darshanhulswar/testEnv.git', branch: 'main'
            }
        }

        stage('Print Env') {
            steps {
                sh '''
                echo "AWS_ACCESS_KEY: $AWS_ACCESS_KEY"
                echo "AWS_SECRET_ACCESS_KEY: $AWS_SECRET_ACCESS_KEY"
                echo "AWS_REGION: $AWS_REGION"
                echo "BUCKET_NAME: $BUCKET_NAME"
                '''
            }
        }

        stage('Build and Tag') {
            steps {
                sh '''
                    docker build -t envtest:1 .
                '''
            }
        }

stage('Run Container') {
    steps {
        sh '''
            docker run -it -d --name envtest \
                -e AWS_ACCESS_KEY=$AWS_ACCESS_KEY \
                -e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
                -e AWS_REGION=$AWS_REGION \
                -e BUCKET_NAME=$BUCKET_NAME \
                -p 9002:8501 \
                envtest:1
        '''
    }
}
    }
}
