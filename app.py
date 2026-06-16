from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# =============================================
# КОНТЕНТ ЭНЦИКЛОПЕДИИ
# Чтобы добавить фото к статье — укажите имя файла в поле "image"
# (файл должен лежать в static/images/)
# =============================================

ARTICLES = {
    "python": {
        "title": "Python",
        "category": "languages",
        "category_title": "Языки программирования",
        "icon": "🐍",
        "short": "Высокоуровневый язык общего назначения с простым и читаемым синтаксисом",
        "image": None,  # Пример: "python.jpg" — файл static/images/python.jpg
        "course_title": "Python для начинающих",
        "course_url": "https://stepik.org/course/67/promo",
        "text": """
            <p>Python — интерпретируемый язык программирования высокого уровня, созданный Гвидо ван Россумом и впервые выпущенный в 1991 году. Философия языка делает акцент на читаемости кода и лаконичности.</p>

            <h3>Ключевые особенности</h3>
            <ul>
                <li><strong>Динамическая типизация</strong> — тип переменной определяется автоматически во время выполнения</li>
                <li><strong>Автоматическое управление памятью</strong> — сборщик мусора освобождает неиспользуемые объекты</li>
                <li><strong>Мультипарадигменность</strong> — поддерживает ООП, функциональное и процедурное программирование</li>
                <li><strong>Богатая стандартная библиотека</strong> — «batteries included» подход</li>
                <li><strong>Кроссплатформенность</strong> — работает на Windows, macOS, Linux</li>
            </ul>

            <h3>Применение</h3>
            <ul>
                <li>Машинное обучение и Data Science (NumPy, Pandas, TensorFlow, PyTorch)</li>
                <li>Веб-разработка (Django, Flask, FastAPI)</li>
                <li>Автоматизация и скриптинг</li>
                <li>Научные вычисления</li>
                <li>Разработка игр (pygame)</li>
            </ul>

            <h3>Пример кода</h3>
            <pre><code># Классическое приветствие
def hello(name: str) -> str:
    return f"Привет, {name}!"

print(hello("Мир"))

# Списковое включение
squares = [x**2 for x in range(10)]
print(squares)</code></pre>

            <h3>Zen of Python</h3>
            <p>В язык встроен свод принципов — «Дзен Python». Главные из них: <em>«Явное лучше неявного», «Простое лучше сложного», «Читаемость имеет значение»</em>.</p>

            <p><strong>Создатель:</strong> Гвидо ван Россум | <strong>Год:</strong> 1991 | <strong>Текущая версия:</strong> Python 3.12+</p>
        """
    },
    "javascript": {
        "title": "JavaScript",
        "category": "languages",
        "category_title": "Языки программирования",
        "icon": "🌐",
        "short": "Язык сценариев для веба, единственный нативный язык браузера",
        "image": None,
        "course_title": "JavaScript для начинающих",
        "course_url": "https://stepik.org/course/2223/promo",
        "text": """
            <p>JavaScript — высокоуровневый интерпретируемый язык программирования, стандарт веб-разработки. Создан Бренданом Айком в 1995 году всего за 10 дней. Несмотря на название, не имеет никакого отношения к Java.</p>

            <h3>Ключевые особенности</h3>
            <ul>
                <li><strong>Прототипное наследование</strong> — объекты наследуют свойства напрямую от других объектов</li>
                <li><strong>Асинхронность</strong> — event loop, Promise, async/await</li>
                <li><strong>Первоклассные функции</strong> — функции являются объектами</li>
                <li><strong>Замыкания (closures)</strong> — функции запоминают своё лексическое окружение</li>
                <li><strong>Ubiquity</strong> — единственный язык, нативно работающий в браузере</li>
            </ul>

            <h3>Экосистема</h3>
            <ul>
                <li><strong>Node.js</strong> — серверный JavaScript</li>
                <li><strong>React, Vue, Angular</strong> — фронтенд-фреймворки</li>
                <li><strong>TypeScript</strong> — строго типизированный надъязык JS</li>
                <li><strong>npm / yarn / pnpm</strong> — пакетные менеджеры</li>
                <li><strong>Electron</strong> — десктопные приложения на JS</li>
            </ul>

            <h3>Пример кода</h3>
            <pre><code>// Стрелочная функция и Promise
const fetchUser = async (id) => {
  const res = await fetch(`/api/users/${id}`);
  const user = await res.json();
  return user;
};

// Деструктуризация
const { name, age } = await fetchUser(1);
console.log(`${name}, ${age} лет`);</code></pre>

            <p><strong>Создатель:</strong> Брендан Айк | <strong>Год:</strong> 1995 | <strong>Стандарт:</strong> ECMAScript 2024</p>
        """
    },
    "git": {
        "title": "Git",
        "category": "tools",
        "category_title": "Инструменты",
        "icon": "🔀",
        "short": "Распределённая система контроля версий, стандарт индустрии",
        "image": None,
        "course_title": "Введение в Git и GitHub",
        "course_url": "https://stepik.org/course/3145/promo",
        "text": """
            <p>Git — распределённая система управления версиями, созданная Линусом Торвальдсом в 2005 году для разработки ядра Linux. Сегодня это абсолютный стандарт для командной разработки.</p>

            <h3>Базовые концепции</h3>
            <ul>
                <li><strong>Репозиторий (repo)</strong> — хранилище истории проекта</li>
                <li><strong>Коммит (commit)</strong> — снимок состояния файлов в момент времени</li>
                <li><strong>Ветка (branch)</strong> — независимая линия разработки</li>
                <li><strong>Merge</strong> — объединение веток</li>
                <li><strong>Rebase</strong> — перенос коммитов на другую ветку</li>
                <li><strong>Remote</strong> — удалённый репозиторий (GitHub, GitLab)</li>
            </ul>

            <h3>Основные команды</h3>
            <pre><code># Инициализация и первый коммит
git init
git add .
git commit -m "Initial commit"

# Работа с ветками
git branch feature/auth
git checkout feature/auth
git merge main

# Синхронизация с удалённым репо
git pull origin main
git push origin feature/auth</code></pre>

            <h3>Модели ветвления</h3>
            <ul>
                <li><strong>Git Flow</strong> — классическая модель с develop/main/feature/hotfix</li>
                <li><strong>GitHub Flow</strong> — упрощённая: main + feature branches + PR</li>
                <li><strong>Trunk-Based Development</strong> — все коммитят напрямую в main</li>
            </ul>

            <p><strong>Создатель:</strong> Линус Торвальдс | <strong>Год:</strong> 2005 | <strong>Лицензия:</strong> GPL-2.0</p>
        """
    },
    "algorithms": {
        "title": "Алгоритмы и структуры данных",
        "category": "cs",
        "category_title": "Информатика",
        "icon": "🧮",
        "short": "Фундаментальные алгоритмы и структуры данных, основа CS",
        "image": None,
        "course_title": "Алгоритмы: теория и практика",
        "course_url": "https://stepik.org/course/217/promo",
        "text": """
            <p>Алгоритмы и структуры данных — фундамент информатики. Понимание этих концепций позволяет писать эффективный код и решать сложные задачи.</p>

            <h3>Основные структуры данных</h3>
            <ul>
                <li><strong>Массив (Array)</strong> — последовательность элементов с индексами. O(1) доступ, O(n) вставка</li>
                <li><strong>Связный список (Linked List)</strong> — узлы с указателями. O(1) вставка, O(n) доступ</li>
                <li><strong>Стек (Stack)</strong> — LIFO. Используется в управлении вызовами функций</li>
                <li><strong>Очередь (Queue)</strong> — FIFO. Используется в BFS, планировщиках</li>
                <li><strong>Хеш-таблица (Hash Map)</strong> — O(1) доступ по ключу в среднем</li>
                <li><strong>Дерево (Tree)</strong> — иерархические данные. BST, AVL, Red-Black</li>
                <li><strong>Граф (Graph)</strong> — вершины и рёбра. Directed/Undirected</li>
            </ul>

            <h3>Сортировки</h3>
            <ul>
                <li><strong>Bubble Sort</strong> — O(n²), учебный алгоритм</li>
                <li><strong>Quick Sort</strong> — O(n log n) среднее, O(n²) худший случай</li>
                <li><strong>Merge Sort</strong> — O(n log n) гарантировано, стабильный</li>
                <li><strong>Heap Sort</strong> — O(n log n), O(1) доп. памяти</li>
                <li><strong>Counting Sort</strong> — O(n+k), только для целых чисел в диапазоне</li>
            </ul>

            <h3>Нотация Big O</h3>
            <pre><code>O(1)       — константное время. Доступ к элементу массива
O(log n)   — логарифмическое. Бинарный поиск
O(n)       — линейное. Линейный поиск
O(n log n) — линейно-логарифмическое. Быстрая сортировка
O(n²)      — квадратичное. Пузырьковая сортировка
O(2ⁿ)      — экспоненциальное. Перебор подмножеств</code></pre>

            <h3>Ключевые алгоритмы</h3>
            <ul>
                <li><strong>BFS / DFS</strong> — обходы графа и дерева</li>
                <li><strong>Dijkstra</strong> — кратчайший путь в взвешенном графе</li>
                <li><strong>Dynamic Programming</strong> — оптимизация через мемоизацию</li>
                <li><strong>Binary Search</strong> — поиск в отсортированном массиве за O(log n)</li>
            </ul>
        """
    },
    "oop": {
        "title": "ООП",
        "category": "cs",
        "category_title": "Информатика",
        "icon": "🏗️",
        "short": "Объектно-ориентированное программирование — парадигма разработки",
        "image": None,
        "course_title": "ООП в Python",
        "course_url": "https://stepik.org/course/7399/promo",
        "text": """
            <p>Объектно-ориентированное программирование (ООП) — парадигма, в основе которой лежат объекты, сочетающие данные (атрибуты) и поведение (методы).</p>

            <h3>Четыре столпа ООП</h3>
            <ul>
                <li><strong>Инкапсуляция</strong> — скрытие внутренней реализации. Данные защищены и доступны только через методы</li>
                <li><strong>Наследование</strong> — класс-потомок получает свойства родителя и может их расширять</li>
                <li><strong>Полиморфизм</strong> — один интерфейс, разные реализации. Метод ведёт себя по-разному в зависимости от объекта</li>
                <li><strong>Абстракция</strong> — выделение существенных характеристик, скрытие деталей реализации</li>
            </ul>

            <h3>Пример на Python</h3>
            <pre><code>class Animal:
    def __init__(self, name: str):
        self._name = name  # protected

    def speak(self) -> str:
        raise NotImplementedError

class Dog(Animal):          # Наследование
    def speak(self) -> str: # Полиморфизм
        return f"{self._name}: Гав!"

class Cat(Animal):
    def speak(self) -> str:
        return f"{self._name}: Мяу!"

animals = [Dog("Рекс"), Cat("Мурка")]
for a in animals:
    print(a.speak())  # Полиморфизм в действии</code></pre>

            <h3>Принципы SOLID</h3>
            <ul>
                <li><strong>S</strong> — Single Responsibility: один класс — одна задача</li>
                <li><strong>O</strong> — Open/Closed: открыт для расширения, закрыт для изменения</li>
                <li><strong>L</strong> — Liskov Substitution: подкласс заменяет базовый класс</li>
                <li><strong>I</strong> — Interface Segregation: много специализированных интерфейсов</li>
                <li><strong>D</strong> — Dependency Inversion: зависимость от абстракций, не реализаций</li>
            </ul>

            <h3>Паттерны проектирования</h3>
            <ul>
                <li><strong>Singleton</strong> — единственный экземпляр класса</li>
                <li><strong>Factory</strong> — создание объектов через фабричный метод</li>
                <li><strong>Observer</strong> — подписка на события объекта</li>
                <li><strong>Strategy</strong> — взаимозаменяемые алгоритмы</li>
                <li><strong>Decorator</strong> — динамическое добавление поведения</li>
            </ul>
        """
    },
    "databases": {
        "title": "Базы данных",
        "category": "tools",
        "category_title": "Инструменты",
        "icon": "🗄️",
        "short": "Реляционные и нереляционные СУБД, SQL, проектирование схем",
        "image": None,
        "course_title": "Интерактивный тренажёр по SQL",
        "course_url": "https://stepik.org/course/63054/promo",
        "text": """
            <p>База данных — организованная структура для хранения, управления и извлечения информации. Выбор СУБД критически влияет на архитектуру приложения.</p>

            <h3>Реляционные базы данных (SQL)</h3>
            <p>Данные хранятся в таблицах с жёсткой схемой. Поддерживают ACID-транзакции.</p>
            <ul>
                <li><strong>PostgreSQL</strong> — мощная open-source СУБД, поддерживает JSON, полнотекстовый поиск</li>
                <li><strong>MySQL / MariaDB</strong> — популярны в веб-разработке</li>
                <li><strong>SQLite</strong> — встраиваемая БД, хранится в одном файле</li>
                <li><strong>Microsoft SQL Server / Oracle</strong> — корпоративные решения</li>
            </ul>

            <h3>Основы SQL</h3>
            <pre><code>-- Создание таблицы
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(200) UNIQUE,
    created_at TIMESTAMP DEFAULT NOW()
);

-- CRUD операции
INSERT INTO users (name, email) VALUES ('Алиса', 'alice@example.com');
SELECT * FROM users WHERE name LIKE 'А%';
UPDATE users SET email = 'new@mail.com' WHERE id = 1;
DELETE FROM users WHERE id = 1;

-- JOIN
SELECT u.name, o.total
FROM users u
JOIN orders o ON o.user_id = u.id
WHERE o.total > 1000;</code></pre>

            <h3>NoSQL базы данных</h3>
            <ul>
                <li><strong>MongoDB</strong> — документно-ориентированная, JSON-like документы</li>
                <li><strong>Redis</strong> — in-memory хранилище, кэш, pub/sub, очереди</li>
                <li><strong>Elasticsearch</strong> — поиск и аналитика</li>
                <li><strong>Cassandra</strong> — распределённая колоночная БД</li>
            </ul>

            <h3>Индексы и оптимизация</h3>
            <ul>
                <li><strong>B-tree индекс</strong> — универсальный, подходит для большинства запросов</li>
                <li><strong>Hash индекс</strong> — быстрый поиск по точному совпадению</li>
                <li><strong>EXPLAIN / EXPLAIN ANALYZE</strong> — анализ плана выполнения запроса</li>
                <li><strong>N+1 проблема</strong> — классическая ошибка при работе с ORM</li>
            </ul>

            <h3>Нормализация</h3>
            <p>1NF → 2NF → 3NF → BCNF — последовательное устранение аномалий данных. Денормализация применяется осознанно для производительности.</p>
        """
    },
    "web": {
        "title": "Веб-разработка",
        "category": "areas",
        "category_title": "Области разработки",
        "icon": "💻",
        "short": "Frontend, Backend, Full-stack: технологии, инструменты, архитектуры",
        "image": None,
        "text": """
            <p>Веб-разработка охватывает создание сайтов и веб-приложений — от простых лендингов до сложных SaaS-платформ с миллионами пользователей.</p>

            <h3>Frontend</h3>
            <p>Всё, что видит и с чем взаимодействует пользователь в браузере.</p>
            <ul>
                <li><strong>HTML5</strong> — структура и семантика страниц</li>
                <li><strong>CSS3</strong> — стилизация, Flexbox, Grid, анимации</li>
                <li><strong>JavaScript / TypeScript</strong> — интерактивность</li>
                <li><strong>React</strong> — компонентная библиотека от Meta</li>
                <li><strong>Vue.js</strong> — прогрессивный фреймворк</li>
                <li><strong>Next.js / Nuxt.js</strong> — SSR/SSG фреймворки</li>
                <li><strong>Webpack / Vite</strong> — сборщики модулей</li>
            </ul>

            <h3>Backend</h3>
            <p>Серверная логика, API, базы данных.</p>
            <ul>
                <li><strong>REST API</strong> — архитектурный стиль на HTTP</li>
                <li><strong>GraphQL</strong> — гибкий язык запросов к API</li>
                <li><strong>Django / FastAPI</strong> — Python фреймворки</li>
                <li><strong>Express.js / NestJS</strong> — Node.js фреймворки</li>
                <li><strong>Spring Boot</strong> — Java фреймворк</li>
                <li><strong>Go / Rust</strong> — высокопроизводительные языки</li>
            </ul>

            <h3>HTTP и протоколы</h3>
            <pre><code>GET    /api/users       # Получить список
POST   /api/users       # Создать пользователя
PUT    /api/users/1     # Обновить полностью
PATCH  /api/users/1     # Частичное обновление
DELETE /api/users/1     # Удалить

Коды ответов:
2xx — успех (200 OK, 201 Created)
3xx — перенаправление
4xx — ошибка клиента (404 Not Found, 401 Unauthorized)
5xx — ошибка сервера</code></pre>

            <h3>DevOps для веба</h3>
            <ul>
                <li><strong>Docker</strong> — контейнеризация приложений</li>
                <li><strong>Nginx / Caddy</strong> — веб-серверы и reverse proxy</li>
                <li><strong>CI/CD</strong> — автоматизация деплоя</li>
                <li><strong>CDN</strong> — сети доставки контента</li>
            </ul>
        """
    },
    "linux": {
        "title": "Linux и командная строка",
        "category": "tools",
        "category_title": "Инструменты",
        "icon": "🐧",
        "short": "Основы работы в Linux, bash-скриптинг и системное администрирование",
        "image": None,
        "course_title": "Введение в Linux",
        "course_url": "https://stepik.org/course/73/promo",
        "text": """
            <p>Linux — семейство Unix-подобных операционных систем на основе ядра Linux, созданного Линусом Торвальдсом в 1991 году. Большинство серверов в мире работает на Linux.</p>

            <h3>Файловая система</h3>
            <pre><code>/           # Корневой каталог
├── bin/    # Исполняемые файлы
├── etc/    # Конфигурационные файлы
├── home/   # Домашние папки пользователей
├── var/    # Переменные данные (логи, БД)
├── tmp/    # Временные файлы
├── usr/    # Программы и библиотеки
└── proc/  # Виртуальная ФС — информация о процессах</code></pre>

            <h3>Базовые команды</h3>
            <pre><code># Навигация
ls -la          # Список файлов с деталями
cd /var/log     # Смена директории
pwd             # Текущая директория
find / -name "*.log"  # Поиск файлов

# Работа с файлами
cp src dst      # Копировать
mv src dst      # Переместить / переименовать
rm -rf dir/     # Удалить рекурсивно
chmod 755 file  # Права доступа
chown user file # Владелец файла

# Процессы и сеть
ps aux          # Список процессов
top / htop      # Мониторинг ресурсов
kill -9 PID     # Завершить процесс
netstat -tlnp   # Открытые порты
ss -tulpn       # Современная альтернатива netstat
curl -I url     # HTTP-запрос заголовков</code></pre>

            <h3>Bash-скриптинг</h3>
            <pre><code>#!/bin/bash
# Простой скрипт резервного копирования

BACKUP_DIR="/backups"
DATE=$(date +%Y-%m-%d)

for dir in /etc /home; do
  tar -czf "$BACKUP_DIR/${dir//\//_}-$DATE.tar.gz" "$dir"
  echo "Создан бэкап: $dir"
done

echo "Готово! Резервные копии в $BACKUP_DIR"</code></pre>

            <h3>Пакетные менеджеры</h3>
            <ul>
                <li><strong>apt</strong> — Debian/Ubuntu</li>
                <li><strong>dnf / yum</strong> — Red Hat/Fedora/CentOS</li>
                <li><strong>pacman</strong> — Arch Linux</li>
                <li><strong>snap / flatpak</strong> — универсальные пакеты</li>
            </ul>

            <p><strong>Популярные дистрибутивы:</strong> Ubuntu, Debian, Fedora, Arch Linux, CentOS/Rocky Linux</p>
        """
    },
    "devops": {
        "title": "DevOps",
        "category": "areas",
        "category_title": "Области разработки",
        "icon": "⚙️",
        "short": "Docker, Kubernetes, CI/CD, Infrastructure as Code",
        "image": None,
        "course_title": "DevOps для разработчиков",
        "course_url": "https://stepik.org/course/77005/promo",
        "text": """
            <p>DevOps — культура и набор практик, объединяющих разработку (Dev) и эксплуатацию (Ops) для ускорения доставки программного обеспечения с высоким качеством.</p>

            <h3>Docker</h3>
            <p>Контейнеризация — упаковка приложения со всеми зависимостями.</p>
            <pre><code># Dockerfile для Python-приложения
FROM python:3.12-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]</code></pre>

            <pre><code># docker-compose.yml
version: '3.9'
services:
  web:
    build: .
    ports: ["8000:8000"]
    depends_on: [db]
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data

volumes:
  pgdata:</code></pre>

            <h3>Kubernetes</h3>
            <p>Оркестратор контейнеров для управления кластерами.</p>
            <ul>
                <li><strong>Pod</strong> — минимальная единица деплоя (1+ контейнеров)</li>
                <li><strong>Deployment</strong> — управление репликами подов</li>
                <li><strong>Service</strong> — сетевой доступ к подам</li>
                <li><strong>Ingress</strong> — HTTP-маршрутизация</li>
                <li><strong>ConfigMap / Secret</strong> — конфигурация и секреты</li>
            </ul>

            <h3>CI/CD</h3>
            <ul>
                <li><strong>GitHub Actions</strong> — интегрированный CI/CD</li>
                <li><strong>GitLab CI</strong> — встроен в GitLab</li>
                <li><strong>Jenkins</strong> — самохостинговый сервер</li>
                <li><strong>ArgoCD</strong> — GitOps для Kubernetes</li>
            </ul>

            <h3>Infrastructure as Code</h3>
            <ul>
                <li><strong>Terraform</strong> — декларативное описание инфраструктуры</li>
                <li><strong>Ansible</strong> — конфигурация серверов через плейбуки</li>
                <li><strong>Pulumi</strong> — IaC на реальных языках программирования</li>
            </ul>

            <h3>Мониторинг</h3>
            <ul>
                <li><strong>Prometheus + Grafana</strong> — метрики и дашборды</li>
                <li><strong>ELK Stack</strong> — Elasticsearch, Logstash, Kibana для логов</li>
                <li><strong>Jaeger / Zipkin</strong> — распределённая трассировка</li>
            </ul>
        """
    },
    "cpp": {
        "title": "C++",
        "category": "languages",
        "category_title": "Языки программирования",
        "icon": "⚡",
        "short": "Системный язык высокой производительности, развитие языка C",
        "image": None,
        "course_title": "Программирование на C++",
        "course_url": "https://stepik.org/course/7/promo",
        "text": """
            <p>C++ — компилируемый язык программирования общего назначения, созданный Бьёрном Страуструпом в 1983 году как расширение языка C. Один из самых производительных языков — используется в системном ПО, играх, финансах, встроенных системах.</p>

            <h3>Ключевые особенности</h3>
            <ul>
                <li><strong>Статическая типизация</strong> — типы проверяются на этапе компиляции</li>
                <li><strong>Ручное управление памятью</strong> — прямой контроль через указатели</li>
                <li><strong>RAII</strong> — Resource Acquisition Is Initialization, умное управление ресурсами</li>
                <li><strong>Шаблоны (Templates)</strong> — обобщённое программирование</li>
                <li><strong>Близость к железу</strong> — доступ к указателям, битовым операциям</li>
            </ul>

            <h3>Современный C++ (C++17/20/23)</h3>
            <pre><code>#include &lt;iostream&gt;
#include &lt;vector&gt;
#include &lt;ranges&gt;

int main() {
    std::vector&lt;int&gt; nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

    // C++20 Ranges
    auto even_squares = nums
        | std::views::filter([](int n){ return n % 2 == 0; })
        | std::views::transform([](int n){ return n * n; });

    for (auto n : even_squares)
        std::cout &lt;&lt; n &lt;&lt; " ";  // 4 16 36 64 100

    return 0;
}</code></pre>

            <h3>Умные указатели</h3>
            <pre><code>// Вместо ручного delete — умные указатели
auto ptr = std::make_unique&lt;MyClass&gt;(args);
auto shared = std::make_shared&lt;Resource&gt;();
// Память освобождается автоматически</code></pre>

            <h3>Области применения</h3>
            <ul>
                <li>Игровые движки (Unreal Engine, CryEngine)</li>
                <li>Операционные системы (Windows, части macOS)</li>
                <li>Браузеры (Chrome, Firefox)</li>
                <li>Высокочастотный трейдинг</li>
                <li>Встроенные системы и робототехника</li>
            </ul>

            <p><strong>Создатель:</strong> Бьёрн Страуструп | <strong>Год:</strong> 1983 | <strong>Стандарт:</strong> ISO C++23</p>
        """
    },
    "ml": {
        "title": "Машинное обучение",
        "category": "areas",
        "category_title": "Области разработки",
        "icon": "🤖",
        "short": "Нейросети, ML-алгоритмы, Data Science и AI",
        "image": None,
        "course_title": "Нейронные сети и компьютерное зрение",
        "course_url": "https://stepik.org/course/50352/promo",
        "text": """
            <p>Машинное обучение (ML) — раздел искусственного интеллекта, где системы учатся на данных без явного программирования. Лежит в основе ChatGPT, рекомендаций Netflix, распознавания лиц.</p>

            <h3>Виды обучения</h3>
            <ul>
                <li><strong>Supervised Learning</strong> — обучение с учителем. Есть размеченные данные. Задачи: классификация, регрессия</li>
                <li><strong>Unsupervised Learning</strong> — без учителя. Кластеризация, поиск аномалий</li>
                <li><strong>Reinforcement Learning</strong> — обучение с подкреплением. Агент учится через награды (AlphaGo, ChatGPT RLHF)</li>
                <li><strong>Self-supervised</strong> — LLM и BERT обучаются предсказывать части входных данных</li>
            </ul>

            <h3>Классические алгоритмы</h3>
            <ul>
                <li><strong>Linear / Logistic Regression</strong> — простые, интерпретируемые</li>
                <li><strong>Decision Trees / Random Forest</strong> — ансамбли деревьев</li>
                <li><strong>SVM</strong> — метод опорных векторов</li>
                <li><strong>K-Means</strong> — кластеризация</li>
                <li><strong>XGBoost / LightGBM</strong> — градиентный бустинг, лучшие для табличных данных</li>
            </ul>

            <h3>Нейросети</h3>
            <pre><code">import torch
import torch.nn as nn

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Dropout(0.2),
            nn.Linear(256, 10)
        )

    def forward(self, x):
        return self.layers(x)

model = SimpleNet()
optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)</code></pre>

            <h3>Современные архитектуры</h3>
            <ul>
                <li><strong>Transformer</strong> — архитектура «Attention is All You Need» (2017), основа GPT, BERT</li>
                <li><strong>CNN</strong> — свёрточные сети для изображений</li>
                <li><strong>RNN / LSTM</strong> — рекуррентные сети для последовательностей</li>
                <li><strong>Diffusion Models</strong> — генерация изображений (Stable Diffusion)</li>
            </ul>

            <h3>Инструменты</h3>
            <ul>
                <li><strong>PyTorch</strong> — исследовательский фреймворк от Meta</li>
                <li><strong>TensorFlow / Keras</strong> — от Google</li>
                <li><strong>scikit-learn</strong> — классические ML-алгоритмы</li>
                <li><strong>Hugging Face</strong> — модели и датасеты для NLP</li>
                <li><strong>Jupyter Notebook</strong> — интерактивная среда для исследований</li>
            </ul>
        """
    },
    "security": {
        "title": "Кибербезопасность",
        "category": "areas",
        "category_title": "Области разработки",
        "icon": "🔒",
        "short": "Защита приложений, веб-уязвимости, криптография и безопасная разработка",
        "image": None,
        "text": """
            <p>Кибербезопасность в разработке — это практики написания кода, защищённого от атак. Знание уязвимостей необходимо каждому разработчику.</p>

            <h3>Топ уязвимостей OWASP</h3>
            <ul>
                <li><strong>Injection (SQL/NoSQL/OS)</strong> — внедрение вредоносного кода через пользовательский ввод</li>
                <li><strong>Broken Authentication</strong> — слабые сессии, небезопасное хранение паролей</li>
                <li><strong>XSS (Cross-Site Scripting)</strong> — внедрение JS-кода в страницы</li>
                <li><strong>CSRF</strong> — подделка межсайтовых запросов</li>
                <li><strong>IDOR</strong> — небезопасный прямой доступ к объектам</li>
                <li><strong>Security Misconfiguration</strong> — неправильная настройка серверов</li>
            </ul>

            <h3>SQL-инъекция: пример и защита</h3>
            <pre><code># УЯЗВИМО:
query = f"SELECT * FROM users WHERE name='{name}'"

# БЕЗОПАСНО — параметризованный запрос:
cursor.execute("SELECT * FROM users WHERE name=%s", (name,))

# Атака: name = "'; DROP TABLE users; --"
# Параметризация полностью нейтрализует её</code></pre>

            <h3>Аутентификация и авторизация</h3>
            <pre><code">import bcrypt
import jwt

# Хеширование пароля
hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())

# JWT токен
token = jwt.encode(
    {"user_id": 1, "exp": datetime.utcnow() + timedelta(hours=1)},
    SECRET_KEY,
    algorithm="HS256"
)</code></pre>

            <h3>Криптография</h3>
            <ul>
                <li><strong>Симметричное шифрование</strong> — AES. Один ключ для шифрования и дешифровки</li>
                <li><strong>Асимметричное</strong> — RSA, ECC. Публичный и приватный ключ</li>
                <li><strong>Хеш-функции</strong> — SHA-256, bcrypt, Argon2 для паролей</li>
                <li><strong>TLS/HTTPS</strong> — шифрование транспортного уровня</li>
            </ul>

            <h3>Безопасная разработка</h3>
            <ul>
                <li>Принцип минимальных привилегий</li>
                <li>Валидация всего пользовательского ввода</li>
                <li>Регулярное обновление зависимостей (dependabot)</li>
                <li>SAST/DAST — статический и динамический анализ кода</li>
                <li>Secrets management — никаких паролей в коде и git-истории</li>
            </ul>
        """
    },
    "networking": {
        "title": "Компьютерные сети",
        "category": "cs",
        "category_title": "Информатика",
        "icon": "🌍",
        "short": "TCP/IP, DNS, HTTP/2, WebSocket — как работает интернет",
        "image": None,
        "text": """
            <p>Понимание сетей необходимо каждому разработчику — это основа интернета, API-интеграций и распределённых систем.</p>

            <h3>Модель OSI</h3>
            <pre><code">7 — Прикладной    HTTP, FTP, DNS, SMTP
6 — Представления  TLS/SSL, сжатие
5 — Сеансовый     Управление сессиями
4 — Транспортный  TCP, UDP, порты
3 — Сетевой       IP, маршрутизация
2 — Канальный     Ethernet, MAC-адреса
1 — Физический    Кабели, радиоволны</code></pre>

            <h3>TCP vs UDP</h3>
            <ul>
                <li><strong>TCP</strong> — надёжный, с подтверждением доставки, упорядоченный. Используется в HTTP, SSH, SMTP</li>
                <li><strong>UDP</strong> — быстрый, без гарантий. Видеозвонки, игры, DNS, стриминг</li>
            </ul>

            <h3>DNS</h3>
            <p>Система доменных имён — «телефонная книга» интернета.</p>
            <pre><code"># Запись типов DNS
A      example.com → 93.184.216.34     # IPv4
AAAA   example.com → 2606:2800:...     # IPv6
CNAME  www → example.com               # Псевдоним
MX     mail.example.com                # Почта
TXT    v=spf1 include:... ~all         # SPF/DKIM

# Запрос DNS
dig example.com A
nslookup example.com 8.8.8.8</code></pre>

            <h3>HTTP/1.1 vs HTTP/2 vs HTTP/3</h3>
            <ul>
                <li><strong>HTTP/1.1</strong> — один запрос за раз, text-based, keep-alive</li>
                <li><strong>HTTP/2</strong> — мультиплексирование, бинарный протокол, server push, сжатие заголовков</li>
                <li><strong>HTTP/3</strong> — на базе QUIC (UDP), устраняет head-of-line blocking</li>
            </ul>

            <h3>WebSocket</h3>
            <pre><code">// Двустороннее соединение в реальном времени
const ws = new WebSocket('wss://api.example.com/ws');

ws.onopen = () => ws.send(JSON.stringify({ type: 'subscribe' }));
ws.onmessage = (e) => console.log(JSON.parse(e.data));
ws.onerror = console.error;</code></pre>

            <h3>Инструменты</h3>
            <ul>
                <li><strong>curl / httpie</strong> — HTTP-запросы из командной строки</li>
                <li><strong>Wireshark</strong> — анализ сетевого трафика</li>
                <li><strong>traceroute / mtr</strong> — диагностика маршрутов</li>
                <li><strong>nmap</strong> — сканер портов и сетей</li>
            </ul>
        """
    },
    "typescript": {
        "title": "TypeScript",
        "category": "languages",
        "category_title": "Языки программирования",
        "icon": "🔷",
        "short": "Строго типизированный надъязык JavaScript от Microsoft",
        "image": None,
        "course_title": "TypeScript с нуля",
        "course_url": "https://stepik.org/course/152537/promo",
        "text": """
            <p>TypeScript — язык программирования, разработанный Microsoft как надстройка над JavaScript. Добавляет статическую типизацию, компилируясь в чистый JavaScript.</p>

            <h3>Ключевые возможности</h3>
            <ul>
                <li><strong>Статическая типизация</strong> — ошибки типов обнаруживаются на этапе компиляции</li>
                <li><strong>Интерфейсы и типы</strong> — мощная система описания форм объектов</li>
                <li><strong>Generics</strong> — обобщённое программирование</li>
                <li><strong>Декораторы</strong> — мета-программирование</li>
                <li><strong>Полная совместимость с JS</strong> — любой JS-код валиден в TS</li>
            </ul>

            <h3>Синтаксис</h3>
            <pre><code>interface User {
  id: number;
  name: string;
  email?: string; // необязательное поле
}

function identity&lt;T&gt;(arg: T): T {
  return arg;
}

type Status = 'active' | 'inactive' | 'pending';

function isString(val: unknown): val is string {
  return typeof val === 'string';
}</code></pre>

            <p><strong>Создатель:</strong> Microsoft | <strong>Год:</strong> 2012 | <strong>Текущая версия:</strong> TypeScript 5.x</p>
        """
    },
    "rust": {
        "title": "Rust",
        "category": "languages",
        "category_title": "Языки программирования",
        "icon": "⚙️",
        "short": "Системный язык с гарантиями безопасности памяти без сборщика мусора",
        "image": None,
        "course_title": "Rust: системное программирование",
        "course_url": "https://stepik.org/course/81289/promo",
        "text": """
            <p>Rust — системный язык программирования от Mozilla. Обеспечивает безопасность памяти без сборщика мусора благодаря уникальной системе владения (Ownership).</p>

            <h3>Система владения</h3>
            <ul>
                <li>Каждое значение имеет единственного владельца</li>
                <li>Когда владелец выходит из области видимости — память освобождается автоматически</li>
                <li><strong>Borrowing</strong> — временное заимствование без передачи владения</li>
                <li><strong>Lifetimes</strong> — явное управление временем жизни ссылок</li>
            </ul>

            <h3>Пример кода</h3>
            <pre><code>fn main() {
    let s1 = String::from("hello");
    let s2 = &s1; // borrowing
    println!("{} {}", s1, s2);

    enum Shape {
        Circle(f64),
        Rectangle(f64, f64),
    }

    let area = match Shape::Circle(3.14) {
        Shape::Circle(r) => std::f64::consts::PI * r * r,
        Shape::Rectangle(w, h) => w * h,
    };
    println!("Area: {}", area);
}</code></pre>

            <h3>Применение</h3>
            <ul>
                <li>Системное программирование и embedded</li>
                <li>WebAssembly</li>
                <li>Сетевые сервисы (Actix, Axum)</li>
                <li>Компоненты ОС (ядро Linux, Windows)</li>
            </ul>

            <p><strong>Создатель:</strong> Graydon Hoare / Mozilla | <strong>Год:</strong> 2010 | <strong>Особенность:</strong> 8 лет «любимый язык» по опросу Stack Overflow</p>
        """
    },
    "go": {
        "title": "Go (Golang)",
        "category": "languages",
        "category_title": "Языки программирования",
        "icon": "🐹",
        "short": "Компилируемый язык от Google для высоконагруженных серверных систем",
        "image": None,
        "course_title": "Golang для бэкенда",
        "course_url": "https://stepik.org/course/54403/promo",
        "text": """
            <p>Go — статически типизированный компилируемый язык, разработанный в Google в 2007 году. Сочетает производительность C с удобством Python, с акцентом на простоту и конкурентность.</p>

            <h3>Ключевые особенности</h3>
            <ul>
                <li><strong>Goroutines</strong> — легковесные потоки (тысячи на одном ядре)</li>
                <li><strong>Channels</strong> — безопасный обмен данными между goroutines</li>
                <li><strong>Быстрая компиляция</strong> — миллион строк за секунды</li>
                <li><strong>Статический бинарник</strong> — один файл без зависимостей</li>
            </ul>

            <h3>Пример кода</h3>
            <pre><code>package main

import (
    "fmt"
    "sync"
)

func worker(id int, wg *sync.WaitGroup) {
    defer wg.Done()
    fmt.Printf("Worker %d done\\n", id)
}

func main() {
    var wg sync.WaitGroup
    for i := 1; i <= 5; i++ {
        wg.Add(1)
        go worker(i, &wg)
    }
    wg.Wait()
}</code></pre>

            <p><strong>Создатели:</strong> Роб Пайк, Кен Томпсон | <strong>Год:</strong> 2009 | <strong>Используют:</strong> Google, Uber, Dropbox, Cloudflare</p>
        """
    },
    "java": {
        "title": "Java",
        "category": "languages",
        "category_title": "Языки программирования",
        "icon": "☕",
        "short": "Объектно-ориентированный язык с принципом «написано однажды — работает везде»",
        "image": None,
        "course_title": "Java для начинающих",
        "course_url": "https://stepik.org/course/187/promo",
        "text": """
            <p>Java — строго объектно-ориентированный язык, разработанный Sun Microsystems в 1995 году. Работает на виртуальной машине JVM, что обеспечивает кроссплатформенность.</p>

            <h3>Принципы JVM</h3>
            <ul>
                <li><strong>Write Once, Run Anywhere</strong> — байткод работает на любой платформе</li>
                <li><strong>Garbage Collection</strong> — автоматическое управление памятью</li>
                <li><strong>JIT-компиляция</strong> — горячий код компилируется в нативный</li>
                <li><strong>Многопоточность</strong> — Thread, ExecutorService, CompletableFuture</li>
            </ul>

            <h3>Современная Java (21+)</h3>
            <pre><code>record Point(int x, int y) {}

sealed interface Shape permits Circle, Rectangle {}
record Circle(double radius) implements Shape {}
record Rectangle(double w, double h) implements Shape {}

// Pattern matching
Object obj = "Hello";
if (obj instanceof String s &amp;&amp; s.length() > 3) {
    System.out.println(s.toUpperCase());
}</code></pre>

            <h3>Экосистема</h3>
            <ul>
                <li><strong>Spring Boot</strong> — корпоративные приложения и микросервисы</li>
                <li><strong>Maven / Gradle</strong> — системы сборки</li>
                <li><strong>JUnit 5</strong> — тестирование</li>
                <li><strong>Hibernate</strong> — ORM</li>
            </ul>

            <p><strong>Создатель:</strong> Джеймс Гослинг | <strong>Год:</strong> 1995 | <strong>Применение:</strong> Android, enterprise, backend</p>
        """
    },
    "docker": {
        "title": "Docker",
        "category": "tools",
        "category_title": "Инструменты",
        "icon": "🐋",
        "short": "Платформа контейнеризации для упаковки и запуска приложений",
        "image": None,
        "course_title": "Docker и контейнеризация",
        "course_url": "https://stepik.org/course/123300/promo",
        "text": """
            <p>Docker — платформа для разработки и запуска приложений в контейнерах. Контейнер включает всё необходимое: код, зависимости, конфигурацию — и работает одинаково в любой среде.</p>

            <h3>Ключевые концепции</h3>
            <ul>
                <li><strong>Image (образ)</strong> — неизменяемый шаблон для создания контейнера</li>
                <li><strong>Container (контейнер)</strong> — запущенный экземпляр образа</li>
                <li><strong>Dockerfile</strong> — инструкции по сборке образа</li>
                <li><strong>Registry</strong> — хранилище образов (Docker Hub, GHCR)</li>
                <li><strong>Volume</strong> — постоянное хранилище данных</li>
            </ul>

            <h3>Dockerfile</h3>
            <pre><code>FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

FROM node:20-alpine AS production
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
EXPOSE 3000
CMD ["node", "dist/main.js"]</code></pre>

            <h3>Docker Compose</h3>
            <pre><code>version: '3.9'
services:
  web:
    build: .
    ports: ["3000:3000"]
    depends_on: [db]
  db:
    image: postgres:16
    environment:
      POSTGRES_PASSWORD: secret
    volumes:
      - pgdata:/var/lib/postgresql/data
volumes:
  pgdata:</code></pre>

            <p><strong>Создатель:</strong> Solomon Hykes | <strong>Год:</strong> 2013 | <strong>Альтернативы:</strong> Podman, containerd</p>
        """
    },
    "vscode": {
        "title": "VS Code",
        "category": "tools",
        "category_title": "Инструменты",
        "icon": "📝",
        "short": "Самый популярный редактор кода от Microsoft с тысячами расширений",
        "image": None,
        "course_title": "VS Code: полное руководство",
        "course_url": "https://www.youtube.com/watch?v=MFBN1iGNiMQ",
        "text": """
            <p>Visual Studio Code — бесплатный редактор кода с открытым исходным кодом от Microsoft. По данным Stack Overflow, используется более чем 70% разработчиков.</p>

            <h3>Встроенные возможности</h3>
            <ul>
                <li><strong>IntelliSense</strong> — умное автодополнение с поддержкой типов</li>
                <li><strong>Встроенный отладчик</strong> — breakpoints, watch, call stack</li>
                <li><strong>Интеграция с Git</strong> — diff, staging, commits</li>
                <li><strong>Встроенный терминал</strong> — не нужно переключаться между окнами</li>
                <li><strong>Remote Development</strong> — разработка на удалённых машинах и в контейнерах</li>
            </ul>

            <h3>Горячие клавиши</h3>
            <pre><code>Ctrl+P          — быстрый поиск файлов
Ctrl+Shift+P    — командная палитра
Ctrl+`          — открыть терминал
Alt+Click       — мультикурсор
Ctrl+D          — выделить следующее вхождение
F2              — переименовать символ
Ctrl+Shift+F    — поиск по всему проекту</code></pre>

            <h3>Расширения</h3>
            <ul>
                <li><strong>Prettier</strong> — форматирование кода</li>
                <li><strong>ESLint / Pylint</strong> — линтеры</li>
                <li><strong>GitLens</strong> — расширенная история Git</li>
                <li><strong>GitHub Copilot</strong> — AI-автодополнение</li>
            </ul>

            <p><strong>Создатель:</strong> Microsoft | <strong>Год:</strong> 2015 | <strong>Лицензия:</strong> MIT</p>
        """
    },
    "patterns": {
        "title": "Паттерны проектирования",
        "category": "cs",
        "category_title": "Информатика",
        "icon": "🎨",
        "short": "Классические решения типичных задач проектирования программных систем",
        "image": None,
        "course_title": "Паттерны проектирования",
        "course_url": "https://stepik.org/course/89836/promo",
        "text": """
            <p>Паттерны проектирования — проверенные решения часто встречающихся задач. Введены книгой «Gang of Four» (1994). Делятся на три категории.</p>

            <h3>Порождающие (Creational)</h3>
            <ul>
                <li><strong>Singleton</strong> — единственный экземпляр класса</li>
                <li><strong>Factory Method</strong> — создание объектов через метод-фабрику</li>
                <li><strong>Builder</strong> — пошаговое создание сложных объектов</li>
                <li><strong>Prototype</strong> — клонирование объектов</li>
            </ul>

            <h3>Структурные (Structural)</h3>
            <ul>
                <li><strong>Adapter</strong> — совместимость несовместимых интерфейсов</li>
                <li><strong>Decorator</strong> — добавление поведения без изменения класса</li>
                <li><strong>Facade</strong> — упрощённый интерфейс к сложной подсистеме</li>
                <li><strong>Proxy</strong> — суррогат для контроля доступа к объекту</li>
            </ul>

            <h3>Поведенческие (Behavioral)</h3>
            <ul>
                <li><strong>Observer</strong> — подписка на события объекта</li>
                <li><strong>Strategy</strong> — взаимозаменяемые алгоритмы</li>
                <li><strong>Command</strong> — инкапсуляция операции как объекта</li>
                <li><strong>State</strong> — изменение поведения при смене состояния</li>
            </ul>

            <h3>Пример: Observer на Python</h3>
            <pre><code>class EventEmitter:
    def __init__(self):
        self._listeners = {}

    def on(self, event, callback):
        self._listeners.setdefault(event, []).append(callback)

    def emit(self, event, *args):
        for cb in self._listeners.get(event, []):
            cb(*args)

emitter = EventEmitter()
emitter.on('data', lambda x: print(f"Получено: {x}"))
emitter.emit('data', 42)</code></pre>
        """
    },
    "testing": {
        "title": "Тестирование ПО",
        "category": "cs",
        "category_title": "Информатика",
        "icon": "✅",
        "short": "Методологии и инструменты тестирования: unit, integration, e2e, TDD",
        "image": None,
        "course_title": "Тестирование ПО с нуля",
        "course_url": "https://stepik.org/course/120491/promo",
        "text": """
            <p>Тестирование — неотъемлемая часть профессиональной разработки. Код с тестами легче рефакторить, содержит меньше регрессий и документирует поведение системы.</p>

            <h3>Пирамида тестирования</h3>
            <ul>
                <li><strong>Unit-тесты</strong> — тестируют отдельные функции/классы. Быстрые, их много (70%)</li>
                <li><strong>Integration-тесты</strong> — тестируют взаимодействие компонентов (20%)</li>
                <li><strong>E2E-тесты</strong> — тестируют весь путь пользователя (10%)</li>
            </ul>

            <h3>TDD — Test-Driven Development</h3>
            <p>Цикл <strong>Red → Green → Refactor</strong>:</p>
            <ul>
                <li><strong>Red</strong> — напишите тест, который падает</li>
                <li><strong>Green</strong> — напишите минимальный код для прохождения теста</li>
                <li><strong>Refactor</strong> — улучшите код, не ломая тесты</li>
            </ul>

            <h3>Пример на pytest</h3>
            <pre><code>import pytest

def add(a, b):
    return a + b

@pytest.mark.parametrize("a,b,expected", [
    (1, 2, 3),
    (0, 0, 0),
    (-1, 1, 0),
])
def test_add(a, b, expected):
    assert add(a, b) == expected</code></pre>

            <h3>Инструменты по языкам</h3>
            <ul>
                <li><strong>Python:</strong> pytest, unittest, coverage.py</li>
                <li><strong>JavaScript:</strong> Jest, Vitest, Cypress, Playwright</li>
                <li><strong>Java:</strong> JUnit 5, Mockito</li>
                <li><strong>Go:</strong> testing (встроенный), testify</li>
            </ul>
        """
    },
    "mobile": {
        "title": "Мобильная разработка",
        "category": "areas",
        "category_title": "Области разработки",
        "icon": "📱",
        "short": "iOS, Android и кроссплатформенная разработка мобильных приложений",
        "image": None,
        "course_title": "Мобильная разработка на Flutter",
        "course_url": "https://stepik.org/course/119/promo",
        "text": """
            <p>Мобильная разработка охватывает создание приложений для смартфонов и планшетов. Существует нативный и кроссплатформенный подходы.</p>

            <h3>Нативная разработка</h3>
            <ul>
                <li><strong>iOS</strong> — Swift / Objective-C, Xcode, App Store</li>
                <li><strong>Android</strong> — Kotlin / Java, Android Studio, Google Play</li>
                <li>Лучшая производительность и доступ ко всем возможностям платформы</li>
                <li>Требует двух отдельных кодовых баз</li>
            </ul>

            <h3>Кроссплатформенные решения</h3>
            <ul>
                <li><strong>React Native</strong> — JavaScript/TypeScript, компилируется в нативные компоненты</li>
                <li><strong>Flutter</strong> — Dart, собственный движок рендеринга</li>
                <li><strong>Xamarin/.NET MAUI</strong> — C#, экосистема Microsoft</li>
            </ul>

            <h3>Flutter пример</h3>
            <pre><code>class Counter extends StatefulWidget {
  @override
  _CounterState createState() => _CounterState();
}

class _CounterState extends State&lt;Counter&gt; {
  int _count = 0;
  @override
  Widget build(BuildContext context) =&gt; Column(
    children: [
      Text('Count: $_count'),
      ElevatedButton(
        onPressed: () =&gt; setState(() =&gt; _count++),
        child: Text('Increment'),
      ),
    ],
  );
}</code></pre>

            <h3>Ключевые концепции</h3>
            <ul>
                <li><strong>State management</strong> — Redux, MobX, Riverpod, BLoC</li>
                <li><strong>Push notifications</strong> — FCM (Firebase), APNs (Apple)</li>
                <li><strong>Deep links</strong> — открытие приложения по URL</li>
            </ul>
        """
    },
    "cloud": {
        "title": "Облачные вычисления",
        "category": "areas",
        "category_title": "Области разработки",
        "icon": "☁️",
        "short": "AWS, GCP, Azure: инфраструктура, сервисы и модели облачных вычислений",
        "image": None,
        "course_title": "Облачные вычисления AWS",
        "course_url": "https://stepik.org/course/100837/promo",
        "text": """
            <p>Облачные вычисления — предоставление вычислительных ресурсов через интернет по требованию. Позволяют строить масштабируемые системы без физических серверов.</p>

            <h3>Модели обслуживания</h3>
            <ul>
                <li><strong>IaaS</strong> — виртуальные машины, сети, хранилище (EC2, GCE)</li>
                <li><strong>PaaS</strong> — платформа для развёртывания приложений (Heroku, App Engine)</li>
                <li><strong>SaaS</strong> — готовое ПО через браузер (Gmail, Salesforce)</li>
                <li><strong>FaaS</strong> — serverless функции (Lambda, Cloud Functions)</li>
            </ul>

            <h3>Основные провайдеры</h3>
            <ul>
                <li><strong>AWS</strong> — лидер рынка, 200+ сервисов</li>
                <li><strong>Google Cloud</strong> — силён в ML/AI, BigQuery, Kubernetes</li>
                <li><strong>Azure</strong> — лучшая интеграция с продуктами Microsoft</li>
            </ul>

            <h3>Ключевые AWS-сервисы</h3>
            <pre><code>EC2          — виртуальные серверы
S3           — объектное хранилище
RDS          — управляемые БД
Lambda       — serverless функции
CloudFront   — CDN
ECS / EKS    — контейнеры и Kubernetes
SQS / SNS    — очереди сообщений</code></pre>
        """
    },
    "api_design": {
        "title": "Проектирование API",
        "category": "areas",
        "category_title": "Области разработки",
        "icon": "🔌",
        "short": "REST, GraphQL, gRPC — подходы к проектированию интерфейсов взаимодействия систем",
        "image": None,
        "text": """
            <p>API (Application Programming Interface) — интерфейс взаимодействия программных компонентов. Хорошо спроектированный API — основа качественной архитектуры.</p>

            <h3>REST API</h3>
            <ul>
                <li><strong>Ресурсы</strong> — существительные в URL: /users, /orders/42</li>
                <li><strong>HTTP-методы</strong> — GET, POST, PUT/PATCH, DELETE</li>
                <li><strong>Stateless</strong> — каждый запрос самодостаточен</li>
                <li><strong>Коды ответов</strong> — 200 OK, 201 Created, 400, 401, 404, 500</li>
            </ul>

            <h3>Типичные эндпоинты</h3>
            <pre><code>GET    /api/v1/users       — список
POST   /api/v1/users       — создать
GET    /api/v1/users/{id}  — получить
PUT    /api/v1/users/{id}  — обновить
DELETE /api/v1/users/{id}  — удалить</code></pre>

            <h3>GraphQL</h3>
            <pre><code>query {
  user(id: "1") {
    name
    posts(last: 3) { title createdAt }
  }
}</code></pre>

            <h3>gRPC</h3>
            <ul>
                <li>Protocol Buffers — компактнее JSON</li>
                <li>Строгая типизация через .proto файлы</li>
                <li>Двунаправленный стриминг</li>
                <li>Генерация клиентов для любого языка</li>
            </ul>

            <h3>Best Practices</h3>
            <ul>
                <li>Версионирование: /api/v1/</li>
                <li>Пагинация: cursor-based или offset</li>
                <li>Rate limiting — защита от злоупотреблений</li>
                <li>OpenAPI/Swagger — документация и генерация клиентов</li>
            </ul>
        """
    },
    "concurrency": {
        "title": "Конкурентность и параллелизм",
        "category": "cs",
        "category_title": "Информатика",
        "icon": "⚡",
        "short": "Потоки, процессы, асинхронность и модели конкурентного выполнения",
        "image": None,
        "course_title": "Параллельное программирование",
        "course_url": "https://stepik.org/course/149374/promo",
        "text": """
            <p>Конкурентность и параллелизм — способность программы выполнять несколько задач одновременно. Критически важны для производительных серверных приложений.</p>

            <h3>Ключевые понятия</h3>
            <ul>
                <li><strong>Конкурентность</strong> — задачи выполняются в перекрывающиеся промежутки времени</li>
                <li><strong>Параллелизм</strong> — задачи выполняются одновременно на разных ядрах CPU</li>
            </ul>

            <h3>Модели выполнения</h3>
            <ul>
                <li><strong>Многопоточность</strong> — OS threads, разделяют память (риск гонок)</li>
                <li><strong>Многопроцессность</strong> — изолированная память</li>
                <li><strong>Async/Await</strong> — кооперативная многозадачность в одном потоке</li>
                <li><strong>Акторы</strong> — общение через сообщения (Erlang, Akka)</li>
                <li><strong>CSP</strong> — Goroutines + Channels в Go</li>
            </ul>

            <h3>Python asyncio</h3>
            <pre><code>import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.json()

async def main():
    urls = ['https://api1.com', 'https://api2.com']
    async with aiohttp.ClientSession() as session:
        results = await asyncio.gather(
            *[fetch(session, url) for url in urls]
        )
    return results</code></pre>

            <h3>Проблемы и решения</h3>
            <ul>
                <li><strong>Race condition</strong> — мьютексы, атомарные операции</li>
                <li><strong>Deadlock</strong> — правильный порядок захвата блокировок</li>
                <li><strong>GIL в Python</strong> — обходится через multiprocessing</li>
            </ul>
        """
    },

    "kotlin": {
        "title": "Kotlin",
        "category": "languages",
        "category_title": "Языки программирования",
        "icon": "🟣",
        "short": "Современный JVM-язык от JetBrains, официальный язык Android-разработки",
        "image": None,
        "course_title": "Kotlin для начинающих",
        "course_url": "https://stepik.org/course/5448/promo",
        "text": """
            <p>Kotlin — статически типизированный язык программирования, разработанный компанией JetBrains и выпущенный в 2016 году. В 2017 году Google объявил его <strong>официальным языком Android-разработки</strong>. Сегодня Kotlin используется и на бэкенде (Ktor, Spring), и в мультиплатформенных проектах.</p>

            <h3>Почему Kotlin лучше Java?</h3>
            <ul>
                <li><strong>Null Safety</strong> — компилятор запрещает передавать null туда, где его не ждут. Тип <code>String</code> гарантированно не null, <code>String?</code> — может быть null. Устраняет целый класс ошибок NullPointerException</li>
                <li><strong>Data classes</strong> — одна строка заменяет десятки строк Java-бойлерплейта: equals, hashCode, toString, copy генерируются автоматически</li>
                <li><strong>Extension functions</strong> — можно добавлять методы к существующим классам без наследования</li>
                <li><strong>Smart casts</strong> — после проверки <code>if (x is String)</code> компилятор сам кастует переменную, не нужно явного приведения типов</li>
                <li><strong>Coroutines</strong> — встроенная поддержка асинхронности без callback hell</li>
            </ul>

            <h3>Ключевые концепции</h3>
            <pre><code>// Data class — компилятор генерирует equals/hashCode/toString
data class User(val name: String, val age: Int)

// Null safety
fun greet(name: String?) {
    val safe = name ?: "Аноним"  // Elvis-оператор
    println("Привет, $safe!")
}

// Extension function
fun String.isPalindrome() = this == this.reversed()
println("racecar".isPalindrome())  // true

// Coroutines
suspend fun fetchData(): String {
    delay(1000)  // Не блокирует поток!
    return "Данные получены"
}</code></pre>

            <h3>Kotlin Multiplatform</h3>
            <p>KMP позволяет писать бизнес-логику один раз и использовать её на Android, iOS, десктопе и в браузере. Крупные компании вроде Netflix уже используют KMP в продакшене.</p>

            <h3>Корутины vs Threads</h3>
            <p>Одна корутина потребляет около 1 КБ памяти против 1 МБ для системного потока. Приложение может запустить миллион корутин без проблем. Они работают через <em>suspend functions</em> — функции, которые умеют приостанавливаться без блокировки потока.</p>

            <p><strong>Создатель:</strong> JetBrains | <strong>Год:</strong> 2016 | <strong>Платформы:</strong> JVM, Android, Native, JS, WASM</p>
        """
    },
    "sql": {
        "title": "SQL",
        "category": "databases",
        "category_title": "Базы данных",
        "icon": "🗄️",
        "short": "Язык структурированных запросов для работы с реляционными базами данных",
        "image": None,
        "course_title": "SQL для начинающих",
        "course_url": "https://stepik.org/course/51562/promo",
        "text": """
            <p>SQL (Structured Query Language) — декларативный язык для управления реляционными базами данных. Придуман в IBM в 1974 году на основе реляционной алгебры Эдгара Кодда. По данным Stack Overflow, SQL входит в топ-5 востребованных технологий уже более 10 лет подряд.</p>

            <h3>Базовые операции (CRUD)</h3>
            <pre><code>-- Создание таблицы
CREATE TABLE users (
    id        SERIAL PRIMARY KEY,
    name      VARCHAR(100) NOT NULL,
    email     VARCHAR(255) UNIQUE NOT NULL,
    age       INTEGER CHECK (age &gt;= 0),
    created_at TIMESTAMP DEFAULT NOW()
);

-- Вставка
INSERT INTO users (name, email, age) VALUES ('Алекс', 'alex@mail.ru', 25);

-- Чтение с условием
SELECT name, email FROM users WHERE age &gt; 18 ORDER BY name LIMIT 10;

-- Обновление
UPDATE users SET age = 26 WHERE email = 'alex@mail.ru';

-- Удаление
DELETE FROM users WHERE id = 42;</code></pre>

            <h3>JOIN — объединение таблиц</h3>
            <pre><code>-- INNER JOIN: только совпадения в обеих таблицах
SELECT u.name, o.product, o.price
FROM users u
INNER JOIN orders o ON u.id = o.user_id;

-- LEFT JOIN: все пользователи + их заказы (или NULL)
SELECT u.name, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id, u.name;</code></pre>

            <h3>Агрегация и группировка</h3>
            <pre><code>-- Топ-5 категорий по выручке
SELECT
    category,
    COUNT(*)    as total_orders,
    SUM(price)  as revenue,
    AVG(price)  as avg_price
FROM orders
WHERE created_at &gt;= '2024-01-01'
GROUP BY category
HAVING SUM(price) &gt; 10000
ORDER BY revenue DESC
LIMIT 5;</code></pre>

            <h3>Индексы — секрет быстрых запросов</h3>
            <p>Без индекса база сканирует каждую строку (Full Table Scan). С индексом — находит нужное за O(log n). Платить приходится местом на диске и скоростью вставки.</p>
            <pre><code>CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_orders_user_date ON orders(user_id, created_at DESC);

-- Проверяем план запроса
EXPLAIN ANALYZE SELECT * FROM users WHERE email = 'alex@mail.ru';</code></pre>

            <h3>Популярные СУБД</h3>
            <ul>
                <li><strong>PostgreSQL</strong> — самая мощная OpenSource СУБД: JSON, массивы, геоданные, полнотекстовый поиск</li>
                <li><strong>MySQL / MariaDB</strong> — классика веба, используется в большинстве сайтов на WordPress</li>
                <li><strong>SQLite</strong> — файловая БД без сервера, встроена в Android, iOS, браузеры</li>
                <li><strong>MS SQL Server / Oracle</strong> — корпоративный сегмент</li>
            </ul>

            <p><strong>Стандарт:</strong> ISO/IEC 9075 | <strong>Год:</strong> 1974 | <strong>Парадигма:</strong> декларативная</p>
        """
    },
    "redis": {
        "title": "Redis",
        "category": "databases",
        "category_title": "Базы данных",
        "icon": "🔴",
        "short": "In-memory хранилище: кэш, очереди, сессии — быстрее любой реляционной БД",
        "image": None,
        "course_title": "Redis полный курс",
        "course_url": "https://stepik.org/course/122441/promo",
        "text": """
            <p>Redis (Remote Dictionary Server) — хранилище данных в оперативной памяти с открытым исходным кодом. Создан Сальваторе Санфилиппо в 2009 году. Работает в 10–100 раз быстрее традиционных баз данных. Используется в Instagram, Twitter, GitHub, Stack Overflow.</p>

            <h3>Структуры данных Redis</h3>
            <ul>
                <li><strong>String</strong> — простое значение, счётчики, JSON</li>
                <li><strong>List</strong> — двусвязный список, очереди задач</li>
                <li><strong>Hash</strong> — объект с полями, профиль пользователя</li>
                <li><strong>Set</strong> — уникальные значения, теги, пересечения</li>
                <li><strong>Sorted Set</strong> — элементы с оценкой, рейтинги и лидерборды</li>
                <li><strong>Stream</strong> — лог событий, альтернатива Kafka</li>
            </ul>

            <h3>Примеры использования</h3>
            <pre><code># Кэширование с TTL (время жизни 1 час)
SET user:1:profile '{"name":"Алекс"}' EX 3600
GET user:1:profile

# Счётчик просмотров (атомарно)
INCR page:views:article:42

# Очередь задач
LPUSH tasks '{"type":"send_email","to":"user@mail.ru"}'
BRPOP tasks 0  # Блокирующее извлечение

# Лидерборд игры
ZADD leaderboard 9500 "Алекс"
ZADD leaderboard 8200 "Мария"
ZREVRANGE leaderboard 0 9 WITHSCORES  # Топ-10</code></pre>

            <h3>Персистентность</h3>
            <ul>
                <li><strong>RDB (снэпшоты)</strong> — полный слепок данных каждые N минут. Быстрое восстановление</li>
                <li><strong>AOF (Append-Only File)</strong> — логирует каждую команду. Никаких потерь, но файл растёт</li>
            </ul>

            <h3>Redis как очередь задач</h3>
            <p>С библиотеками <strong>Celery (Python)</strong> или <strong>BullMQ (Node.js)</strong> Redis становится мощным брокером задач. Воркеры берут задачи из очереди, выполняют, отмечают результат.</p>

            <p><strong>Создатель:</strong> Сальваторе Санфилиппо | <strong>Год:</strong> 2009 | <strong>Скорость:</strong> 100 000+ операций/сек</p>
        """
    },
    "react": {
        "title": "React",
        "category": "areas",
        "category_title": "Области разработки",
        "icon": "⚛️",
        "short": "Библиотека для построения пользовательских интерфейсов от Meta",
        "image": None,
        "course_title": "React — полный курс",
        "course_url": "https://stepik.org/course/173374/promo",
        "text": """
            <p>React — JavaScript-библиотека для создания пользовательских интерфейсов, разработанная в Facebook и открытая в 2013 году. Сегодня React — самый популярный UI-фреймворк в мире: его используют Meta, Netflix, Airbnb, Discord, WhatsApp Web.</p>

            <h3>Компонентный подход</h3>
            <p>Интерфейс разбивается на независимые компоненты. Каждый компонент — функция, принимающая данные (props) и возвращающая JSX.</p>
            <pre><code>function UserCard({ name, avatar, role }) {
  return (
    &lt;div className="card"&gt;
      &lt;img src={avatar} alt={name} /&gt;
      &lt;h2&gt;{name}&lt;/h2&gt;
      &lt;p&gt;{role}&lt;/p&gt;
    &lt;/div&gt;
  );
}

&lt;UserCard name="Алекс" avatar="/alex.jpg" role="Frontend Dev" /&gt;</code></pre>

            <h3>Хуки — сердце современного React</h3>
            <pre><code>import { useState, useEffect } from 'react';

function Counter() {
  const [count, setCount] = useState(0);

  useEffect(() => {
    document.title = `Счётчик: ${count}`;
  }, [count]);

  return (
    &lt;button onClick={() =&gt; setCount(c =&gt; c + 1)}&gt;
      Нажато: {count}
    &lt;/button&gt;
  );
}</code></pre>

            <h3>Virtual DOM</h3>
            <p>React хранит виртуальную копию DOM в памяти. При изменении состояния сравнивает новый Virtual DOM со старым, находит минимальный набор изменений и применяет только их. Это в разы быстрее прямой работы с DOM.</p>

            <h3>Экосистема</h3>
            <ul>
                <li><strong>Next.js</strong> — фулстек-фреймворк: SSR, роутинг, API routes</li>
                <li><strong>React Native</strong> — мобильные приложения для iOS и Android</li>
                <li><strong>Zustand / Redux</strong> — управление глобальным состоянием</li>
                <li><strong>React Query / SWR</strong> — загрузка и кэширование данных с сервера</li>
                <li><strong>Vite</strong> — молниеносная сборка проектов</li>
            </ul>

            <p><strong>Создатель:</strong> Jordan Walke (Meta) | <strong>Год:</strong> 2013 | <strong>Версия:</strong> React 19</p>
        """
    },
    "data_structures": {
        "title": "Структуры данных",
        "category": "cs",
        "category_title": "Информатика",
        "icon": "🌳",
        "short": "Массивы, списки, деревья, графы — фундамент эффективных программ",
        "image": None,
        "course_title": "Алгоритмы и структуры данных",
        "course_url": "https://stepik.org/course/1547/promo",
        "text": """
            <p>Структура данных — способ организации и хранения данных в памяти компьютера. Выбор правильной структуры — это 80% успеха любого алгоритма. Понимание структур данных — обязательное требование на технических интервью в Google, Яндекс, VK.</p>

            <h3>Массив (Array)</h3>
            <p>Элементы хранятся последовательно в памяти. Доступ по индексу за O(1). Вставка/удаление в середину — O(n), потому что нужно сдвигать элементы.</p>

            <h3>Хэш-таблица (Hash Map)</h3>
            <p>Доступ, вставка и удаление за O(1) в среднем. Ключ проходит через хэш-функцию, результат — индекс в массиве.</p>
            <pre><code># Python dict — это хэш-таблица
phone_book = {}
phone_book["Алекс"] = "+7-900-123-45-67"  # O(1)
print(phone_book["Алекс"])                 # O(1)</code></pre>

            <h3>Стек (Stack) и Очередь (Queue)</h3>
            <ul>
                <li><strong>Стек — LIFO</strong> (Last In, First Out): как стопка тарелок. Применение: отмена действий, рекурсия, скобочные выражения</li>
                <li><strong>Очередь — FIFO</strong> (First In, First Out): как очередь в кассе. Применение: BFS-обход графа, очереди задач</li>
            </ul>

            <h3>Дерево (Tree)</h3>
            <ul>
                <li><strong>BST (Бинарное дерево поиска)</strong> — левее меньше, правее больше. Поиск/вставка за O(log n)</li>
                <li><strong>Heap (Куча)</strong> — родитель всегда больше детей. Основа Priority Queue</li>
                <li><strong>Trie (Префиксное дерево)</strong> — автодополнение и поиск слов</li>
            </ul>

            <h3>Граф (Graph)</h3>
            <p>Набор вершин и рёбер. Социальные сети, карты городов, зависимости пакетов — всё это графы. Обходы: BFS (в ширину) и DFS (в глубину) — основа большинства алгоритмов на графах.</p>

            <h3>Шпаргалка по сложности</h3>
            <ul>
                <li>Массив: доступ O(1), поиск O(n), вставка O(n)</li>
                <li>Хэш-таблица: O(1) для всего в среднем</li>
                <li>BST сбалансированное: O(log n) для всего</li>
                <li>Heap: O(log n) вставка, O(1) получение min/max</li>
            </ul>
        """
    },
    "regex": {
        "title": "Регулярные выражения",
        "category": "tools",
        "category_title": "Инструменты",
        "icon": "🔍",
        "short": "Мощный мини-язык для поиска и замены текста по шаблонам",
        "image": None,
        "course_title": "Регулярные выражения",
        "course_url": "https://stepik.org/course/107335/promo",
        "text": """
            <p>Регулярные выражения (regex) — формальный язык для поиска и замены текста по паттернам. Изобретены математиком Стивеном Клини в 1956 году. Незаменимы для парсинга, валидации данных, обработки логов.</p>

            <h3>Базовые символы</h3>
            <ul>
                <li><code>.</code> — любой символ кроме переноса строки</li>
                <li><code>\\d</code> — цифра [0-9], <code>\\D</code> — не цифра</li>
                <li><code>\\w</code> — буква/цифра/underscore</li>
                <li><code>\\s</code> — пробельный символ</li>
                <li><code>^</code> — начало строки, <code>$</code> — конец строки</li>
                <li><code>[abc]</code> — один из символов, <code>[^abc]</code> — любой кроме</li>
            </ul>

            <h3>Квантификаторы</h3>
            <ul>
                <li><code>*</code> — ноль или более, <code>+</code> — один или более</li>
                <li><code>?</code> — ноль или один (необязательный)</li>
                <li><code>{2,5}</code> — от 2 до 5 раз</li>
                <li><code>*?</code> — ленивый (минимальное совпадение)</li>
            </ul>

            <h3>Практические примеры на Python</h3>
            <pre><code>import re

# Валидация email
pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$'
is_valid = bool(re.match(pattern, "user@example.com"))

# Маскировка карточных данных
text = "Карта: 4532 1234 5678 9012"
masked = re.sub(r'(\\d{4} ){3}', '#### #### #### ', text)
# Результат: "Карта: #### #### #### 9012"

# Группы — извлечь части URL
url = "https://example.com:8080/path"
match = re.search(r'(https?)://([^/:]+)(?::(\\d+))?', url)
protocol, host, port = match.groups()  # https, example.com, 8080</code></pre>

            <h3>Lookahead и Lookbehind</h3>
            <pre><code># Lookahead: числа перед знаком $
re.findall(r'\\d+(?=\\$)', "100$ и 200€")  # ['100']

# Lookbehind: числа после символа #
re.findall(r'(?&lt;=#)\\d+', "#42 #100")  # ['42', '100']</code></pre>

            <p><strong>Совет:</strong> Тестируйте regex на <strong>regex101.com</strong> — там интерактивное объяснение каждого символа в реальном времени.</p>
        """
    },
    "clean_code": {
        "title": "Чистый код",
        "category": "cs",
        "category_title": "Информатика",
        "icon": "✨",
        "short": "Принципы написания кода, который легко читать, понимать и поддерживать",
        "image": None,
        "course_title": "Принципы написания чистого кода",
        "course_url": "https://stepik.org/course/175878/promo",
        "text": """
            <p>Чистый код — код, который легко читается, понимается и изменяется. Концепцию популяризировал Роберт Мартин (Uncle Bob) в книге «Clean Code» (2008). Главный принцип: <em>«Код пишется один раз, а читается десятки раз»</em>.</p>

            <h3>Именование — важнее, чем кажется</h3>
            <pre><code># Плохо
def calc(a, b, fl):
    if fl:
        return a * b * 0.9
    return a * b

# Хорошо
DISCOUNT_RATE = 0.9

def calculate_order_total(price: float, quantity: int, apply_discount: bool) -> float:
    total = price * quantity
    return total * DISCOUNT_RATE if apply_discount else total</code></pre>

            <h3>Функции — одна ответственность</h3>
            <p>Принцип SRP: функция должна делать одну вещь. Если функцию сложно назвать — значит, она делает слишком много.</p>
            <pre><code># Плохо — функция делает 3 вещи
def process_user(data):
    validate(data)
    db.save(data)
    send_email(data['email'])

# Хорошо — разбиваем на отдельные функции
def register_user(data):
    validate_user(data)
    save_user(data)
    send_welcome_email(data['email'])</code></pre>

            <h3>Комментарии — когда нужны</h3>
            <p>Хороший код документирует себя сам. Комментарий нужен, когда код объясняет <em>как</em>, но не объясняет <em>почему</em>.</p>
            <pre><code># Плохо — очевидный комментарий
i = i + 1  # Увеличиваем i на 1

# Хорошо — объясняем неочевидное бизнес-правило
import math
# По бизнес-правилам округление всегда в большую сторону
units = math.ceil(total / unit_size)</code></pre>

            <h3>Принципы SOLID</h3>
            <ul>
                <li><strong>S</strong>ingle Responsibility — один класс, одна причина изменяться</li>
                <li><strong>O</strong>pen/Closed — открыт для расширения, закрыт для изменения</li>
                <li><strong>L</strong>iskov Substitution — подкласс можно заменить базовым классом</li>
                <li><strong>I</strong>nterface Segregation — много маленьких интерфейсов лучше одного большого</li>
                <li><strong>D</strong>ependency Inversion — зависеть от абстракций, не от конкреций</li>
            </ul>

            <h3>Правило бойскаута</h3>
            <p><em>«Оставь лагерь чище, чем нашёл»</em>. Каждый раз открывая файл — улучшай его чуть-чуть: переименуй переменную, разбей функцию, удали дубликат. Маленькие улучшения накапливаются и меняют весь проект.</p>
        """
    },
    "graphql": {
        "title": "GraphQL",
        "category": "areas",
        "category_title": "Области разработки",
        "icon": "🔷",
        "short": "Язык запросов для API: клиент сам выбирает, какие данные получить",
        "image": None,
        "course_title": "GraphQL для разработчиков",
        "course_url": "https://stepik.org/course/155504/promo",
        "text": """
            <p>GraphQL — язык запросов для API, разработанный Facebook в 2012 году и открытый в 2015-м. Главная идея: <strong>клиент сам описывает, что именно ему нужно</strong>, и получает ровно эти данные.</p>

            <h3>Проблема REST, которую решает GraphQL</h3>
            <ul>
                <li><strong>Over-fetching</strong> — API возвращает лишние данные. Нужно только имя, а приходят 30 полей</li>
                <li><strong>Under-fetching</strong> — для одного экрана нужно 3–5 запросов к разным эндпоинтам</li>
            </ul>
            <p>GraphQL решает обе проблемы: один запрос, только нужные поля.</p>

            <h3>Запрос и ответ</h3>
            <pre><code>query {
  user(id: "1") {
    name
    email
    posts(last: 3) {
      title
      comments { count }
    }
  }
}</code></pre>

            <h3>Типы операций</h3>
            <ul>
                <li><strong>Query</strong> — чтение данных (как GET в REST)</li>
                <li><strong>Mutation</strong> — изменение данных (POST/PUT/DELETE)</li>
                <li><strong>Subscription</strong> — события в реальном времени через WebSocket</li>
            </ul>

            <h3>Schema — контракт между клиентом и сервером</h3>
            <pre><code>type User {
  id: ID!
  name: String!
  posts: [Post!]!
}

type Query {
  user(id: ID!): User
}

type Mutation {
  createPost(title: String!, body: String!): Post!
}</code></pre>

            <h3>GraphQL vs REST</h3>
            <ul>
                <li><strong>Гибкость</strong> — GraphQL: клиент управляет данными</li>
                <li><strong>Кэширование</strong> — REST: HTTP кэш из коробки</li>
                <li><strong>Типизация</strong> — GraphQL: строгая схема как живая документация</li>
            </ul>

            <p>GitHub, Shopify, Twitter используют GraphQL для своих публичных API.</p>

            <p><strong>Создатель:</strong> Meta (Facebook) | <strong>Год открытия:</strong> 2015 | <strong>Спецификация:</strong> graphql.org</p>
        """
    },
}

