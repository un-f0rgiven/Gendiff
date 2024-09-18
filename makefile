install:
	poetry install

test:
	poetry run pytest

gen-diff:
	poetry run gendiff -h

build: check
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl --force-reinstall

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

lint:
	poetry run flake8 gendiff

selfcheck:
	poetry check

check: selfcheck test lint

.PHONY: install test lint selfcheck check build