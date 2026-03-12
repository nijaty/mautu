# Система просмотра руководств MAUTU

Полная реализация системы просмотра и управления руководствами для MAUTU с базой данных SQLite.

## Возможности

- **Иерархическая навигация**: Организованные категории руководств (DevOps, Network, Development)
- **Просмотр руководств**: Отображение содержимого с форматированием и управлением размером шрифта
- **Поиск**: Полнотекстовый поиск по заголовкам и содержимому руководств
- **Редактор руководств**: Встроенный диалог для создания и редактирования руководств
- **SQLite**: Лёгкое локальное хранилище по пути `~/.local/share/mautu/docs.db`
- **Масштабируемая архитектура**: Эффективные запросы к базе данных с управлением соединениями

## Быстрый старт

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Запуск приложения

```bash
python3 main.py
```

База данных SQLite создаётся автоматически при первом запуске.

## Руководство по использованию

### Просмотр руководств

1. Нажмите кнопку меню, чтобы открыть боковую панель
2. Перемещайтесь по дереву категорий:
   - **DevOps** → Git, Ansible, Terraform, Kubernetes, Docker
   - **Network** → OSI Model, TCP/IP, ARP
   - **Development** → C++, Python, Algorithms
3. Нажмите на руководство, чтобы отобразить его в центральной панели
4. Используйте кнопки A+ и A- для изменения размера шрифта

### Поиск руководств

1. Введите поисковый запрос в строку поиска вверху
2. Нажмите кнопку поиска
3. Будет отображено первое найденное руководство
4. Поиск выполняется как по заголовкам, так и по содержимому

### Добавление и редактирование руководств

Чтобы добавить кнопку редактора руководств:

1. **Из консоли Python** (для тестирования):
```python
from PySide6.QtWidgets import QApplication
app = QApplication.instance()
window = app.activeWindow()
window.open_manual_editor()           # открыть редактор для нового руководства
window.open_manual_editor(manual_id=1)  # открыть редактор для существующего руководства
```

2. **Добавить кнопку в интерфейс** (рекомендуется):
   - Откройте `mautu_new_design.ui` в Qt Designer
   - Добавьте кнопку «Новое руководство»
   - Подключите её к методу `open_manual_editor()`
   - Перегенерируйте `ui_mautu_new_design.py`

### Диалог редактора руководств

Диалог редактора включает:
- **Заголовок**: Название руководства
- **Категория**: Выбор из конечных категорий (без подкатегорий)
- **Содержимое**: Полный текст руководства (поддерживает HTML)
- **Сохранить/Отмена**: Сохранить в базу данных или отменить изменения

## Архитектура

### Структура каталогов

```
MAUTU/
├── database/
│   ├── __init__.py
│   ├── db_manager.py         # Операции с базой данных
│   └── db_schema.sql         # Схема SQLite
├── ui/
│   ├── __init__.py
│   ├── manual_viewer.py      # Виджет отображения содержимого
│   ├── manual_tree_widget.py # Дерево навигации
│   └── manual_editor_dialog.py # Диалог редактора
├── manuals/
│   ├── DevOps/
│   │   ├── Git/
│   │   │   ├── images/       # Изображения для руководств по Git
│   │   │   └── git-basics.md
│   │   └── Docker/
│   │       ├── images/       # Изображения для руководств по Docker
│   │       └── docker-intro.md
│   └── ...
├── main.py                   # Основное приложение
└── requirements.txt          # Зависимости Python
```

### Использование изображений в руководствах

Поместите изображения в подпапку `images/` рядом с файлом `.md` и укажите относительный путь:

```
manuals/
└── DevOps/
    └── Docker/
        ├── images/
        │   └── architecture.png
        └── docker-intro.md
```

В файле `docker-intro.md`:

```markdown
## Архитектура Docker

![Архитектура Docker](images/architecture.png)
```

Пути к изображениям автоматически преобразуются в абсолютные `file://` URI при импорте, поэтому они корректно отображаются в просмотрщике.

### Схема базы данных

#### Таблица категорий
```sql
CREATE TABLE IF NOT EXISTS categories (
    id            INTEGER PRIMARY KEY AUTOINCREMENT,
    name          TEXT    NOT NULL,
    parent_id     INTEGER REFERENCES categories(id) ON DELETE CASCADE,
    display_order INTEGER DEFAULT 0,
    created_at    TEXT    DEFAULT CURRENT_TIMESTAMP
);
```

