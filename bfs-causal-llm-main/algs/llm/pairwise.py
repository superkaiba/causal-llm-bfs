import numpy as np
import pickle
# This code is for v1 of the openai package: pypi.org/project/openai
from openai import OpenAI
import random
from tqdm.autonotebook import tqdm
from .utils import PreviousEdges
from itertools import combinations


def llm_pairwise(var_names_and_desc, prompts, df):
    client = OpenAI(api_key='...')

    # causal_graph = pickle.load(open('dataset/Neuropathic-Pain-Diagnosis-Simulator-master/models/bnm.pickle', 'rb'))
    # list all edges
    edges = list(combinations(df.columns, 2))
    previous_edges = PreviousEdges()
    for e in tqdm(edges):
        if random.random() < 0.5:
            head,tail = e
        else:
            tail,head = e            
        head = var_names_and_desc[head]
        tail = var_names_and_desc[tail]

        query = f'''{prompts["user"]} 
        Here is a description of the causal variables in this causal graph:
        '''
        for var in var_names_and_desc:
            causal_var = var_names_and_desc[var]
            query += f'''{causal_var.name}: {causal_var.description}\n'''

        query += f'''
        Here are the causal relationships you know so far:
        {previous_edges.get_previous_relevant_edges_string(head.name, tail.name)}
        
        Which cause-and-effect relationship is more likely? 
        A. "{head.name}" causes "{tail.name}". 
        B. "{tail.name}" causes "{head.name}". 
        C. There is no causal relationship between "{head.name}" and "{tail.name}".
        Let’s work this out in a step by step way to be sure that we have the right answer. Then provide your final answer within the tags <Answer>A/B/C</Answer>.'''
        response = client.chat.completions.create(
            model="gpt-4-1106-preview",
            messages=[
            {
                "role": "system",
                "content": prompts["system"]
            },
            {
                "role": "user",
                "content": query
            }
            ],
            temperature=0.7,
            max_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        answer = response.choices[0].message.content
        idx = answer.find('<Answer>')
        if idx == -1:
            print("NO ANSWER FOUND")
            print("This was the answer:", answer)
            continue
        choice = answer[idx+8]

        previous_edges.add_edge_pair_wise(head.name, tail.name, choice)

    adj_matrix = previous_edges.get_adjacency_matrix([var_names_and_desc[var].name for var in df.columns])

    return adj_matrix

  
