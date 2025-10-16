# 💰 CashFlow Story - Python Edition

> **B2B Financial Analytics Platform** - Автоматический расчет 21+ финансовых коэффициентов с использованием Python, FastAPI и Pandas

[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🎯 Зачем этот проект?

Финансовым аналитикам нужно быстро оценивать компании, но ручной расчет 21+ коэффициентов занимает часы. **CashFlow Story** автоматизирует это:

- ✅ Загружаете P&L и Balance Sheet
- ✅ Получаете 21 коэффициент за секунды
- ✅ Сравниваете периоды и компании
- ✅ Экспортируете в Excel для презентаций

## 🚀 Быстрый старт

### 1. Установка

```bash
# Клонировать репозиторий
git clone https://github.com/leval907/-claude_cashflowstory_python.git
cd -claude_cashflowstory_python/backend

# Создать виртуальное окружение
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Установить зависимости
pip install -r requirements.txt
```

### 2. Запуск сервера

```bash
# Запустить FastAPI server
python main.py

# Сервер доступен на:
# http://localhost:8000
# API документация: http://localhost:8000/docs
```

### 3. Тестовый запрос

```bash
# Получить демо данные Rebeccas Coffee
curl http://localhost:8000/api/demo/rebeccas

# Или откройте в браузере:
http://localhost:8000/docs
```

## 📊 Что умеет платформа?

### 21 финансовая метрика в 3 группах:

#### 🟢 Группа 1: Прибыльность (Profitability)
1. **Revenue Growth %** - Рост выручки
2. **Gross Margin %** - Валовая маржа
3. **Operating Profit %** - Операционная прибыль
4. **Net Profit %** - Чистая прибыль
5. **EBITDA %** - EBITDA маржа
6. **Interest Coverage** - Покрытие процентов

#### 🔵 Группа 2: Оборотный капитал (Working Capital)
7. **Accounts Receivable Days** - Оборачиваемость дебиторки
8. **Inventory Days** - Оборачиваемость запасов
9. **Accounts Payable Days** - Оборачиваемость кредиторки
10. **Working Capital Cycle** - Цикл оборотного капитала
11. **Working Capital per 100** - Оборотный капитал на 100 выручки
12. **Current Ratio** - Коэффициент текущей ликвидности

#### 🟣 Группа 3: Эффективность капитала (Capital Efficiency)
13. **Return on Capital %** - Рентабельность капитала
14. **Asset Turnover** - Оборачиваемость активов
15. **ROE %** - Рентабельность собственного капитала
16. **ROA %** - Рентабельность активов
17. **Fixed Assets Turnover** - Оборачиваемость основных средств
18. **Debt to Equity** - Соотношение долга к капиталу
19. **Debt to Capital** - Доля долга в структуре капитала
20. **Equity Ratio %** - Доля собственного капитала
21. **Operating Cash Flow** - Операционный денежный поток

## 📖 Примеры использования

### Python API

```python
from calculations import calculate_analytics

# Входные данные
data = {
    'revenue': 6600000,
    'cost_of_goods': 4700000,
    'overheads': 1100000,
    'depreciation': 180000,
    'interest_paid': 110000,
    'tax_paid': 140000,
    'cash': 200000,
    'accounts_receivable': 1500000,
    'inventory': 1800000,
    'fixed_assets': 2500000,
    'current_liabilities': 1200000,
    'noncurrent_liabilities': 2100000,
    'accounts_payable': 750000
}

# Расчет
analytics = calculate_analytics(data)

# Результаты
print(f"Gross Margin: {analytics['gross_margin_percent']:.1f}%")
print(f"ROE: {analytics['return_on_equity']:.1f}%")
print(f"Working Capital Days: {analytics['working_capital_days']:.0f}")
```

### REST API

```bash
# Расчет для одного периода
curl -X POST http://localhost:8000/api/calculate \
  -H "Content-Type: application/json" \
  -d '{
    "company_name": "Acme Corp",
    "period": "2024-Q4",
    "revenue": 1000000,
    "cost_of_goods": 600000,
    "overheads": 200000,
    "cash": 100000,
    "accounts_receivable": 150000
  }'

# Batch расчет для нескольких периодов
curl -X POST http://localhost:8000/api/calculate/batch \
  -H "Content-Type: application/json" \
  -d @periods.json
```

### Pandas для массовых расчетов

```python
import pandas as pd
from calculations import calculate_analytics_df

# Загрузить данные
df = pd.read_excel('companies.xlsx')

# Рассчитать для всех компаний
results = calculate_analytics_df(df)

# Экспортировать результаты
results.to_excel('analytics_results.xlsx', index=False)

# Построить графики
import matplotlib.pyplot as plt
results.plot(x='period', y=['roe', 'roa', 'gross_margin_percent'])
plt.show()
```

## 🏗️ Архитектура проекта

```
-claude_cashflowstory_python/
├── backend/
│   ├── main.py              # FastAPI server
│   ├── calculations.py      # 21 формула
│   ├── models.py            # Pydantic models
│   ├── demo_data.py         # Rebeccas Coffee data
│   └── requirements.txt     # Python dependencies
│
├── tests/
│   └── test_calculations.py # Unit tests
│
├── notebooks/
│   └── formulas_test.ipynb  # Jupyter прототипирование
│
└── README.md
```

## 🧪 Тестирование

```bash
# Запустить все тесты
pytest tests/ -v

# С покрытием кода
pytest tests/ --cov=backend --cov-report=html

# Проверить типы
mypy backend/

# Форматирование кода
black backend/
```

## 📊 Demo: Rebeccas Coffee

В проекте есть реальные данные кофейни **Rebeccas Coffee** (2015-2018):

```bash
# Получить демо данные через API
curl http://localhost:8000/api/demo/rebeccas

# Или в Python
from demo_data import get_rebeccas_data
data = get_rebeccas_data()
```

**Ключевые insights:**
- 📈 Рост выручки: 94% за 3 года (3.4M → 6.6M)
- 📉 Падение маржи: 29.4% → 28.8%
- ⚠️ Растущий цикл оборотного капитала: 81 день
- 💰 Высокая долговая нагрузка: Debt/Equity = 1.82

## 🔧 API Endpoints

| Endpoint | Method | Описание |
|----------|--------|----------|
| `/` | GET | API информация |
| `/health` | GET | Health check |
| `/api/calculate` | POST | Расчет для одного периода |
| `/api/calculate/batch` | POST | Batch расчет |
| `/api/demo/rebeccas` | GET | Демо данные Rebeccas Coffee |
| `/docs` | GET | Swagger UI (автоматически) |
| `/redoc` | GET | ReDoc документация |

## 🎓 Финансовые формулы

Все формулы документированы с объяснениями:

<details>
<summary><b>Gross Margin %</b></summary>

```python
gross_margin = revenue - cost_of_goods
gross_margin_percent = (gross_margin / revenue) * 100
```

**Что показывает:** Какой процент от выручки остается после вычета прямых затрат.

**Хорошие значения:**
- Услуги: 70-90%
- Ритейл: 25-40%
- Производство: 20-35%

</details>

<details>
<summary><b>Return on Equity (ROE)</b></summary>

```python
equity = total_assets - total_liabilities
roe = (net_profit / equity) * 100
```

**Что показывает:** Сколько прибыли компания генерирует на каждый рубль собственного капитала.

**Хорошие значения:**
- ROE > 15% - отлично
- ROE 10-15% - хорошо
- ROE < 10% - слабо

</details>

[→ Полная документация формул](docs/FORMULAS.md)

## 🚢 Деплой

### Railway

```bash
# 1. Создать railway.json
{
  "build": {
    "builder": "NIXPACKS"
  },
  "deploy": {
    "startCommand": "cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT"
  }
}

# 2. Деплой
railway up
```

### Render

```yaml
# render.yaml
services:
  - type: web
    name: cashflow-api
    runtime: python
    buildCommand: "pip install -r backend/requirements.txt"
    startCommand: "cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT"
```

### Docker

```bash
# Собрать образ
docker build -t cashflow-api .

# Запустить контейнер
docker run -p 8000:8000 cashflow-api
```

## 🤝 Вклад в проект

Приветствуются Pull Requests! Особенно интересны:

- [ ] Новые финансовые метрики
- [ ] Excel импорт/экспорт
- [ ] Визуализация данных
- [ ] Frontend на React
- [ ] ML модели для прогнозирования

## 📝 Лицензия

MIT License - используйте свободно!

## 🔗 Полезные ссылки

- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [Pandas Documentation](https://pandas.pydata.org)
- [CashFlowStory.com](https://cashflowstory.com) - оригинальный инструмент
- [Financial Ratios Guide](https://corporatefinanceinstitute.com/resources/accounting/financial-ratios/)

## 📧 Контакты

Вопросы? Пишите: **[leval907@gmail.com](mailto:leval907@gmail.com)**

---

**⭐ Если проект полезен - поставьте звезду на GitHub!**
