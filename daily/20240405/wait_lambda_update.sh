#!/bin/bash

# Function to wait until the Lambda function is ready for the next update
wait_for_lambda_ready() {
  local function_name="$1"
  local region="$2"

  while true; do
    # Get the current state of the Lambda function
    local status=$(aws lambda get-function --function-name "$function_name" --region "$region" 2>&1)

    if [[ $? -ne 0 ]]; then
      echo "Error getting Lambda function status."
      exit 1
    fi

    # Check if the function is still updating (there will be an ongoing "LastUpdateStatus" field)
    local last_update_status=$(aws lambda get-function-configuration --function-name "$function_name" --region "$region" | jq -r '.LastUpdateStatus')

    if [[ "$last_update_status" == "Successful" || "$last_update_status" == "Failed" ]]; then
      echo "Lambda function is ready for the next update."
      break
    else
      echo "Lambda function is still updating. Waiting..."
      sleep 5  # Wait for 5 seconds before checking again
    fi
  done
}

# Parameters
LAMBDA_NAME="MyLambdaFunction"
REGION="us-east-1"
S3_BUCKET="my-bucket"
S3_KEY="my-code.zip"

# Wait until Lambda is ready
wait_for_lambda_ready "$LAMBDA_NAME" "$REGION"

# Update Lambda function code
aws lambda update-function-code \
  --function-name "$LAMBDA_NAME" \
  --s3-bucket "$S3_BUCKET" \
  --s3-key "$S3_KEY" \
  --region "$REGION"

# Wait for Lambda to be ready before updating configuration
wait_for_lambda_ready "$LAMBDA_NAME" "$REGION"

# Update Lambda function configuration
aws lambda update-function-configuration \
  --function-name "$LAMBDA_NAME" \
  --region "$REGION" \
  --memory-size 512 \
  --timeout 30
