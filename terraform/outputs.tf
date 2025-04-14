output "load_balancer_url" {
  value = aws_lb.simpletime.dns_name
  description = "Public URL of the load balancer"
}