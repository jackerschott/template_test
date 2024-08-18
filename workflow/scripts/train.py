from pathlib import Path

from template_test import bla

def main(model_path: str):
    print(bla(1, 2))
    Path(model_path).touch()


# satisfy the linter
if not "snakemake" in globals():
    snakemake = None


if __name__ == "__main__":
    main(
        snakemake.output["model"]
    )
