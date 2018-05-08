import editdistance
import io
import itertools
import networkx as nx
import nltk
import os

def build_graph(nodes):
    gr = nx.Graph() 
    gr.add_nodes_from(nodes)
    nodePairs = list(itertools.combinations(nodes, 2))
    for pair in nodePairs:
        firstString = pair[0]
        secondString = pair[1]
        levDistance = editdistance.eval(firstString, secondString)
        gr.add_edge(firstString, secondString, weight=levDistance)
    return gr

def extract_sentences(text, summary_length=200, clean_sentences=False, language='english'):
    sent_detector = nltk.data.load('tokenizers/punkt/'+language+'.pickle')
    sentence_tokens = sent_detector.tokenize(text.strip())
    graph = build_graph(sentence_tokens)
    calculated_page_rank = nx.pagerank(graph, weight='weight')
    sentences = sorted(calculated_page_rank, key=calculated_page_rank.get,reverse=True)
    summary = ' '.join(sentences)
    summary_words = summary.split()
    summary_words = summary_words[0:summary_length]
    dot_indices = [idx for idx, word in enumerate(summary_words) if word.find('.') != -1]
    if clean_sentences and dot_indices:
        last_dot = max(dot_indices) + 1
        summary = ' '.join(summary_words[0:last_dot])
    else:
        summary = ' '.join(summary_words)
    return summary

