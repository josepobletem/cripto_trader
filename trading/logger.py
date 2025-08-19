from datetime import datetime


class Logger:
    def log(self, message: str):
        with open("trading.log", "a") as f:
            f.write(f"{datetime.now()} - {message}\n")
