# 🤖 Crypto Trader Bot (FastAPI + Binance + OpenAI)

Proyecto de trading automático de criptomonedas en Python, usando FastAPI, Binance API y OpenAI para explicar decisiones. Guarda operaciones en SQLite y corre automáticamente con APScheduler.

---

## 📦 Estructura
```bash
crypto_trader/
├── .env                             # Claves Binance / OpenAI / configuración
├── Dockerfile                       # Imagen para producción
├── Makefile                         # Comandos útiles: test, run, build
├── README.md                        # Documentación del proyecto
├── docker-compose.yml              # Orquestación de contenedor
├── main.py                          # API FastAPI + Scheduler
├── requirements.txt                 # Dependencias

├── trading/
│   ├── __init__.py
│   ├── binance_client.py           # Clase BinanceClient: precios y órdenes
│   ├── strategy.py                 # Clase TradingStrategy: lógica de EMA
│   ├── gpt_helper.py               # Clase GPTExplainer: explica decisiones
│   ├── scheduler.py                # Clase TradingScheduler: ejecución cíclica
│   ├── db.py                       # Clase DatabaseManager: persistencia SQLite
│   ├── logger.py                   # Clase Logger
│   └── model.py                    # Modelo Trade para SQLAlchemy

├── tests/
│   ├── conftest.py                 # Fixtures de test
│   ├── test_binance_client.py     # Test mock de Binance
│   ├── test_gpt_helper.py         # Test mock de OpenAI
│   ├── test_scheduler.py          # Test integración lógica de ciclo
│   └── test_strategy.py           # Test unitario de lógica de decisión

├── trading.log                     # Logs del bot
├── trades.db                       # Base de datos SQLite

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
