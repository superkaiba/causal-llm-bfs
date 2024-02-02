import dagma.utils as utils
from cdt.metrics import SID
from utils import adj_mat_to_edge_list, is_dag

def accuracy(B_true, B_est):
  '''
  B_true and B_est are edge lists
  '''
  B_true = set(B_true)
  B_est = set(B_est)
  return len(B_true.intersection(B_est)) / len(B_true.union(B_est))

def precision(B_true, B_est):
  '''
  B_true and B_est are edge lists
  '''
  B_true = set(B_true)
  B_est = set(B_est)
  return len(B_true.intersection(B_est)) / len(B_est)

def recall(B_true, B_est):
  '''
  B_true and B_est are edge lists
  '''
  B_true = set(B_true)
  B_est = set(B_est)
  return len(B_true.intersection(B_est)) / len(B_true)

def F_score(B_true, B_est):
  '''
  B_true and B_est are edge lists
  '''
  p = precision(B_true, B_est)
  r = recall(B_true, B_est)
  if p + r == 0:
    return "p + r = 0"
  return 2 * p * r / (p + r)


def normalized_hamming_distance(prediction, target):
  '''
  prediction and target are edge lists
  calculate the normalized hamming distance

  For a graph with m nodes, the distance is given by ∑m i,j=1 1 m2 1Gij 6=G′ ij , 
  the number of edges that are present in one graph but not the other, 
  divided by the total number of all possible edges.
  '''
  prediction = set(prediction)
  target = set(target)
  total_nodes = set()
  for i,j in target:
    total_nodes.add(i)
    total_nodes.add(j)
  no_overlap = len(prediction.union(target)) - len(prediction.intersection(target))
  nhd = no_overlap / (len(total_nodes) ** 2)
  reference_nhd = (len(prediction) + len(target))/ (len(total_nodes) ** 2)
  return nhd, reference_nhd, nhd / reference_nhd

def compute_metrics(B_true, B_est):
  '''
  B_true and B_est are adjacency matrices
  '''
  is_dag_true = is_dag(B_true)
  is_dag_est = is_dag(B_est)
  B_true = adj_mat_to_edge_list(B_true)
  B_est = adj_mat_to_edge_list(B_est)
  nhd = normalized_hamming_distance(B_true, B_est)
  try:
    sid = SID(B_true, B_est)
  except:
    sid = 'Not a DAG'
  return {
    'precision': precision(B_true, B_est),
    'recall': recall(B_true, B_est),
    'Number of predicted edges': len(B_est),
    'Number of true edges': len(B_true),
    'F_score': F_score(B_true, B_est),
    'SID': sid,
    'Is true graph a DAG?': is_dag_true,
    'Is estimated graph a DAG?': is_dag_est,
    'NHD': nhd[0],
    'REFERENCE NHD': nhd[1],
    'RATIO': nhd[2],
    'accuracy': accuracy(B_true, B_est)
  }