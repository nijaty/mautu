# React Overview

## Overview

TCP/IP (Transmission Control Protocol / Internet Protocol) is the foundational communication protocol suite of the internet.

## TCP/IP Layers

| Layer | Name            | Example Protocols      |
|-------|-----------------|------------------------|
| 4     | Application     | HTTP, FTP, DNS, SSH    |
| 3     | Transport       | TCP, UDP               |
| 2     | Internet        | IP, ICMP, ARP          |
| 1     | Network Access  | Ethernet, Wi-Fi        |

## IP Addressing

### IPv4

- 32-bit address written as four octets: `192.168.1.100`
- Private ranges: `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`

### Subnet Mask

```
IP:      192.168.1.100
Mask:    255.255.255.0  (/24)
Network: 192.168.1.0
Broadcast: 192.168.1.255
Hosts:   192.168.1.1 – 192.168.1.254
```

## TCP vs UDP

| Feature      | TCP            | UDP            |
|--------------|----------------|----------------|
| Connection   | Connection-oriented | Connectionless |
| Reliability  | Guaranteed delivery | No guarantee |
| Order        | Ordered        | Unordered      |
| Use cases    | HTTP, SSH, FTP | DNS, VoIP, streaming |

## Common Ports

| Port | Protocol |
|------|----------|
| 22   | SSH      |
| 80   | HTTP     |
| 443  | HTTPS    |
| 53   | DNS      |
| 3306 | MySQL    |
| 5432 | PostgreSQL |

## Useful Commands

```bash
ip addr show              # show IP addresses
ip route                  # show routing table
ss -tulnp                 # list open ports
ping 8.8.8.8              # test connectivity
traceroute 8.8.8.8        # trace route
```

## References

- https://www.ietf.org/rfc/rfc793.txt (TCP)
- https://www.ietf.org/rfc/rfc791.txt (IP)


<span style="color:blue">Blue Text</span>
