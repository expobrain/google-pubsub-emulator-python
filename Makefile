fmt:
	autoflake --in-place --remove-all-unused-imports --recursive .
	isort --profile=black .
	black .

lint:
	mypy .
	flake8 .