#### Таблица руководств
```sql
CREATE TABLE IF NOT EXISTS manuals (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    title       TEXT    NOT NULL,
    category_id INTEGER NOT NULL REFERENCES categories(id) ON DELETE CASCADE,
    content     TEXT,
    created_at  TEXT DEFAULT CURRENT_TIMESTAMP,
    updated_at  TEXT DEFAULT CURRENT_TIMESTAMP,
    UNIQUE (title, category_id)
);
```

### Ключевые компоненты

1. **DatabaseManager** (`database/db_manager.py`)
   - Управление соединениями SQLite
   - CRUD-операции над руководствами
   - Полнотекстовый поиск
   - Запросы иерархии категорий

2. **ManualViewer** (`ui/manual_viewer.py`)
   - Отображение содержимого в формате HTML
   - Управление размером шрифта
   - Стилизованное представление

3. **ManualTreeWidget** (`ui/manual_tree_widget.py`)
   - Иерархическая навигация по категориям
   - Выбор руководства
   - Автообновление при изменениях

4. **ManualEditorDialog** (`ui/manual_editor_dialog.py`)
   - Создание и редактирование руководств
   - Выбор категории
   - Валидация данных

## Добавление примеров содержимого

### Способ 1: через SQLite CLI

```bash
sqlite3 ~/.local/share/mautu/docs.db
```

```sql
INSERT INTO manuals (title, category_id, content) VALUES
('Git Basics', 2, '<h2>Git Introduction</h2><p>Git is a distributed version control system...</p>'),
('Docker Guide', 6, '<h2>Docker Overview</h2><p>Docker is a containerization platform...</p>');
```

### Способ 2: через Python-скрипт

Создайте файл `add_sample_manuals.py`:

```python
from database.db_manager import DatabaseManager

db = DatabaseManager()

# Добавить руководство по Git
db.save_manual(
    title="Git Basics",
    category_id=2,  # категория Git
    content="""
    <h2>Introduction to Git</h2>
    <p>Git is a distributed version control system used for tracking changes in source code.</p>
    <h3>Key Concepts</h3>
    <ul>
        <li>Repository</li>
        <li>Commit</li>
        <li>Branch</li>
        <li>Merge</li>
    </ul>
    """
)

print("Примеры руководств успешно добавлены!")
```

Запустите:
```bash
python3 add_sample_manuals.py
```

## Устранение неполадок

### База данных не найдена

**Проблема**: Приложение не может открыть базу данных

**Решение**:
1. Убедитесь, что каталог `~/.local/share/mautu/` существует (создаётся автоматически при первом запуске)
2. Проверьте права доступа: `ls -la ~/.local/share/mautu/`

### Руководства не отображаются

**Проблема**: Дерево пустое

**Решение**:
1. Проверьте наличие данных в базе:
   ```bash
   sqlite3 ~/.local/share/mautu/docs.db "SELECT COUNT(*) FROM manuals;"
   ```
2. Добавьте примеры руководств (см. выше)
3. Нажмите обновить или перезапустите приложение

### Поиск не работает

**Проблема**: Поиск не возвращает результатов

**Решение**:
1. Убедитесь, что в базе есть данные:
   ```bash
   sqlite3 ~/.local/share/mautu/docs.db "SELECT title FROM manuals;"
   ```
2. Проверьте, совпадает ли запрос с заголовками или содержимым руководств

### Ошибки импорта

**Ошибка**: «ModuleNotFoundError»

**Решение**:
```bash
pip install -r requirements.txt
```

## Планируемые улучшения

1. **Список результатов поиска**: Отображение нескольких результатов поиска
2. **Экспорт руководств**: Экспорт в PDF/Markdown
3. **История версий**: Отслеживание изменений руководств
4. **Теги и метки**: Дополнительная организация помимо категорий
5. **Шаблоны руководств**: Готовые шаблоны для типичных тем
6. **Редактирование на месте**: Редактирование руководств прямо в просмотрщике
7. **Вложения**: Поддержка изображений и файлов
8. **Управление пользователями**: Многопользовательский доступ с правами

## Участие в разработке

Чтобы внести вклад в систему просмотра руководств:

1. Соблюдайте существующую структуру кода
2. Добавляйте docstring ко всем новым функциям
3. Тщательно тестируйте операции с базой данных
4. Обновляйте этот README при добавлении новых функций

## Лицензия

Совпадает с лицензией проекта MAUTU.

## Поддержка

По вопросам и проблемам:
- Изучите этот документ для получения информации об использовании
- Откройте issue в репозитории MAUTU на GitHub
