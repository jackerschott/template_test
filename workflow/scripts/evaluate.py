from pathlib import Path

def main(predictions_path: str, results_path: str):
    Path(results_path).touch()


# satisfy the linter
if not "snakemake" in globals():
    snakemake = None


if __name__ == "__main__":
    main(
        snakemake.input["predictions"],
        snakemake.output["results"],
    )
