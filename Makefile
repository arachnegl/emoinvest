VENV_PYTHON = ./.venv/bin/python
VENV_PIP = ./.venv/bin/pip
VENV_PYLINT = ./.venv/bin/pylint
CURRENT_DIR = $(shell pwd)
FRONTEND_DIR = src/frontend

# PP -> Project Path
PP = src/emoinvest/


clean:
	-rm -rf .venv
	-rm -f $(PP).env
	-rm -rf res/test_data

flake8:
	./.venv/bin/flake8 src --statistics 

test:
	.venv/bin/py.test src --flake8
	.venv/bin/py.test tests

develop:
	python3 -m venv .venv
	$(VENV_PIP) install --upgrade wheel
	$(VENV_PIP) install -e .[develop]
	$(VENV_PIP) install --upgrade pip

