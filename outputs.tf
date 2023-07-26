output "website_domain_name" {
  value = var.domain_name
}

output "website_s3_bucket_arn" {
  value = aws_s3_bucket.website.arn
}
