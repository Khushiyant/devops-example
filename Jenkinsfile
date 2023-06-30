pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    
    triggers {
        pollSCM '* * * * *'
    }
    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        
        stage('Run') {
            steps {
                sh 'flask --app devops --port 3434 run'
            }
        }
    }
    
}
