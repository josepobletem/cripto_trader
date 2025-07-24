# 🤖 Crypto Trader Bot (FastAPI + Binance + OpenAI)

Proyecto de trading automático de criptomonedas en Python, usando FastAPI, Binance API y OpenAI para explicar decisiones. Guarda operaciones en SQLite y corre automáticamente con APScheduler.

---

🧠 Introducción

crypto_trader es un bot de trading automático de criptomonedas desarrollado con Python, FastAPI, Binance API y OpenAI. Su misión es democratizar el acceso a herramientas inteligentes de inversión, facilitando la toma de decisiones basada en datos, automatización y aprendizaje continuo.

Este proyecto está diseñado como una plataforma de lanzamiento para quienes desean:

    Iniciarse en el mundo del trading algorítmico

    Aprender sobre APIs, automatización y programación orientada a objetos

    Desplegar sistemas reales en la nube (GCP, AWS) con infraestructura como código (Terraform)

    Construir una solución extensible, transparente y auditable

🚀 Lo que se puede alcanzar con este proyecto

Con crypto_trader, puedes:

    📈 Crear una estrategia de trading personalizada y automatizada

    🧠 Generar explicaciones de decisiones usando IA (GPT-4)

    📊 Exponer métricas en tiempo real con Prometheus

    ✅ Validar y testear tu lógica con cobertura unitaria y de integración

    🐳 Contenerizar tu aplicación y desplegarla en minutos con Docker y Terraform

    ☁️ Adaptarlo para correr en Cloud Run, EC2, Fargate, Kubernetes, u otros entornos

Este proyecto no es solo un bot, es una base sólida para:

    Tu primer emprendimiento de trading automatizado

    Una startup de inteligencia financiera

    Un MVP para inversionistas o analistas cuantitativos

    Un portafolio técnico fuerte y aplicable en el mundo real

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