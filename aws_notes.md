# AWS Cloud Practitioner Study Notes
## Week 1  | Prajwal CK  | CloudGuard

---

## Domain 1 - Cloud Concepts (24%)

### What is Cloud Computing?
- On-demand IT resources over internet
- Pay as you go - no upfront cost
- scale instantly up or down
- Global in minutes

### IaaS vs PaaS vs SaaS
- IaaS = Infrastructure (EC2, VPC) - you manage OS up
- PaaS = Platform (Elastic Beanstalk) - you manage app only
- SaaS = Software (Gmail, Salesforce) - just use  it
- CloudGuard = SaaS product at $29/month

### AWS Global Infrastructure
- Region = geographic location (ap-south-1 = Mumbai)
- Availability Zone = data centre in regiin (min 2 per region)
- Edge Location = CDN point for CloudFront
- 30+ regions, 90+ AZs worldwide

---

## Domain 2 - Security (30%) - MOST IMPORTANT

### Shared Responsibility Model
- AWS responsible FOR the cloud:
Physical servers, network, hypervision, facilities
- Customer responsible IN the cloud:
OS patches, IAM, Security Groups, encryption, app security
- CloudGuard helps customers fulfill THEIR responsibility

### IAM -Identity and Access Management
- Root account = god mode, never use, enable MFA immediately
- Users = individual people, long-term credentials
- Groups = collection of users, assign policies to group
- Roles = temporary credentials for services/apps
- Policies = JSON defining allowed/denied actions
- Best practices: least privilege, MFA, rotate keys

### Key Security Services
- GuardDuty = threat detection (ML on CloudTrail + VPC Flow Logs)
- CloudTrail = API call logging (MUST be enabled all regions)
- Config = configuration compliance monitoring
- Inspector = vulnerability scanning for EC2
- Security Hub = aggregated security findings
- Macie = sensitive data discovery in S3
- KMS = Key Management Service

---