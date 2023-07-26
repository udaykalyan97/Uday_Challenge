provider "aws" {
  region = "us-east-1"  # Replace with your preferred region
}

resource "aws_s3_bucket" "static_website_bucket" {
  bucket = "your-unique-bucket-name"  # Replace with your preferred bucket name
  acl    = "public-read"
  website {
    index_document = "index.html"
    error_document = "error.html"
  }
}

resource "aws_s3_bucket_policy" "static_website_policy" {
  bucket = aws_s3_bucket.static_website_bucket.bucket

  policy = jsonencode({
    Version = "2012-10-17",
    Statement = [
      {
        Sid       = "PublicReadGetObject",
        Effect    = "Allow",
        Principal = "*",
        Action    = "s3:GetObject",
        Resource  = "${aws_s3_bucket.static_website_bucket.arn}/*",
      },
    ],
  })
}
