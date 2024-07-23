# Grafana & User Authentication

Before running:
1. Create a folder `./www` and add any html (will be web root, eg index.html)
2. Start MySQL and create some database to use as Grafana datasource **OR** use any other datasource you have available

Run:
1. Start Apache httpd  
    `docker-compose -f docker-compose.apache2.yml up`
2. Start Grafana  
    `docker-compose -f docker-compose.grafana.yml up`

    i. Make a dashboard and make it **public**.  
       _Get the public url of the board_

3. Start Flask (authentication app)  
    `docker-compose -f docker-compose.flask.yml up`  
    Source in `./flask` folder

4. Start nginx reverse proxy  
    `docker-compose -f docker-compose.nginx.yml up`  
    Config in `nginx.conf`  
    Rules (executed top to bottom):
    * Urls starting with `.../grafana/` are redirected to `/auth` and **then** `grafana` container -> users are filtered
    * Urls starting with `.../` are redirected to `<flask container>/auth` and **then** `apache2` container
    * Urls starting with `.../login` are redirected to `<flask container>/login`
    * Urls starting with `.../auth` are redirected to `<flask container>/auth`
