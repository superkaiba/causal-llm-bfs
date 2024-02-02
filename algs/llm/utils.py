import numpy as np
import dagma.utils as utils
from cdt.metrics import SID

class PreviousEdges:
  def __init__(self):
      self.previous_edges = {}

  def add_node(self, node):
    if node not in self.previous_edges:
      self.previous_edges[node] = {
        "incoming":[],
        "outgoing":[]
      }
    
  def add_edge_pair_wise(self, head, tail, choice):
    self.add_node(head)
    self.add_node(tail)
    if choice == 'A':
      self.previous_edges[head]["outgoing"].append(tail)
      self.previous_edges[tail]["incoming"].append(head)
    elif choice == 'B':
      self.previous_edges[tail]["outgoing"].append(head)
      self.previous_edges[head]["incoming"].append(tail)
      
  def add_edge_full_graph(self, head, tails):
    self.add_node(head)
    for tail in tails:
      self.add_node(tail)
      self.previous_edges[head]["outgoing"].append(tail)
      self.previous_edges[tail]["incoming"].append(head)

  def get_previous_relevant_edges_string(self, head, tail):
    output_str = ''
    if head in self.previous_edges:
      for node in self.previous_edges[head]["outgoing"]:
        output_str += f'{head} causes {node}.\n'
      for node in self.previous_edges[head]["incoming"]:
        output_str += f'{node} causes {head}.\n'
      
    if tail in self.previous_edges:
      for node in self.previous_edges[tail]["outgoing"]:
        output_str += f'{tail} causes {node}.\n'
      for node in self.previous_edges[tail]["incoming"]:
        output_str += f'{node} causes {tail}.\n'
    return output_str
  
  def get_all_edges_string(self):
    output_str = ''
    for head in self.previous_edges:
      for node in self.previous_edges[head]["outgoing"]:
        output_str += f'{head} causes {node}.\n'
      for node in self.previous_edges[head]["incoming"]:
        output_str += f'{node} causes {head}.\n'
    return output_str
  
  def get_adjacency_matrix(self, vars):
    n = len(vars)
    adj_matrix = np.zeros((n, n))
    for i, var in enumerate(vars):
      if var in self.previous_edges:
        for node in self.previous_edges[var]["outgoing"]:
          j = vars.index(node)
          adj_matrix[i][j] = 1
    return adj_matrix
    


def adjacency_matrix_to_edge_list(adjacency_matrix):
  '''
  adjacency_matrix is a numpy array
  '''
  edge_list = []
  for i in range(adjacency_matrix.shape[0]):
    for j in range(adjacency_matrix.shape[1]):
      if adjacency_matrix[i,j] == 1:
        edge_list.append((i,j))
  return edge_list

def precision(B_true, B_est):
  '''
  B_true and B_est are adjacency matrices
  '''
  B_true = set(adjacency_matrix_to_edge_list(B_true))
  B_est = set(adjacency_matrix_to_edge_list(B_est))
  return len(B_true.intersection(B_est)) / len(B_est)

def recall(B_true, B_est):
  '''
  B_true and B_est are adjacency matrices
  '''
  B_true = set(adjacency_matrix_to_edge_list(B_true))
  B_est = set(adjacency_matrix_to_edge_list(B_est))
  return len(B_true.intersection(B_est)) / len(B_true)

def F_score(B_true, B_est):
  '''
  B_true and B_est are adjacency matrices
  '''
  p = precision(B_true, B_est)
  r = recall(B_true, B_est)
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
  B_true_edge_list = adjacency_matrix_to_edge_list(B_true)
  B_est_edge_list = adjacency_matrix_to_edge_list(B_est)
  nhd = normalized_hamming_distance(B_true_edge_list, B_est_edge_list)
  try:
    sid = SID(B_true, B_est)
  except:
    sid = 'Not a DAG'
  return {
    'precision': precision(B_true, B_est),
    'recall': recall(B_true, B_est),
    'Number of predicted edges': len(B_est_edge_list),
    'Number of true edges': len(B_true_edge_list),
    'F_score': F_score(B_true, B_est),
    'SID': sid,
    'NHD': nhd[0],
    'REFERENCE NHD': nhd[1],
    'RATIO': nhd[2],
    'accuracy': utils.count_accuracy(B_true, B_est)
  }