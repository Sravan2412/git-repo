pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/python']], doGenerateSubmoduleConfigurations: false, extensions: [], submoduleCfg: [], userRemoteConfigs: [[credentialsId: 'MyGitHubId', url: 'https://github.com/Sravan2412/git-repo.git']]])
                echo "This is at Checkout stage"
            }
        }
        stage('Build') {
            steps {
                git branch: 'python', credentialsId: 'MyGitHubId', url: 'https://github.com/Sravan2412/git-repo.git'
                echo "This is at Build stage"
                bat label: '', script: 'python samplepython.py'
                echo "Build is now started"
            }
        }
        stage('Test') {
            steps {
                echo "This is at Testing stage"
                echo "Testing has been done"
            }
        }
    }
}
