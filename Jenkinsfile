pipeline {
	agent any
	    stages {

	        stage('Cloning Source Repository') {
	        /* Cloning the repository to our workspace */
		        steps {
		        	checkout scm
		        }
	   		}
/*____________________________________________________________________________________________________________*/
		/* For first run there is no need to remove old images and container */
		    // stage('Build first image') {
		    //      steps {
		    //      	sh 'sudo docker build -t sslcertification-webapp:1.0.0 .'
		    //      }
		    // }
// /*_____________________________________________________________________________________________________________*/
			/* For later runs*/
		   stage('Stop and Remove old container') {
		        steps {

                sh '''
                    sudo docker container stop sslcertification-webapp-container
                    sudo docker container rm sslcertification-webapp-container
                '''
		        }
		   }

		   stage('Remove old image and build new one') {
		        steps {
					sh 'sudo docker image rm sslcertification-webapp:1.0.0'
					sh 'sudo docker build -t sslcertification-webapp:1.0.0 .'
		        }
		   }
// /*_____________________________________________________________________________________________________________*/

// -v /home/ubuntu/importantfiles:/app/app/static

		   stage('Run Image') {
		        steps {
		        	// sh 'sudo docker run -d -p 5000:4000 --name asmi-clothing-api-app asmi-clothing-webapp:1.0.0'
					// sh 'sudo docker run -d -p 5000:4000 -p 5432:5432 --name asmi-clothing-api-app asmi-clothing-webapp:1.0.0 --add-host=database:18.221.2.60'
					// sh 'sudo docker run -d -p 5000:4000 --name asmi-clothing-api-app asmi-clothing-webapp:1.0.0 --add-host=database:18.221.2.60'
					sh 'sudo docker run -d --add-host=database:172.17.0.1 -v /home/ubuntu/importantfiles:/app/app/static -p 80:4000 --name sslcertification-webapp-container sslcertification-webapp:1.0.0'
					
		        }
		   }

		   stage('Testing'){
		        steps {
		            echo 'Testing..'
		        }
		   }
    	}
}