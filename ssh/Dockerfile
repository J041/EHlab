FROM debian:bookworm-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y openssh-server && \
    rm -rf /var/lib/apt/lists/* && \
    mkdir -p /run/sshd && \
    useradd -m -s /bin/bash student && \
    echo 'student:training-only' | chpasswd

RUN printf '\nPasswordAuthentication yes\nPermitRootLogin no\n' >> /etc/ssh/sshd_config

COPY banner.txt /etc/ssh/banner.txt
RUN printf '\nBanner /etc/ssh/banner.txt\n' >> /etc/ssh/sshd_config

EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-e"]
