pipeline {
    agent any
    environment {
        AWS_REGION = 'us-east-1'  // Specify your AWS region
        LAMBDA_FUNCTION_NAME = 'my-lambda-function'  // Change to your Lambda function name
        LAMBDA_FILE = 'lambda_function.py'  // Change to 'lambda_function.zip' if packaging dependencies
        EXECUTION_ROLE_ARN = 'arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_ROLE_NAME'  // Execution role ARN
    }
    stages {
        stage('Checkout') {
            steps {
                // Checkout the latest code from the Git repository
                git url: 'https://github.com/your-repo.git', branch: 'main'
            }
        }
        stage('Check and Deploy Lambda') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: 'aws-creds']]) {
                    script {
                        // Check if the Lambda function exists
                        def lambdaExists = sh(
                            script: """
                                aws lambda get-function --function-name ${LAMBDA_FUNCTION_NAME} --region ${AWS_REGION} > /dev/null 2>&1
                                echo $?
                            """, returnStdout: true
                        ).trim()

                        // If the Lambda function exists, update the function code and role
                        if (lambdaExists == '0') {
                            echo "Lambda function exists. Updating function code and role..."
                            sh """
                            # Update the Lambda function code
                            aws lambda update-function-code \
                                --function-name ${LAMBDA_FUNCTION_NAME} \
                                --zip-file fileb://./${LAMBDA_FILE} \
                                --region ${AWS_REGION}
                            
                            # Update the function configuration to set the execution role
                            aws lambda update-function-configuration \
                                --function-name ${LAMBDA_FUNCTION_NAME} \
                                --role ${EXECUTION_ROLE_ARN} \
                                --region ${AWS_REGION}
                            """
                        } else {
                            echo "Lambda function does not exist. Creating new Lambda function..."
                            sh """
                            # Create the Lambda function with the provided execution role
                            aws lambda create-function \
                                --function-name ${LAMBDA_FUNCTION_NAME} \
                                --runtime python3.8 \  # Adjust runtime as needed
                                --role ${EXECUTION_ROLE_ARN} \
                                --handler lambda_function.lambda_handler \
                                --zip-file fileb://./${LAMBDA_FILE} \
                                --region ${AWS_REGION}
                            """
                        }
                    }
                }
            }
        }
    }
    post {
        success {
            echo 'Lambda function deployment successful!'
        }
        failure {
            echo 'Lambda function deployment failed.'
        }
    }
}
