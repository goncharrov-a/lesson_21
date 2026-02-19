from pathlib import Path


def pytest_sessionstart(session):
    results_dir = Path("allure-results")
    results_dir.mkdir(exist_ok=True)

    for src_name in ("categories.json", "environment.properties"):
        src = Path("allure") / src_name
        if src.exists():
            (results_dir / src_name).write_text(src.read_text(encoding="utf-8"), encoding="utf-8")
