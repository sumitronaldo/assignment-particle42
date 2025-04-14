# ☁️ Terraform: SimpleTimeService AWS ECS Deployment

This repository contains Terraform code to deploy the SimpleTimeService container into a secure AWS ECS Fargate setup.

---

## 📦 Infrastructure Overview

- VPC with 2 public and 2 private subnets
- ECS Fargate cluster and service
- Application Load Balancer in public subnets
- ECS Tasks running in private subnets
- Docker image pulled from Docker Hub

---

## 🚀 Usage

### 🔐 Authenticate with AWS

Make sure you’ve set up your AWS CLI or environment credentials:

```bash
aws configure