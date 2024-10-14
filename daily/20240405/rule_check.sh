#!/bin/bash

# Parameters
RULE_NAME="my-scheduled-rule"
REGION="us-east-1"
TARGET_ARN="arn:aws:lambda:us-east-1:123456789012:function:MyLambdaFunction"

# Create the rule
aws events put-rule \
  --name "$RULE_NAME" \
  --schedule-expression "rate(1 hour)" \
  --region "$REGION"

# Function to check if the rule exists
wait_for_rule_creation() {
  local rule_name="$1"
  local region="$2"

  while true; do
    # Try to describe the rule to see if it exists
    rule_status=$(aws events describe-rule --name "$rule_name" --region "$region" 2>&1)

    if [[ $? -eq 0 ]]; then
      echo "Rule $rule_name exists. Proceeding to put targets."
      break
    else
      echo "Rule $rule_name is not ready yet. Waiting..."
      sleep 5  # Wait for 5 seconds before checking again
    fi
  done
}

# Wait for the rule to be fully created
wait_for_rule_creation "$RULE_NAME" "$REGION"

# Now add the target for the rule
aws events put-targets \
  --rule "$RULE_NAME" \
  --targets "Id"="1","Arn"="$TARGET_ARN" \
  --region "$REGION"

echo "Target added to the rule successfully."
