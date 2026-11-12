"""Prédiction du risque de dépression chez les étudiants."""

from importlib.metadata import version

__version__ = version("depression")


def main() -> None:
    """Point d'entrée de la CLI (provisoire, sera remplacé en phase 3)."""
    print(f"depression {__version__}")
