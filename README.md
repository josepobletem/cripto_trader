# 🤖 Crypto Trader Bot (FastAPI + Binance + OpenAI)

Proyecto de trading automático de criptomonedas en Python, usando FastAPI, Binance API y OpenAI para explicar decisiones. Guarda operaciones en SQLite y corre automáticamente con APScheduler.

---

## 📦 Estructura

crypto_trader/
├── main.py # API principal FastAPI
├── .env # Claves Binance / OpenAI
├── Dockerfile, docker-compose.yml
├── trading/
│ ├── binance_client.py # Conexión Binance
│ ├── strategy.py # Estrategia (EMA)
│ ├── gpt_helper.py # Explicación GPT
│ ├── scheduler.py # Automatización
│ ├── db.py # SQLite
│ └── logger.py
├── tests/ # Tests unitarios


---

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
