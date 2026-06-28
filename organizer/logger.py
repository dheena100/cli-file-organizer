from functools import wraps
from pathlib import Path
from datetime import datetime
import time
from typing import Any, Callable

LOG_FILE = Path("logs/execution.log")
LOG_FILE.parent.mkdir(exist_ok=True)

print(f"Logging to: {LOG_FILE.resolve()}")

def log_execution(func: Callable[..., Any]) -> Callable[..., Any]:
    """Decorator to log execution details."""

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        print("Decorator is running...")

        start = time.perf_counter()

        result = func(*args, **kwargs)

        end = time.perf_counter()
        runtime = end - start

        with LOG_FILE.open("a", encoding="utf-8") as log:
            log.write("=" * 50 + "\n")
            log.write(f"Time      : {datetime.now()}\n")
            log.write(f"Function  : {func.__name__}\n")
            log.write(f"Args      : {args}\n")
            log.write(f"Kwargs    : {kwargs}\n")
            log.write(f"Runtime   : {runtime:.4f} sec\n\n")

        print("Log written successfully.")

        return result

    return wrapper