# Git Команды 

### Обзор

<span style="color: green;"><strong>Git</strong></span> — это распределённая система контроля версий, которая отслеживает изменения в исходном коде в процессе разработки программного обеспечения.

### Настройка Git

- <span style="color: green;"><strong>git config --global user.name "Your Name"</strong></span> — Установить глобальное имя пользователя Git
- <span style="color: green;"><strong>git config --global user.email "you@example.com"</strong></span> — Установить глобальный email пользователя Git
- <span style="color: green;"><strong>git config --list</strong></span> — Просмотреть все конфигурации Git

### Инициализация проекта

- <span style="color: green;"><strong>git init</strong></span> — Инициализировать новый репозиторий Git
- <span style="color: green;"><strong>git clone</strong></span> — Клонировать существующий репозиторий

### Базовые снимки состояния

- <span style="color: green;"><strong>git status</strong></span> — Проверить текущее состояние репозитория
- <span style="color: green;"><strong>git add</strong></span> — Добавить файл в индекс для коммита
- <span style="color: green;"><strong>git add .</strong></span> — Добавить все изменения в директории в индекс
- <span style="color: green;"><strong>git commit -m "message"</strong></span> — Зафиксировать изменения с сообщением
- <span style="color: green;"><strong>git diff</strong></span> — Просмотреть неиндексированные изменения
- <span style="color: green;"><strong>git diff --staged</strong></span> — Просмотреть изменения, добавленные в индекс

### Ветвление

- <span style="color: green;"><strong>git branch</strong></span> — Список всех веток
- <span style="color: green;"><strong>git branch <имя></strong></span> — Создать новую ветку
- <span style="color: green;"><strong>git checkout <ветка></strong></span> — Переключиться на другую ветку
- <span style="color: green;"><strong>git checkout -b <ветка></strong></span> — Создать и переключиться на новую ветку
- <span style="color: green;"><strong>git branch -d <ветка></strong></span> — Безопасно удалить ветку

### Слияние и перебазирование

- <span style="color: green;"><strong>git merge <ветка></strong></span> — Слить ветку с текущей
- <span style="color: green;"><strong>git rebase <ветка></strong></span> — Перебазировать текущую ветку на другую

###  Работа с удалёнными репозиториями

- <span style="color: green;"><strong>git remote add origin <url></strong></span> — Привязать удалённый репозиторий
- <span style="color: green;"><strong>git remote -v</strong></span> — Показать URL удалённых репозиториев
- <span style="color: green;"><strong>git push origin <ветка></strong></span> — Отправить ветку на удалённый сервер
- <span style="color: green;"><strong>git pull</strong></span> — Получить и применить изменения с удалённого 
- <span style="color: green;"><strong>git fetch</strong></span> — Получить изменения без слияния

### Отмена изменений

- <span style="color: green;"><strong>git checkout -- <файл></strong></span> — Отменить изменения в файле
- <span style="color: green;"><strong>git reset HEAD <файл></strong></span> — Убрать файл из индекса
- <span style="color: green;"><strong>git revert <коммит></strong></span> — Создать новый коммит для отмены предыдущего
- <span style="color: green;"><strong>git reset --hard <коммит></strong></span> — Сбросить до предыдущего коммита (деструктивно)

### Сохранение изменений в стек

- <span style="color: green;"><strong>git stash</strong></span> — Временно сохранить текущие изменения в стек
- <span style="color: green;"><strong>git stash pop</strong></span> — Применить сохранённые изменения обратно

### Теги

- <span style="color: green;"><strong>git tag <имя></strong></span> — Создать тег
- <span style="color: green;"><strong>git tag</strong></span> — Список всех тегов
- <span style="color: green;"><strong>git push origin <тег></strong></span> — Отправить тег на удалённый сервер