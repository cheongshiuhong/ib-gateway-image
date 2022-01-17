terraform {
  required_version = ">=0.12.7"

  required_providers {
    google = ">=3.4"
  }
}

# ------------------------------------
# Google Provider
# ------------------------------------
provider "google" {
  credentials = file("./credentials.json")
  project = var.project
}

# ---------------------------------------------
# Firebase Firestore Database
# ---------------------------------------------
resource "google_app_engine_application" "app" {
  location_id   = var.app_engine_location
  database_type = "CLOUD_FIRESTORE"
}

# ---------------------------------------------
# Google Cloud Source Repository
# ---------------------------------------------
resource "google_sourcerepo_repository" "repo" {
  name    = var.repository_name
}

# ---------------------------------------------
# Google Cloud Build
# ---------------------------------------------
resource "google_cloudbuild_trigger" "cloud_build_trigger" {
  description = "Cloud Source Repository Trigger ${var.repository_name} (${var.branch_name})"
  
  trigger_template {
    branch_name = var.branch_name
    repo_name   = var.repository_name
  }

  substitutions = {
    _LOCATION = var.location
    _GCR_REGION = var.gcr_region
    _SERVICE_NAME = var.cloud_run_service_name
  }

  filename = "cloudbuild.yml"

  depends_on = [google_sourcerepo_repository.repo]
}

# ---------------------------------------------
# Google Cloud Run
# ---------------------------------------------
resource "google_cloud_run_service" "service" {
  name     = var.cloud_run_service_name
  location = var.location

  template {
    spec {
      containers {
        image = var.image_name

        env {
          name = "TWS_USERID"
          value = var.tws_userid
        }

        env {
          name = "TWS_PASSWORD"
          value = var.tws_password
        }

        env {
          name = "TWS_TRADING_MODE"
          value = var.tws_trading_mode
        }

        resources {
          limits = {
            cpu    = "2000m"
            memory = "2048Mi"
          }
        }
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }
}

resource "google_cloud_run_service_iam_member" "cloud_run_role" {
  service = google_cloud_run_service.service.name
  location = google_cloud_run_service.service.location
  role = "roles/run.invoker"
  member = "allUsers"
}

# ---------------------------------------------
# Google Cloud Scheduler
# ---------------------------------------------
