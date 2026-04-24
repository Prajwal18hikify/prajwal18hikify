# Cloud Guard - Day 1

## How the internet works

When we enter a website URL:

1. Browser sends request
2. DNS converts domain to IP address
3. Request goes to server
4. Server responds with website data

_ _ _


## DNS Resolution Flow

1. Browser cache
2. OS cache
3. Resolver
4. Root server
5. TLD server (.com, .org)
6. Authoritative server
7. Returns IP address

_ _ _ 

## Common Ports

-HTTP → 80
-HTTPS → 443
-DNS → 53
-SSH → 22

_ _ _

# Why this matters for security

- DNS spofing attacks
- open ports risk
- Misconfigured servers

# eg;
user (Browser)
    ↓
Enter URL (google.com)
    ↓
DNS Resolver
    ↓
Final IP address (142.250.xxx.xxx)
    ↓
Web Server (Google)
    ↓
Response (HTML, CSS, JS)
    ↓
Browser Displays Website


# DNS Resolution Diagram

Browser Cache
    ↓
OS Cache
    ↓
DNS Resolver
    ↓
Root Server
    ↓
TLD Server (.com)
    ↓
Authorative Server
    ↓
Returns IP address

## Security Risks in DNS

- DNS Spoffing → Fake IP address returned
- DNS Cache Poisoning → Corrupt cached DNS data
- Open DNS Resolver → Can be abused for attacks

# Prevention

- Use HTTP (Port 443)
- Use secure DNS (DoH / DoT)
- Restrict open ports
