from pathlib import Path

def main(model_path: str, predictions_path: str):
    Path(predictions_path).touch()


# satisfy the linter
if not "snakemake" in globals():
    snakemake = None


if __name__ == "__main__":
    main(
        snakemake.input["model"],
        snakemake.output["predictions"],
    )
