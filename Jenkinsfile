pipeline {

	//agent { label 'lbl_agent_node' }

	agent any
		stages {
			stage('Checkout') {
				steps {

					checkout([$class: 'GitSCM',
							branches: [[name: '*/main']],
							userRemoteConfigs: [[url: 'https://github.com/satish-gadigi/hwpygitjendocodb']]
					])
				}
			}
			// git 'https://github.com/satish-gadigi/Hello-World.git'


			stage('Build') {
				steps {
					sh 'docker build -t satishri/hdpygitjendocodb:${BUILD_NUMBER} .'
				}
			}

			stage('Push') {
				steps {
					withCredentials([usernamePassword(
								credentialsId: 'docker-cred_id',
								usernameVariable: 'DOCKER_USER',
								passwordVariable: 'DOCKER_PASS'
								)]) {
						sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
							sh 'docker tag satishri/hdpygitjendocodb:${BUILD_NUMBER} satishri/hdpygitjendocodb:latest'
							sh 'docker push satishri/hdpygitjendocodb:latest'
					}
				}
			}
			stage('Cleanup Old Containers') {
				steps {
					sh '''
# Stop and remove all containers from this compose project
						docker-compose -f docker-compose.yml down --remove-orphans || true

# Extra safety: remove any leftover containers by name
						docker rm -f hdpygitjendocodb_ap_1 || true
						docker rm -f hdpygitjendocodb_db_1 || true
						'''
				}
			}
			//stage('Deploy')	{
			//	steps {
			//sh 'docker run -d --name helloworldappusingjenkins -p 8081:8080 satishri/hello-world:latest'
			//}
			//}
			stage('Deploy with Docker-Compose') {
				steps {
					sh '''

		# Start new stack
						docker-compose up -d --build
						'''
				}
			}		
		}
}
