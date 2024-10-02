install:
	poetry install

test:
	poetry run pytest

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install dist/*.whl --force-reinstall

package-uninstall:
	python3 -m pip uninstall dist/*.whl

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff
	poetry run flake8 tests

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build