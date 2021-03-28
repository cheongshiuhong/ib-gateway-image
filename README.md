# Trade IB Gateway
### IB Gateway Docker Container with Github Actions to push to GCR

## How to use

### Setup GCP Project:
- Create a project on GCP Console
- Create a Service Account and create a JSON credentials file
- Enable API for Google Container Registry

### Setup Docker Container:

- Copy from this repository

- Setup a .env file based on .env.localtemplate to test with docker-compose locally.
  <br><b>Note</b>: These should be provided through Cloud Run's environemnt except for the PORT which is provided by default
    - TRADING_MODE=[paper or live]
    - TWSUSERID=[YOUR USERNAME HERE]
    - TWSPASSWORD=[YOUR PASSWORD HERE]
    - PORT=8080 (Google Cloud Run uses port 8080 by default)

- Setup GitHub secrets for:
    - <b>GCR_KEY</b>: The credentials.json from your Google Project's Service Account in base64 form
        <pre><code>cat credentials.json | base64</code></pre>
    - <b>GOOGLE_PROJECT_ID</b>: The id of your project on GCP
    - <b>IMAGE</b>: The name of the image on Google Container Registry
