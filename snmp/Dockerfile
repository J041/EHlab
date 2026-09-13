FROM debian:bookworm-slim

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y snmpd && \
    rm -rf /var/lib/apt/lists/*

COPY snmpd.conf /etc/snmp/snmpd.conf

EXPOSE 161/udp

CMD ["snmpd", "-f", "-Lo", "-C", "-c", "/etc/snmp/snmpd.conf"]
