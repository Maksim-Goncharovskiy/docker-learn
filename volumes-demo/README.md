# Инструкция 
## Создание вольюма
```bash
$docker volume create demo-data
```

## Сборка образа
Находясь в папке volumes-demo выполнить команду:
```
$docker build -t demo .
```

## Запуск контейнера с вольюмом
```
$docker run -v demo-data:/app/data -p 8000:8000 --name <container-name> demo
```
