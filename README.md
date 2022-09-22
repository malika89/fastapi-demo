## structure
### small app
### large app


## router
+ /docs
+ /redoc
+ /api/v1/*

## alembic
```
pip install alembic

1. init 
 alembic inint alembic=>生成alembic、alembic.ini
2. upgrade
 alembic revision --autogenerate -m "update by alembic"
 alembic upgrade head
3. 继承到prestart.sh
```
## test
```
pytest app/tests

```

