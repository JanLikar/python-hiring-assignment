init: venv/.installed setup.py

venv/.installed: setup.py
	python3 -m venv venv
	venv/bin/pip install -e ".[dev]"
	touch venv/.installed

test: init
	pytest tests
