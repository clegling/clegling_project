install:
	poetry install

project:
	poetry run project

build:
	poetry build

lint:
	poetry run flake8 .

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl
