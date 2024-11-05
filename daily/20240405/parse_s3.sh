#!/bin/bash

s3_url="s3://your-bucket-name/path/to/your/file.txt"

# Extract bucket name and key
bucket=$(echo "$s3_url" | sed -E 's#s3://([^/]+).*#\1#')
key=$(echo "$s3_url" | sed -E 's#s3://[^/]+/(.*)#\1#')

echo "Bucket: $bucket"
echo "Key: $key"
