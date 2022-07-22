# Victm & Ataccker


## Informations

* Descripton: Find the Server IP and the Attacker IP in .pcap file

* Flag Format: BDSEC{serverip_attackerip}


## Getting the flag 

First i open the file using  wireshark and I came across a lot of GET requests requesting random files on the server
<p align="center"><img src="https://github.com/AmoloHT/CTFs/blob/main/BDSec%202022%20CTF/networking/Victim%20%26%20Attacker/h.png"></p>
right away I thought it was a brute force to find files in this web server, with this we have the IP the hacker and the server IP


# Flag

```
BDSEC{192.168.1.13_192.168.1.10}
```
