# Trade IB Gateway
### IB Gateway Docker Container with Github Actions to push to GCR

## How to use

### Setup GCP Project:
- Create a project on GCP Console
- Create a Service Account and create a JSON credentials file
- Enable API for Google Container Registry

### Setup Docker Container:
- Copy from this repository
- Setup a .env file based on .env.template to test with docker-compose locally
    - TRADING_MODE=[paper or live]
    - TWSUSERID=[YOUR USERNAME HERE]
    - TWSPASSWORD=[YOUR PASSWORD HERE]
    - PORT=8080 (Google Cloud Run uses port 8080 by default)
- Setup github secrets for everything mentioned above with the exceptions:
    - <b>PORT</b> - Exclude it since Google Cloud Run provides it
    - <b>GOOGLE_PROJECT_ID</b>: Include the id of your project on GCP
    - <b>GCR_KEY</b>: Include the credentials.json from your Google Project's Service Account in base64 form
<pre><code>cat credentials.json | base64</code></pre>
