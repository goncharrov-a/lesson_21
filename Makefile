.PHONY: install test test-api test-smoke allure-meta report serve clean

install:
	python -m pip install -r requirements.txt

test:
	pytest

test-api:
	pytest -m api

test-smoke:
	pytest -m smoke

allure-meta:
	mkdir -p allure-results
	cp allure/categories.json allure-results/categories.json || true
	cp allure/environment.properties allure-results/environment.properties || true

report: test allure-meta
	allure generate allure-results -o allure-report --clean

serve: test allure-meta
	allure serve allure-results

clean:
	rm -rf allure-results allure-report .pytest_cache
