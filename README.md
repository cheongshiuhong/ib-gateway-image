# IB Gateway Image
### Terraform GCP Infrastructure 
### IB Gateway Docker Container

### Setup GCP Project:
- Create a project on GCP Console
- Create a Service Account and create a JSON credentials file
- Enable API for Google Cloud Source Repository
- Enable API for Google Cloud Build
- Enable API for Google Container Registry
- Enable API for Google Cloud Run
- Enable API for Google App Engine Admin
- Set IAM Policy for Cloud Build Service Account to <b>editor</b>


### Setup Terraform
- Place <em>main project</em>'s credentials.json file isnide <b>infrastructure</b> folder
- Create a terraform.tfvars file based on terraform.tfvars.example to input project details
  <br><b>Note</b>: These will be used to configure the resources and provide environment variables for Cloud Run


### Setup Local Environment:

#### Local Environment Variables with Docker Compose
- Create a .env file based on .env.localtemplate to test with docker-compose locally.
  <br><b>Note</b>: These should be provided through Cloud Run's environemnt except for the PORT which is provided by default

#### Local Environment for Firestore (Use a separate project for testing)
- Place <em>testing project</em>'s credentials.json file for Firestore DB inside <b>app</b> folder 
    - Docker will copy into image for local testing
    - Note: Terraform will use this to create infrastructure resources
