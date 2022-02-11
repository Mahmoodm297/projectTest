pipeline {
    agent any
	
	environment {
		POSTGRES_HOST = 'localhost'
		POSTGRES_USER = 'myuser'
	}
	
	tools {
		maven	'Maven'    // 'Mave' the plugin name installed in the jenkins 
		
	
	}
  
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
            }
        }
    }
}
