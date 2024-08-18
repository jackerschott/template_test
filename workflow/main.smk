configfile: "workflow/config.yaml"
container: "containers/experiment_env.sif"


experiment_path = config["experiment_path"]


rule all:
    input:
        f"{experiment_path}/results.pdf"


rule evaluate:
    input:
        predictions = f"{experiment_path}/predictions.h5"
    output:
        results = f"{experiment_path}/results.pdf"
    script:
        "scripts/evaluate.py"


rule predict:
    output:
        predictions = f"{experiment_path}/predictions.h5"
    input:
        model = f"{experiment_path}/model.ckpt"
    script:
        "scripts/predict.py"


rule train:
    output:
        model = f"{experiment_path}/model.ckpt"
    script:
        "scripts/train.py"
