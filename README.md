# Efficient Causal Graph Discovery Using Large Language Models

## Setup
`conda env create -f environment.yml`

`conda activate LLM_for_causal`

## Reproducing Results
To reproduce the results from the paper, run 

`python run.py --dataset DATASET_NAME --alg ALG_NAME --n_samples N_SAMPLES`

with the desired `DATASET_NAME`, `ALG_NAME`, and `N_SAMPLES`

The results will be saved in `./logs/DATASET_NAME/N_SAMPLES/alg.json`
The supported values for `DATASET_NAME` are:
- `asia`
- `child`
- `neuropathic`

The supported values for `ALG_NAME` are:
- `pc`
- `ges`
- `notears`
- `dagma_linear`
- `llm_pairwise` (Note that to run `llm_pairwise` you must provide a valid OpenAI API key in `algs/llm/pairwise.py`)
- `llm_pairwise_with_statistics` (Note that to run `llm_pairwise_with_statistics` you must provide a valid OpenAI API key in `algs/llm/pairwise.py`)
- `llm_bfs` (Note that to run `llm_bfs` you must provide a valid OpenAI API key in `algs/llm/bfs.py`)
- `llm_bfs_with_statistics` (Note that to run `llm_bfs_with_statistics` you must provide a valid OpenAI API key in `algs/llm/bfs.py`)

The supported values for `N_SAMPLES` are:
- 100
- 1000
- 10000
