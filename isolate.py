from rdflib import Graph
from SPARQLWrapper import SPARQLWrapper, JSON
from emma.kb.kb_load_refactor import KBLoader

# end = "http://semaphore-dev:8080/swoe/api/t/WyJzdGV2ZWpzIiwxNTc4NTg5MDcwLCJNQ0VDRHdEYXBvYmwvWTVsem1jZHZmTnhhUUlPZUg4NC82bUp1SjVpSnIyTi9odz0iXQ/model:NCIThesaurus/sparql"
mesh_end = """http://semaphore-dev.abbvienet.com:8080/swoe/api/t/WyJlZG1pc21sIiwxNTc4ODM3MTQ2LCJNQ0FDRGxKaTc5ek01L0l2YzJoZkxmRzVBZzQ4U2ExdTNFakkrOFR5SFZwazJRPT0iXQ/model:MeSH2019%5C-07%5C-29/sparql"""

# sparql = SPARQLWrapper(end)

# query = """
#  SELECT DISTINCT ?prop ?pObj 
#  WHERE {
#      ?s ?prop ?obj .
#      ?prop  <http://www.w3.org/2000/01/rdf-schema#label> ?pObj

#  }
# LIMIT 1000
#  """

# sparql.setQuery(query)
# sparql.setReturnFormat(JSON)
# res = sparql.query().convert()


# print(res)
# # for r in res:
# #      print(r)     

kb_load = KBLoader()
mesh_kb = kb_load.load_mesh(mesh_end)
# nci_kb = kb_load.load_nci('C:\\Users\\EDMISML\\Desktop\\ont_align_data\\disease_subtrees\\nci_dis_subset.rdf')