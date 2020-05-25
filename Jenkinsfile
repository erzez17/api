node ("linux") {
	stage("Build") {
		deleteDir()
		checkout scm
		sh 'docker build -t erzez/api_test:latest .'
	}
	stage("Test") {
		sh 'docker run --name test -p 433:80 -dit erzez/api_test:latest'
		sh 'chmod +x test.sh'
		def var = sh (script: "./test.sh", returnStdout: true)
		sh 'docker rm -f test'
		if ("${var}") {
			echo "Testing completed successfully"
		}
		else {
			"Failed The Testing"
			currentBuild.result = 'FAILURE'
		}
	}
	stage("Deploy") {
		sh 'docker build -t erzez/api_prod:latest .'
		sh 'hostname'
		sh 'kubectl set image deployment/flask-dep flask=erzez/api_prod:latest'
	}
}
