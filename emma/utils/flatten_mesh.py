from SPARQLWrapper import SPARQLWrapper, XML

MESH_END = """http://semaphore-dev.abbvienet.com:8080/swoe/api/t/WyJlZG1pc21sIiwxNTc4ODM3MTQ2LCJNQ0FDRGxKaTc5ek01L0l2YzJoZkxmRzVBZzQ4U2ExdTNFakkrOFR5SFZwazJRPT0iXQ/model:MeSH2019%5C-07%5C-29/sparql"""

def flatten_mesh(mesh_endpoint):
    """
    Query mesh endpoint for relevant subtree
    for each result, extract labels, relations, and other interesting property values
    :param mesh_endpoint: 
    :abbvified: True if passed in URL is abbvie semaphore endpoint url 
    :return: kb as xml 
    """
    disease_query = """
    PREFIX  skosxl: <http://www.w3.org/2008/05/skos-xl#>
    PREFIX  owl:  <http://www.w3.org/2002/07/owl#>
    PREFIX  meshv: <http://id.nlm.nih.gov/mesh/vocab#>
    PREFIX  smartmesh: <http://vocabularies.smartlogic.com/mesh/>
	PREFIX skos: <http://www.w3.org/2004/02/skos/core#> 

    CONSTRUCT 
    { 
        ?disUri ?disProp ?disObj .
  		?disUri skos:prefLabel ?prefLiteral . 
        ?disUri skos:altLabel ?altLiteral .
    }
    WHERE
    { ?disUri (meshv:broaderDescriptor)+ <http://id.nlm.nih.gov/mesh/C> .
        ?disUri  ?disProp ?disObj .
  		?disUri skosxl:prefLabel ?prefLabelUri .
  		?prefLabelUri skosxl:literalForm ?prefLiteral .

        OPTIONAL
        { ?disUri  smartmesh:termLabel  ?label .
            ?label   skosxl:literalForm   ?altLiteral
        }
		
}

"""
    # create sparql instance and fetch json results from endpoint
    sparql = SPARQLWrapper(mesh_endpoint)
    sparql.setQuery(disease_query)

    sparql.setReturnFormat(XML)
    res = sparql.query().convert()

    res.serialize(destination='mesh_dis.xml', format='xml')

flatten_mesh(MESH_END)