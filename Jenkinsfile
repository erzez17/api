node ("linux") {
	stage("Build") {
		deleteDir()
		checkout scm
		sh 'docker build -t erzez/api_test:latest .'
	}
	stage("Test") {
		sh 'chmod +x test.sh'
		def var ' sh (script: "./test.sh", returnStdout: true)'
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
		sh 'docker build -t erzez/api_prod:latest'
		sh 'kubectl set image deployment/flask-dep flask=erzez/api_prod:latest'
	}
}
