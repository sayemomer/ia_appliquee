from rdflib import Graph, Literal, RDF, URIRef

# Create a graph
g = Graph()

# Create an RDF URI node to use as the subject for multiple triples
uri = URIRef("http://example.org/Person")

# Add triples using store's add() method.
g.add((uri, RDF.type, URIRef("http://schema.org/Person")))
g.add((uri, URIRef("http://schema.org/name"), Literal("Alice")))

# Iterate over triples in store and print them out.
print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))
