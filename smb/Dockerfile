FROM debian:bookworm-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y samba && \
    rm -rf /var/lib/apt/lists/*

COPY smb.conf /etc/samba/smb.conf

RUN mkdir -p /srv/samba/public && chmod 0777 /srv/samba/public

EXPOSE 139 445

CMD ["smbd", "--foreground", "--no-process-group"]
