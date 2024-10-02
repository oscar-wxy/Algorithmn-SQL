#!/bin/bash

# Set your tag key and substring value
TAG_KEY="Environment"
TAG_SUBSTRING="prod"
S3_PREFIX="s3://your-s3-bucket/prefix"

# List all EMR clusters
clusters=$(aws emr list-clusters --query 'Clusters[*].Id' --output text)

# Check if any clusters are available
if [ -z "$clusters" ]; then
    echo "No EMR clusters found."
    exit 0
fi

# Loop through each cluster to check for the specific tag substring
for cluster_id in $clusters; do
    # Get the tags for the current cluster
    tags=$(aws emr describe-cluster --cluster-id $cluster_id --query 'Cluster.Tags' --output json)

    # Check if the tag contains the substring
    if echo "$tags" | jq -e --arg key "$TAG_KEY" --arg substring "$TAG_SUBSTRING" \
      '.[] | select(.Key == $key and (.Value | contains($substring)))' > /dev/null; then
        echo "Cluster ID: $cluster_id has tag with $TAG_KEY containing substring '$TAG_SUBSTRING'"
        
        # List files in the S3 location for this cluster
        s3_path="$S3_PREFIX/$cluster_id/"
        echo "Listing files in $s3_path"
        
        # Get the latest updated file
        latest_file=$(aws s3 ls $s3_path --recursive | sort -k1,2 | tail -n 1)
        
        if [ -n "$latest_file" ]; then
            # Extract the date and file path
            latest_date=$(echo "$latest_file" | awk '{print $1 " " $2}')
            file_key=$(echo "$latest_file" | awk '{print $4}')

            # Convert the latest file date to a timestamp
            latest_file_timestamp=$(date -d "$latest_date" +%s)
            current_time=$(date +%s)
            two_hours_ago=$((current_time - 7200)) # 2 hours in seconds

            echo "Latest file: $file_key, Last modified: $latest_date"

            # Check if the latest file is older than 2 hours
            if [ $latest_file_timestamp -lt $two_hours_ago ]; then
                echo "The latest file is older than 2 hours. Deleting cluster $cluster_id..."
                
                # Delete the EMR cluster
                aws emr terminate-clusters --cluster-ids $cluster_id
                
                if [ $? -eq 0 ]; then
                    echo "Cluster $cluster_id successfully deleted."
                else
                    echo "Failed to delete cluster $cluster_id."
                fi
            else
                echo "The latest file is less than 2 hours old. Skipping deletion for cluster $cluster_id."
            fi
        else
            echo "No files found in $s3_path"
        fi
    fi
done
