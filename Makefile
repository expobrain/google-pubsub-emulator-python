.SILENT: fmt check lint

fmt:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade --exit-zero-even-if-changed --py39-plus {} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		.
	isort --profile=black .
	black .

lint:
	mypy .
	flake8 .

check:
	find . -type d -name ".venv" -prune -o -print -type f -name "*.py" \
		-exec pyupgrade --py39-plus {} \+ 1> /dev/null
	autoflake \
		--in-place \
		--remove-all-unused-imports \
		--ignore-init-module-imports \
		-r \
		-c \
		.
	isort --profile black -c .
	black --check .
