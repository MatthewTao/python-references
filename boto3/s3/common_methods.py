import boto3


def delete_object(bucket, object_path, s3_client):
    """
    Function will delete a single object given
    - bucket name
    - and a object path.
    """
    try:
        print(f"Deleting object: {bucket}/{object_path}")
        s3_client.delete_object(Bucket=bucket, Key=object_path)
    except Exception as e:
        print("Could not delete object", e)
        status = {"success": False, "error": f"Error: {e}"}
    else:
        status = {"success": True, "error": ""}
    return status


def delete_operation(bucket, list_of_paths, s3_client, dry_run=0):
    """
    Function will delete everything in the specified bucket
    and in the specified path.

    This function deletes object by object using s3_client.delete_object()

    pass p_dry_run = 1 to do a dry run

    Iterating over a list is usually faster than using s3_client.delete_objects()
    for less than 100 objects.
    Also have more control over behaviour with iteration rather than delete_objects
    """
    # Iterate through the list, deleting each object
    errors = []
    for item in list_of_paths:
        if dry_run == 1:
            # Do a dry run
            print(f"DRY RUN: Would have deleted {bucket}/{item}")
        elif dry_run == 0:
            status = delete_object(bucket, item, s3_client)
            print(f"Deleted {bucket}/{item}")
            if status["success"] is False:
                errors.append(f"Could not delete {item}: {status['error']}")

    return errors


if __name__ == "__main__":
    aws_access_key = "Dummy fetch actual key from config or secret store"
    aws_secret_key = "Dummy fetch actual secret key from config or secret store"
    s3_client = boto3.client(
        "s3", aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key
    )
