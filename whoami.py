import google.auth
from google.auth.transport.requests import Request

credentials, project = google.auth.default()

credentials.refresh(Request())

print("Project :", project)
print("Account :", getattr(credentials, "service_account_email", "User Credentials"))
print("Quota Project :", getattr(credentials, "quota_project_id", None))
print("Credential Type :", type(credentials).__name__)