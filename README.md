# simple-query-optimization-task   


## Run  

```bash
# to run the project 
docker compose up -d 
# db migrate
docker compose exec fred python manage.py migrate 
# populate db 
docker compose exec fred python manage.py generate_data --users 20 --products 400 --orders 1000 --orderitems 4000
```    

