import argparse
def get_args():
    parser = argparse.ArgumentParser(description='LLM4Causal')
    parser.add_argument('--dataset', type=str, default='alarm', help='dataset name')
    parser.add_argument('--alg', type=str, default='bfs', help='algorithm name')
    parser.add_argument('--n_samples', type=int, default=1000, help='number of samples')
    parser.add_argument('--lambda1', type=float, default=0.01, help='lambda for NOTEARS and DAGMA')
    parser.add_argument('--lambda2', type=float, default=0.005, help='lambda2 for DAGMA')
    parser.add_argument('--w_threshold', type=float, default=0.3, help='w_threshold for NOTEARS')
    parser.add_argument('--logdir', type=str, default='./logs', help='log directory')
    args = parser.parse_args()
    return args