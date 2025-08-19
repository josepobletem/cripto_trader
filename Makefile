# Variables de entorno
VENV_DIR=.venv

# Detecta sistema operativo y ajusta paths
ifeq ($(OS),Windows_NT)
	ACTIVATE=.venv/Scripts/activate
	PYTHON=.venv/Scripts/python
	PIP=.venv/Scripts/pip
	CLEAN=rmdir /s /q .venv
	CHECK_VENV=if not exist $(VENV_DIR) python -m venv $(VENV_DIR)
else
	ACTIVATE=.venv/bin/activate
	PYTHON=.venv/bin/python
	PIP=.venv/bin/pip
	CLEAN=rm -rf .venv
	CHECK_VENV=test -d $(VENV_DIR) || python -m venv $(VENV_DIR)
endif

# Crear entorno virtual si no existe
venv:
	$(CHECK_VENV)
	@echo "✅ Entorno virtual creado o ya existente"

# Instalar dependencias
install: venv
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt
	@echo "✅ Dependencias instaladas"

# Ejecutar servidor FastAPI
run: install
	$(PYTHON) -m uvicorn main:app --reload

# Tests
test: install
	$(PYTHON) -m pytest -v

# Formato de código
format: install
	$(PYTHON) -m black .
	$(PYTHON) -m isort .

# Lint
lint: install
	$(PYTHON) -m flake8 trading/ tests/

# Docker
build:
	docker build -t crypto_trader .

# Deploy simulado GCP
deploy-gcp:
	cd infra/gcp && terraform init && terraform apply -auto-approve

# Deploy simulado AWS
deploy-aws:
	cd infra/aws && terraform init && terraform apply -auto-approve

# Limpiar entorno virtual
clean:
	$(CLEAN)
	@echo "🧹 Entorno virtual eliminado"
