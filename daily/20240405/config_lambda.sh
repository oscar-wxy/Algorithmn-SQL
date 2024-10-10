#!/bin/bash

# Variables
LAMBDA_NAME="func"
S3_BUCKET="your-s3-bucket"
S3_KEY="path/to/your/python_file.zip"
IAM_ROLE="arn:aws:iam::123456789012:role/execution-role"
SCHEDULE_PARAM="$1" # Schedule interval in cron or rate syntax, e.g., "rate(5 minutes)"
REGION="us-east-1"

# Check if Lambda function exists
lambda_exists=$(aws lambda get-function --function-name "$LAMBDA_NAME" --region "$REGION" 2>&1)

if [[ "$lambda_exists" == *"ResourceNotFoundException"* ]]; then
    echo "Lambda function $LAMBDA_NAME does not exist. Creating..."
    
    # Create Lambda function
    aws lambda create-function \
        --function-name "$LAMBDA_NAME" \
        --runtime python3.9 \
        --role "$IAM_ROLE" \
        --handler lambda_function.lambda_handler \
        --code S3Bucket="$S3_BUCKET",S3Key="$S3_KEY" \
        --region "$REGION"
    echo "Lambda function $LAMBDA_NAME created."
else
    echo "Lambda function $LAMBDA_NAME exists. Updating..."
    
    # Update Lambda function code and IAM role
    aws lambda update-function-code \
        --function-name "$LAMBDA_NAME" \
        --s3-bucket "$S3_BUCKET" \
        --s3-key "$S3_KEY" \
        --region "$REGION"

    aws lambda update-function-configuration \
        --function-name "$LAMBDA_NAME" \
        --role "$IAM_ROLE" \
        --region "$REGION"
    echo "Lambda function $LAMBDA_NAME updated."
fi

# Check for existing CloudWatch schedule rule
rule_exists=$(aws events list-rule-names-by-target --target-arn arn:aws:lambda:$REGION:123456789012:function:$LAMBDA_NAME --region "$REGION")

if [[ -z "$rule_exists" ]]; then
    echo "No schedule exists for Lambda. Creating schedule..."
    
    # Create CloudWatch Events rule to trigger Lambda
    aws events put-rule \
        --name "${LAMBDA_NAME}_schedule" \
        --schedule-expression "$SCHEDULE_PARAM" \
        --region "$REGION"

    # Add Lambda as the target for the schedule
    aws events put-targets \
        --rule "${LAMBDA_NAME}_schedule" \
        --targets "Id"="1","Arn"="arn:aws:lambda:$REGION:123456789012:function:$LAMBDA_NAME" \
        --region "$REGION"

    # Grant CloudWatch permission to invoke the Lambda function
    aws lambda add-permission \
        --function-name "$LAMBDA_NAME" \
        --statement-id "cloudwatch-lambda-permission" \
        --action "lambda:InvokeFunction" \
        --principal events.amazonaws.com \
        --source-arn "arn:aws:events:$REGION:123456789012:rule/${LAMBDA_NAME}_schedule" \
        --region "$REGION"
    echo "Scheduled rule created for Lambda."
else
    echo "Schedule exists. Updating trigger..."
    
    # Update CloudWatch Events rule
    aws events put-rule \
        --name "${LAMBDA_NAME}_schedule" \
        --schedule-expression "$SCHEDULE_PARAM" \
        --region "$REGION"
    echo "Schedule updated."
fi
