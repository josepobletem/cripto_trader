# 🤖 Crypto Trader Bot (FastAPI + Binance + OpenAI)

Proyecto de trading automático de criptomonedas en Python, usando FastAPI, Binance API y OpenAI para explicar decisiones. Guarda operaciones en SQLite y corre automáticamente con APScheduler.

---

## 📦 Estructura
```bash
crypto_trader/
├── .env
├── Dockerfile
├── Makefile
├── README.md
├── docker-compose.yml
├── main.py
├── requirements.txt

├── trading/
│   ├── __init__.py
│   ├── binance_client.py
│   ├── strategy.py
│   ├── gpt_helper.py
│   ├── scheduler.py
│   ├── db.py
│   ├── logger.py
│   ├── model.py
│   └── schemas.py

├── tests/
│   ├── conftest.py
│   ├── test_binance_client.py
│   ├── test_gpt_helper.py
│   ├── test_scheduler.py
│   ├── test_strategy.py
│   └── infra/
│       ├── test_deploy_gcp.py     # Test para despliegue GCP simulado o real
│       └── test_deploy_aws.py     # Test para despliegue AWS simulado o real

├── trading.log
├── trades.db

├── infra/
│   ├── gcp/
│   │   ├── main.tf
│   │   └── variables.tf
│   └── aws/
│       ├── main.tf
│       └── variables.tf

└── .github/
    └── workflows/
        └── ci.yml

```

## 🚀 Uso rápido

```bash
make install        # Instala dependencias
make run            # Inicia FastAPI en localhost:8000
make test           # Corre tests unitarios
make docker-up      # Levanta todo con Docker
```


🔁 Webhook para ejecución manual

```bash
curl -X POST http://localhost:8000/webhook
```

📊 Estrategia: Cruce de EMAs

El bot decide:

    buy: EMA corta cruza hacia arriba la EMA larga

    sell: EMA corta cruza hacia abajo

    hold: si no hay señal clara

📄 Requisitos

    .env con:


```bash
BINANCE_API_KEY=...
BINANCE_API_SECRET=...
OPENAI_API_KEY=...
TRADE_SYMBOL=BTCUSDT
TRADE_QUANTITY=0.001
```

🔐 Seguridad

    Las claves se cargan desde .env

    SQLite y logs persistentes via volumen Docker

📦 To-do

    Agregar backtesting

    Panel gráfico con precios y decisiones

    Soporte para múltiples símbolos

🧠 Autor

Desarrollado por José Poblete M.
MIT License

🙌 Créditos

Este proyecto fue creado con el propósito de emprender, aprender y construir una herramienta práctica de inversión basada en automatización, datos y transparencia.

Inspirado en la necesidad de contar con sistemas accesibles y abiertos para operar en el mundo de las criptomonedas de forma responsable y mejor informada.
🚀 Dedicado a

Este proyecto está dedicado a todas las personas que:

    Quieren emprender en tecnología e inversión.

    Buscan aprender desde cero y crear soluciones reales.

    Sueñan con construir herramientas útiles para ellos y su comunidad.

    Creen en la colaboración abierta para mejorar lo que existe.

💡 Mejora y contribuye

crypto_trader está hecho para usarse, aprender y evolucionar.
Siéntete libre de:

    Clonarlo y adaptarlo

    Mejorar la estrategia de trading

    Añadir indicadores más avanzados

    Conectarlo con otros exchanges o APIs

    Contribuir con ideas, feedback o código

Tu participación es bienvenida 🤝