# RECOLECTA APP

---

### Quick setup

Clone the repo and move to the folder, then:

```
# If you don't have poetry, install it:
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python

# create venv & install dependencies
poetry install

# Run server
poetry run python recolectadjango/manage.py runserver localhost:8000
```

### SSL certs
##### nginx without docker
```
server {
  listen 80 default_server;
  listen [::]:80 default_server ipv6only=on;
  server_name tucanoar.com *.tucanoar.com;
  root /var/lib/letsencrypt;

  location ^~ /.well-known/acme-challenge/ {
    default_type "text/plain";
    root /var/lib/letsencrypt;
  }

  location / {
    try_files $uri $uri/ =404;
  }
}
```

`certbot certonly --webroot -w /var/lib/letsencrypt -d tucanoar.com -d www.tucanoar.com`
* _Remember to add other subdomains_
