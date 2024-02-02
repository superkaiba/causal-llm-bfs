import bnlearn as bn
from algs.pc.pc import pc
from algs.ges.ges import ges
from algs.notears.notears import notears
from algs.llm.pairwise import llm_pairwise 
from algs.llm.bfs import llm_bfs
from algs.dagma_baseline.dagma_wrapper import dagma_nonlinear_wrapper, dagma_linear_wrapper
import numpy as np
from metrics import compute_metrics
from args import get_args
from data.var_names_and_desc import *
import json
import os
import pandas as pd
from data.init_prompts import *

args = get_args()

if args.dataset == "neuropathic":
  adj_mat = np.load('./data/neuropathic_dag_gt.npy')
  df = pd.read_csv(f'./data/neuropathic_data_{args.n_samples}.csv')
else:
  dag = bn.import_DAG(f'./data/{args.dataset}.bif')
  var_names = dag['adjmat'].columns
  adj_mat = dag['adjmat'].to_numpy().astype(int)
  df = bn.sampling(dag, n=args.n_samples)

data = df.to_numpy()
gaussian_noise = np.random.normal(loc=0.0, scale=0.00001, size=data.shape)

if args.alg == 'ges':
  data = data + gaussian_noise
  predicted_adj_mat = ges(data, score_func='local_score_BIC', maxP=None, parameters=None)
elif args.alg == 'pc':
  data = data + gaussian_noise
  predicted_adj_mat = pc(data)
elif args.alg == 'dagma_nonlinear':
  predicted_adj_mat = dagma_nonlinear_wrapper(data, len(adj_mat), args.lambda1, args.lambda2)
elif args.alg == 'dagma_linear':
  predicted_adj_mat = dagma_linear_wrapper(data, args.lambda1)
elif args.alg == 'notears':
  predicted_adj_mat = notears(data, lambda1=args.lambda1, loss_type='l2', w_threshold=args.w_threshold)
elif args.alg == 'llm_pairwise':
  predicted_adj_mat = llm_pairwise(VAR_NAMES_AND_DESC[args.dataset], prompts[args.dataset], df, include_statistics=False)
elif args.alg == 'llm_pairwise_with_statistics':
  predicted_adj_mat = llm_pairwise(VAR_NAMES_AND_DESC[args.dataset], prompts[args.dataset], df, include_statistics=True)
elif args.alg == 'llm_bfs':
  predicted_adj_mat = llm_bfs(VAR_NAMES_AND_DESC[args.dataset], args.dataset, df, include_statistics=False)
elif args.alg == 'llm_bfs_with_statistics':
  predicted_adj_mat = llm_bfs(VAR_NAMES_AND_DESC[args.dataset], args.dataset, df, include_statistics=True)
else:
  raise ValueError(f"Unknown algorithm {args.alg}")


metrics = compute_metrics(adj_mat, predicted_adj_mat)
logdir = f"{args.logdir}/{args.dataset}/{args.n_samples}"
os.makedirs(logdir, exist_ok=True)
logfile = f"{logdir}/{args.alg}_lambda1={args.lambda1}.json"
with open(logfile, "w") as outfile: 
    json.dump(metrics, outfile)
