import nltk
from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON, XML
from emma.kb.kb_load_refactor import KBLoader

# end = "http://semaphore-dev:8080/swoe/api/t/WyJzdGV2ZWpzIiwxNTc4NTg5MDcwLCJNQ0VDRHdEYXBvYmwvWTVsem1jZHZmTnhhUUlPZUg4NC82bUp1SjVpSnIyTi9odz0iXQ/model:NCIThesaurus/sparql"
mesh_end = """http://semaphore-dev.abbvienet.com:8080/swoe/api/t/WyJlZG1pc21sIiwxNTc4ODM3MTQ2LCJNQ0FDRGxKaTc5ek01L0l2YzJoZkxmRzVBZzQ4U2ExdTNFakkrOFR5SFZwazJRPT0iXQ/model:MeSH2019%5C-07%5C-29/sparql"""

nltk.download()
