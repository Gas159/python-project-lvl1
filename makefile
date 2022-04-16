# Makefile

install: #install ))
	poetry install

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games

patch:
	poetry install
	poetry publish --dry-run
	poetry build
	poetry run flake8 brain_games
	python3 -m pip install --user dist/*.whl

asciinema:
	asciinema rec
