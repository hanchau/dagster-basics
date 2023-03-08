# dagster_basics

Exploring the [Dagster](https://dagster.io/) orchestration tool with [`dagster project scaffold`](https://docs.dagster.io/getting-started/create-new-project).

## Getting started

```bash
pip install -e ".[dev]"
```

Then, start the Dagster UI web server:

```bash
dagster dev
```

Open http://localhost:3000 with your browser to see the project.


## Development

### ETL 

Can add the ETL related assets in dagster_basics directory.

### Adding new Python dependencies

Add the dependency in setup.py file.
### Unit testing

Tests are in the `dagster_basics_tests` directory and you can run tests using `pytest`:

```bash
pytest -v
```
