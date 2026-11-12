# Student Mental Health (Depression) Detection

Estimation du risque de dépression chez les étudiants à partir de données tabulaires
(dataset Kaggle *Student Depression Dataset*), servie via une API et une interface web.

> ⚠️ **Avertissement** : ce projet est un outil pédagogique de **dépistage statistique**.
> Il ne constitue en aucun cas un diagnostic médical et ne remplace pas l'avis d'un
> professionnel de santé.

## Statut

🚧 En construction — phase 0 (fondations).

## Démarrage rapide

Prérequis : [uv](https://docs.astral.sh/uv/).

```bash
uv sync                          # crée l'environnement et installe les dépendances
uv run pre-commit install        # active les contrôles avant commit
uv run pytest                    # lance les tests
```

## Qualité

```bash
uv run ruff check     # lint
uv run ruff format    # formatage
uv run mypy           # typage statique (strict)
uv run pytest --cov   # tests + couverture
```
