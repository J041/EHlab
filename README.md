# EC2 Enumeration Lab

Single-host beginner enumeration/scanning lab.

## Services

| Port | Service | Intended lesson |
|---|---|---|
| 21/tcp | FTP | Banner + anonymous-style/file enumeration |
| 80/tcp | HTTP | Web enumeration |
| 139,445/tcp | SMB | Share enumeration |
| 161/udp | SNMP | UDP scanning |
| 8080/tcp | HTTP login | Password brute-force practice |
| 8443/tcp | HTTP | Unusual web port |
| 2222/tcp | SSH | Service fingerprinting on a non-standard port |
| 31337/tcp | Custom banner | Do not infer service solely from port number |

## Start

```bash
docker compose up -d --build
```

## Stop / reset

```bash
docker compose down
docker compose up -d --build
```

For a fully clean rebuild:

```bash
docker compose down --volumes --remove-orphans
docker compose build --no-cache
docker compose up -d
```

## Suggested student objectives

1. Identify all exposed TCP ports.
2. Identify the exposed UDP service.
3. Fingerprint each service.
4. Enumerate web content.
5. Discover the virtual host clue.
6. Enumerate the SMB share.
7. Enumerate SNMP information.
8. Identify the service running on TCP/2222.
9. Identify what is actually listening on TCP/31337.
10. Produce an attack-surface table.

## DNS / virtual host exercise

The web server responds differently to:

- `www.lab.local`
- `dev.lab.local`

Students can test the Host header directly or add the EC2 IP to `/etc/hosts`.

## EC2 safety

Do **not** expose this lab to the entire Internet.

Restrict the EC2 Security Group source to your classroom/VPN/public IP range.
At minimum, avoid `0.0.0.0/0` for ports 21, 139, 445, 161/UDP, 2222,
30000-30009, and 31337.

If students connect over the public Internet, TCP/445 may also be blocked by
some ISPs/networks. A VPN into the lab network is preferable.

## Password brute-force exercise

`login.lab.local` hosts an intentionally weak login portal for classroom use.

- Username is discoverable from `/staff-notes.txt`
- No account lockout
- No rate limiting
- No CAPTCHA
- Failed logins return HTTP 401
- Successful login returns a training flag
- Small practice wordlist: `wordlists/passwords.txt`

Suggested workflow: discover `login.lab.local`, inspect the login form, enumerate `/robots.txt`, find `/staff-notes.txt`, identify the username, then test the provided classroom wordlist against the isolated lab service.


## Username enumeration exercise

The login endpoint on `login.lab.local` intentionally leaks whether a username exists.

- Invalid credentials: HTTP `404` + `Invalid credentials`
- Valid username with wrong password: HTTP `401` + `Invalid password`
- Successful authentication: HTTP `200`
- Practice list: `wordlists/usernames.txt`

Suggested workflow:

1. Discover the web service on `login.lab.local`.
2. Send login attempts with candidate usernames and a known-wrong password.
3. Compare the status code and response body.
4. Identify the valid username.
5. Continue with the password brute-force exercise.

The vulnerability is intentional. A production application should normally
use uniform authentication failure responses so account existence is not
disclosed.

### Kali wordlist note

The intended password is `123456`, which is present in Kali Linux's standard
RockYou wordlist at `/usr/share/wordlists/rockyou.txt`.

On some Kali installations, the wordlist may initially be compressed as
`/usr/share/wordlists/rockyou.txt.gz`.


## Enumeration completion flags

The lab now includes explicit completion flags for each major enumeration task:

- Web content enumeration: `D6AkVUh1FEBVXLXjsa6Lw7ETJ95YdJW1`
- FTP enumeration: `uUyyo0i16y3lIbZfw1Anq63OJJRtTxKv`
- SMB enumeration: `TmZzRYggE3XLwK5x65tJscyMIVTFLfMr`
- SNMP enumeration: `0uiKwKIDOMK3bcAxWG4eVEQu8z2GKONM`
- Non-standard SSH port identification: `2xkCpdAy4l6tGZ3YUhv1xd6Gf7i9Kzn9`

Existing flags are preserved:

- `mqYIG8ynxdQfcZQuPkO55mh2VPUDXWdd`
- `uHvvZPjAxIPfZJuDMRPEHIAvW1njHoz7`
- `epITL6KxA2JrCFPUdabmIxQI0AQXTKUa`


## DNS enumeration exercise

The lab exposes a DNS server on:

- `53/udp`
- `53/tcp`

Zone:

- `lab.local`

The intended TXT-record exercise is:

```bash
dig @<TARGET-IP> TXT verify.lab.local
```

The TXT response contains a 32-character completion flag.

Instructor flag:

`fA5WJ5aD7GqFr7AVO5tX2dm7k9eHpjta`


## Build note

The `login.lab.local` page is still served as an Nginx virtual host. Its `/login`
request is proxied internally to a small Python standard-library auth container.
No Python package installation is performed during the Nginx image build, which
avoids Alpine repository/TLS issues on restricted build hosts.
