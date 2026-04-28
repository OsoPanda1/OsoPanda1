.PHONY: bootstrap dry-run fmt check test integrate serve

bootstrap:
	python scripts/unify_repos.py --owner OsoPanda1 --target-root sources --manifest-out config/repos.json --max-repos 177

dry-run:
	python scripts/unify_repos.py --owner OsoPanda1 --manifest-out config/repos.json --max-repos 177 --dry-run

integrate:
	python -m tamv_digital_nexus.cli integrate --inventory config/repos_seed.json --cache-root cache/repos --workspace-root sources --index-db cache/nexus_index.db --index-json cache/nexus_index.json

serve:
	python -m tamv_digital_nexus.cli serve --index-db cache/nexus_index.db --host 127.0.0.1 --port 8080

fmt:
	python -m compileall scripts src tests

test:
	python -m pytest -q

check: fmt test
