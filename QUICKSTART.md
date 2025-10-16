# 🚀 Быстрый старт - CashFlow Story Python

## За 5 минут до первого API запроса!

### Шаг 1: Клонировать репозиторий

```bash
git clone https://github.com/leval907/-claude_cashflowstory_python.git
cd -claude_cashflowstory_python
```

### Шаг 2: Установить Python

Убедитесь что у вас Python 3.11+:

```bash
python --version
# Должно быть: Python 3.11.x или выше
```

### Шаг 3: Создать виртуальное окружение

```bash
# Создать venv
python -m venv venv

# Активировать (Linux/Mac)
source venv/bin/activate

# Активировать (Windows)
venv\Scripts\activate
```

### Шаг 4: Установить зависимости

```bash
cd backend
pip install -r requirements.txt
```

### Шаг 5: Запустить сервер

```bash
python main.py
```

Сервер запущен! 🎉

```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

### Шаг 6: Проверить работу

Откройте в браузере:

**1. API документация (Swagger UI):**
```
http://localhost:8000/docs
```

**2. Демо данные Rebeccas Coffee:**
```
http://localhost:8000/api/demo/rebeccas
```

**3. Health check:**
```
http://localhost:8000/health
```

## 📊 Ваш первый API запрос

### Через curl:

```bash
curl -X POST http://localhost:8000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "Test Company",
    "period": "2024-Q4",
    "revenue": 1000000,
    "cost_of_goods": 600000,
    "overheads": 200000,
    "depreciation": 50000,
    "interest_paid": 10000,
    "tax_paid": 30000,
    "cash": 100000,
    "accounts_receivable": 150000,
    "inventory": 200000,
    "fixed_assets": 500000,
    "current_liabilities": 120000,
    "noncurrent_liabilities": 300000,
    "accounts_payable": 80000
  }'
```

### Через Python:

```python
import requests

response = requests.post(
    "http://localhost:8000/api/calculate",
    json={
        "company_name": "Test Company",
        "period": "2024-Q4",
        "revenue": 1000000,
        "cost_of_goods": 600000,
        "overheads": 200000
    }
)

result = response.json()
print(f"Gross Margin: {result['analytics']['gross_margin_percent']:.1f}%")
print(f"ROE: {result['analytics']['return_on_equity']:.1f}%")
```

### Через Swagger UI:

1. Откройте http://localhost:8000/docs
2. Найдите `/api/calculate`
3. Нажмите "Try it out"
4. Вставьте JSON данные
5. Нажмите "Execute"

## 🧪 Запустить тесты

```bash
# Из корневой папки проекта
pytest tests/ -v

# С покрытием кода
pytest tests/ --cov=backend
```

## 🐳 Docker (альтернативный метод)

```bash
# Собрать и запустить
docker-compose up --build

# Сервер будет на http://localhost:8000
```

## ❓ Что-то не работает?

### Ошибка: "ModuleNotFoundError"

```bash
# Убедитесь что вы в правильной папке
cd backend

# И venv активирован
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate      # Windows
```

### Ошибка: "Port 8000 already in use"

```bash
# Найти процесс
lsof -i :8000  # Linux/Mac
netstat -ano | findstr :8000  # Windows

# Или изменить порт
python main.py --port 8001
```

### Ошибка: "pydantic.error_wrappers.ValidationError"

Проверьте что `revenue` > 0 в вашем JSON запросе.

## 📚 Что дальше?

- 📖 Читайте [полный README](README.md)
- 🧮 Изучите [формулы](backend/calculations.py)
- 🎓 Попробуйте [Jupyter notebook](notebooks/)
- 🔌 Интегрируйте с вашим приложением

## 💬 Вопросы?

Создайте Issue в GitHub или пишите: leval907@gmail.com

---

**Готово! Теперь у вас работает финансовый API! 🎉**
