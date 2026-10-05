from dagster_duckdb import DuckDBResource

import dagster as dg

# mettre un path existant sur son ordinateur
database_resource = DuckDBResource(
    database="C:/msys64/home/Flykorov/tuto_dagster_duckdb/jaffle_platform.duckdb"
)


@dg.definitions
def resources():
    return dg.Definitions(
        resources={
            "duckdb": database_resource,
        }
    )
