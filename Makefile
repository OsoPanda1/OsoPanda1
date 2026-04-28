.PHONY: bootstrap dry-run fmt check

bootstrap:
	python scripts/unify_repos.py --owner OsoPanda1 --target-root sources --manifest-out config/repos.json --max-repos 177

dry-run:
	python scripts/unify_repos.py --owner OsoPanda1 --manifest-out config/repos.json --max-repos 177 --dry-run

fmt:
	python -m compileall scripts src

check: fmt
	python scripts/unify_repos.py --owner OsoPanda1 --manifest-out config/repos.json --max-repos 5 --dry-run
