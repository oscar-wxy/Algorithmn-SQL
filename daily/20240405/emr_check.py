import boto3
from datetime import datetime, timezone, timedelta

def get_active_emrs(emr_client):
    """List all active EMRs in us-east-1 and filter by 'daily cluster'."""
    clusters = emr_client.list_clusters(ClusterStates=['WAITING', 'RUNNING'])
    emr_ids = [cluster['Id'] for cluster in clusters['Clusters'] if 'daily cluster' in cluster['Name']]
    return emr_ids

def get_latest_zepplin_file(s3_client, cluster_id):
    """Get the latest 'zepplin' suffixed file in the S3 path for the given cluster ID."""
    bucket_name = 'abc'
    prefix = f'{cluster_id}/'
    paginator = s3_client.get_paginator('list_objects_v2')
    pages = paginator.paginate(Bucket=bucket_name, Prefix=prefix)

    latest_file = None
    latest_mod_time = None

    for page in pages:
        if 'Contents' in page:
            for obj in page['Contents']:
                if obj['Key'].endswith('zepplin'):
                    mod_time = obj['LastModified']
                    if latest_mod_time is None or mod_time > latest_mod_time:
                        latest_mod_time = mod_time
                        latest_file = obj

    return latest_file, latest_mod_time

def terminate_emr_if_old(emr_client, cluster_id, last_mod_time):
    """Terminate EMR if the latest file is older than 2 hours."""
    now = datetime.now(timezone.utc)
    if last_mod_time and (now - last_mod_time > timedelta(hours=2)):
        print(f"Terminating cluster {cluster_id} as latest file is older than 2 hours.")
        emr_client.terminate_job_flows(JobFlowIds=[cluster_id])
    else:
        print(f"Cluster {cluster_id} is safe. Latest file is within 2 hours.")

def lambda_handler(event, context):
    # Initialize AWS clients for EMR and S3 inside the Lambda function
    emr_client = boto3.client('emr', region_name='us-east-1')
    s3_client = boto3.client('s3')

    # Step 1: Get active EMRs filtered by 'daily cluster'
    emr_ids = get_active_emrs(emr_client)
    print(f"Found {len(emr_ids)} clusters: {emr_ids}")

    # Step 2: Process each cluster, find latest zepplin file, and terminate if necessary
    for cluster_id in emr_ids:
        latest_file, last_mod_time = get_latest_zepplin_file(s3_client, cluster_id)
        
        if latest_file:
            print(f"Latest 'zepplin' file for cluster {cluster_id}: {latest_file['Key']} (Last modified: {last_mod_time})")
            terminate_emr_if_old(emr_client, cluster_id, last_mod_time)
        else:
            print(f"No 'zepplin' files found for cluster {cluster_id}")
    
    return {
        'statusCode': 200,
        'body': 'EMR cleanup completed'
    }
