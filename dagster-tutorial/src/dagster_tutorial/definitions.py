from pathlib import Path

from dagster import definitions, load_from_defs_folder


@definitions
def defs():
    """
    Fonction permetant de charger le module parent dagster-tutorial
    Permet ainsi de charger tout les assets
    """
    return load_from_defs_folder(
        path_within_project=Path(__file__).parent.parent.parent
    )
