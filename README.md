# Tuto project Dagster

## Installation

installer dagster via pip

commande d'installation  

```bash
pip install dagster dagster-webserver dagster-dg-cli create-dagster dagster-duckdb
```

ajouter Script au PATH pour avoir les commandes

## Initialisation

commande pour crée un projet dagster:  

```bash
create-dagster project nom_du_project
```

commande pour lancer le dagster-webserver:  

```bash
dg dev
```

lancer le localhost pour acceder a UI de dagster  
lien du localhost:  
<http://127.0.0.1:3000>

## Tutoriel

Suivi du tutoriel fourni dans la doc de dagster  
lien:
<https://dagster.io/docs>

## Explication

### Decorateur

@dg.asset -> decorateur qui permet a dagster de traiter l'asset dans son graph

@definitions -> les objets définis doivent etre associé un top-level **definitions** pour etre déployé.  

@dg.definitions -> decorateur qui defini les points d'entré pour charger les definitions au sein de Dagster

@dg.asset_check -> check les assets si ils fournissent les données attendu

### Command

Commande permettant de verifier les issues

```bash
dg check defs
```

Commande qui lance/materialise les assets

```bash
dg launch
```

### Fonction

dg.Definitions ->

dg.AssetCheckResult -> retourn True ou False pour determiner la validité d'un asset

DuckDBResource -> crée une db sur son ordi local, mettre un path valide