# Категории для навигации
CATEGORIES = {
    "languages": {"title": "Языки программирования", "icon": "💬"},
    "tools": {"title": "Инструменты", "icon": "🛠"},
    "cs": {"title": "Информатика", "icon": "🧠"},
    "areas": {"title": "Области разработки", "icon": "🚀"},
    "databases": {"title": "Базы данных", "icon": "🗄️"},
}


@app.route('/')
def index():
    return render_template('index.html', articles=ARTICLES, categories=CATEGORIES)


@app.route('/article/<article_key>')
def article(article_key):
    if article_key not in ARTICLES:
        return redirect(url_for('index'))
    art = ARTICLES[article_key]
    # Похожие статьи из той же категории
    related = {k: v for k, v in ARTICLES.items()
               if v['category'] == art['category'] and k != article_key}
    return render_template('article.html', article=art, article_key=article_key, related=related, all_categories=CATEGORIES)


@app.route('/category/<cat_key>')
def category(cat_key):
    if cat_key not in CATEGORIES:
        return redirect(url_for('index'))
    cat_articles = {k: v for k, v in ARTICLES.items() if v['category'] == cat_key}
    return render_template('category.html',
                           category=CATEGORIES[cat_key],
                           cat_key=cat_key,
                           articles=cat_articles,
                           all_categories=CATEGORIES)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
