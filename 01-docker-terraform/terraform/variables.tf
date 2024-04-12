variable "location" {
    description = "Project location"
    default = "EU"
}

variable "precise_location" {
    description = "Project location with region"
    default = "europe-central2"
}

variable "precise_zone" {
    description = "Project zone"
    default = "europe-central2-a"
}

variable "bq_dataset_name" {
    description = "My BQ dataset_name"
    default = "demo_dataset"
}

variable "gcs_bucket_name" {
    description = "My gcs bucket name"
    default = "curious-furnace-413416-terra-bucket"
}

variable "gcs_storage_class" {
    description = "My Bucket storage class"
    default = "STANDARD"
}

variable "gcs_project" {
    description = "My gcs project id"
    default = "curious-furnace-413416"
}

