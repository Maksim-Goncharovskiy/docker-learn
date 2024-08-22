# Работа с файлами 
По умолчанию файловые системы хоста и контейнера изолированы друг от друга, однако не всегда эта изолированность нам нужна:
- есть необходимость сохранять изменения файлов внутри контейнера, чтобы не потерять их при его остановке(например, при работе с базами данных)
- может быть нужно прокинуть в контейнер файл, который может изменяться на хосте
- нужно организовать общие данные для нескольких контейнеров

Есть два инструмента для синхронизации файловых систем контейнера и хоста:
1. Bind Mount - прокидывание данных в контейнер
2. Volumes - сохранение данных из контейнера

## Bind Mount
- Позволяет связывать любую папку/файл на хосте с папкой/файлом на контейнере
- Нужно передавать абсолютный путь
- Применяется для прокидывания папки/файла в контейнер

Команды для запуска контейнера с монтированием файла:
1. C возможность читать/писать из контейнера: `docker run -v <полный_путь_на_хосте>:<полный_путь_в_контейнере> <образ>`
2. Только на чтение из контейнера: `docker run -v <полный_путь_на_хосте>:<полный_путь_в_контейнере>:ro <образ>`

При использовании Bind Mount папка/файл находится в общем владении хоста и контейнера и может меняться как в контейнере, так и на хосте. 

! Рекомендуется монтировать таким образом только определённые несистемные файлы, так как есть риск изменения/удаления важных системных файлов хоста внутри контейнера.

## Volumes
- Монтирование папок, находящихся в специально отведённом месте(управляемым докером)
- Используется для сохранения данных из контейнера

Volumes VS Bind Mount:
- Volumes не зависят от хоста
- Volumes безопаснее
- Volumes находятся в специально отведённом месте
- Volumes связывают только папки

### Команды:
1. `docker volume ls` — вывести список вольюмов
2. `docker volume create <название>` — создать вольюм
3. `docker volume rm <название>` — удалить вольюм
4. `docker volume prune` — удалить вольюмы, которые не используются контейнерами

Для запуска контейнера с использованием предварительно созданного вольюма:

`docker run -v <название_вольюма>:<полный_путь_в_контейнере> <образ>`

### Инструкция VOLUME в Dockerfile
Создание volume можно прописать в dockerfile при помощи инструкции `VOLUME <dir>`.

Тогда, даже если использование вольюма не будет прописано явно при запуске контейнера, то вольюм всё равно будет создан и будет хранить в себе данные указанной директории dir.

Таким образом, некоторые контейнеры могут втихую создавать себе вольюмы, которые могут занимать место в памяти, поэтому за создаваемыми вольюмами лучше следить.
