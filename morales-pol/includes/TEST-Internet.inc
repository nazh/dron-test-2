term accept-http/s-isrtoinet {
  comment:: "Allow HTTP/S access"
  destination-port:: HTTP HTTPS
  protocol:: tcp
  source-address:: NA-UCS-Srv_subnt_10.189.9.0/24
  destination-address:: ANY
  logging:: syslog
  action:: accept
}

#term accept-dns-isrtoinet {
#  comment:: "Allow DNS_TCP access"
#  destination-port:: DNS
#  protocol:: tcp
#  source-address:: NA-UCS-Srv_subnt_10.189.9.0/24
#  destination-address:: GOOGLE_PUBLIC_DNS
#  logging:: syslog
#  action:: accept
#}

