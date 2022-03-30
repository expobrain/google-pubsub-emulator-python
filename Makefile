.SILENT: fmt lint

fmt:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade --exit-zero-even-if-changed --py38-plus {} \+ 1> /dev/null
	autoflake --in-place --remove-all-unused-imports --recursive .
	isort --profile=black .
	black .

lint:
	mypy .
	flake8 .
