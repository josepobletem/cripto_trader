install:
	pip install -r requirements.txt

run:
	uvicorn main:app --reload

docker-build:
	docker build -t crypto_trader .

docker-up:
	docker-compose up --build

test:
	pytest tests/
