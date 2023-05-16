pipeline {
    agent any
    environment {
        project='vksh'
    }

    stages {
        stage('GitPipLine') {
            steps {
                git 'https://github.com/vishaljudoka/python_learning.git'
                bat 'dir'
                withCredentials([string(credentialsId: 'eaf673a3-3c41-4480-a6fd-17fa2b661584', variable: 'secretcredFID')]) {
                // some block 
                echo secretcredFID
                }
            } 
        }
        
        stage('CheckName') {
            steps {
                input 'Enter Name'
                echo project
            } 
        }
        
         stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**', followSymlinks: false
            }
        }
    }
}
