# Efficient Full Causal Graph Discovery Using Large Language Models

## Setup
`conda env create -f environment.yml`

`conda activate LLM_for_causal`

## Reproducing Results
To reproduce the results from the paper, run 

`python run.py --dataset DATASET_NAME --alg ALG_NAME --n_samples N_SAMPLES`

with the desired `DATASET_NAME`, `ALG_NAME`, and `N_SAMPLES`

The supported values for `DATASET_NAME` are:
- `alarm`
- `asia`
- `child`
- `insurance`
- `neuropathic`


The supported values for `ALG_NAME` are:
- `pc`
- `ges`
- `notears`
- `dagma_linear`
- `llm_pairwise`
- `llm_bfs`

The supported values for `N_SAMPLES` are:
- 100
- 1000
- 10000