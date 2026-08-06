from google.cloud import storage

client = storage.Client(project="global-job-market-etl")

print("Project:", client.project)

bucket = client.bucket("global-job-market-etl-bronze")

blob = bucket.blob("python_test.txt")

blob.upload_from_string("Hello from Python!")

print("Upload successful!")