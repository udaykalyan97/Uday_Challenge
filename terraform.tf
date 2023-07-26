terraform {
  required_providers {
    aws = "~> 3.75"
  }
}

resource "aws_s3_bucket" "website" {
  bucket = "my-static-website"
  website {
    index_document = "index.html"
    routing_rules = [
      {
        hostname = "www.example.com"
        redirect_to = "/"
      }
    ]
  }
}
