# ---------------------------------------------------------------------------------------------------------------------
# REQUIRED PARAMETERS
# These variables are expected to be passed in.
# ---------------------------------------------------------------------------------------------------------------------

variable "project" {
  description = "The project ID where all resources will be launched."
  type        = string
}

variable "location" {
  description = "The location (region or zone) to deploy the Cloud Run services. Note: Be sure to pick a region that supports Cloud Run."
  type        = string
}

variable "gcr_region" {
  description = "Name of the GCP region where the GCR registry is located. e.g: 'us' or 'eu'."
  type        = string
}

variable "app_engine_location" {
  description = "The location to deploy the app engine service."
  type        = string
}

variable "repository_name" {
  description = "Name of the Google Cloud Source Repository to create."
  type        = string
}

variable "cloud_run_service_name" {
  description = "The name of the Cloud Run service to deploy."
  type        = string
}

variable "tws_userid" {
  description = "Userid for Interactive Brokers"
  type        = string
}

variable "tws_password" {
  description = "Password for Interactive Brokers"
  type        = string
}

variable "tws_trading_mode" {
  description = "Trading mode on Interactive Brokers"
  type        = string
}

# ---------------------------------------------------------------------------------------------------------------------
# OPTIONAL PARAMETERS (Non-sensitive)
# Generally, these values won't need to be changed.
# ---------------------------------------------------------------------------------------------------------------------

variable "branch_name" {
  description = "Example branch name used to trigger builds."
  type        = string
  default     = "master"
}

variable "digest" {
  description = "The docker image digest or tag to deploy."
  type        = string
  default     = "latest"
}

variable "image_name" {
  description = "The name of the image to deploy. Defaults to a publically available image."
  type        = string
  default     = "gcr.io/cloudrun/hello"
}
