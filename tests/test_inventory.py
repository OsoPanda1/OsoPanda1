from pathlib import Path

from tamv_digital_nexus.inventory import load_inventory, save_inventory
from tamv_digital_nexus.models import RepoArtifact


def test_inventory_roundtrip(tmp_path: Path) -> None:
    manifest = tmp_path / "repos.json"
    source = [RepoArtifact(name="OsoPanda1", source_url="https://github.com/OsoPanda1/OsoPanda1.git")]
    save_inventory(manifest, source)

    loaded = load_inventory(manifest)
    assert len(loaded) == 1
    assert loaded[0].name == "OsoPanda1"
