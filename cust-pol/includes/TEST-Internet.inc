term accept-http/s-isrtoinet {
  comment:: "Allow HTTP/S access"
  destination-port:: HTTP HTTPS
  protocol:: tcp
  source-address:: RFC_6598
  destination-address:: ANY
  logging:: syslog
  action:: accept
}

term accept-dns-isrtoinet {
  comment:: "Allow DNS_TCP access"
  destination-port:: DNS
  protocol:: tcp
  source-address:: RFC_6598
  destination-address:: GOOGLE_PUBLIC_DNS
  logging:: syslog
  action:: accept
}

term accept-ssh-isrtoinet {
  comment:: "Allow SSH_TCP access"
  destination-port:: SNMP
  protocol:: udp
  source-address:: RFC_6598
  destination-address:: GOOGLE_PUBLIC_DNS
  logging:: syslog
  action:: accept
}

term accept-tacacs-isrtoinet {
  comment:: "Allow Tacacs access"
  destination-port:: TACACS
  protocol:: tcp
  source-address:: RFC_6598
  destination-address:: GOOGLE_PUBLIC_DNS
  logging:: syslog
  action:: accept
}
