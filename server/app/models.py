from py2neo import Graph, Node, Relationship, NodeMatcher,Cursor

url = 'localhost:7474'
username = 'neo4j'
password = 'root'

graph = Graph(url, username=username, password=password)
matcher = NodeMatcher(graph)
# print(graph)
# print(matcher)

def add(word,subCategory):
    wd = Node('Word', name=word)
    sc = Node('Subcategory', name=subCategory)
    rel = Relationship(wd,"belongTo",sc)
    graph.create(rel)
    return True

def search(name):
    query = 'MATCH (word:Word)-[:belongTo]->(subCategory:Subcategory)-[:belongTo]->(category:Category) WHERE word.name = {Jackson} RETURN subCategory.name AS name'
    re = graph.run(query, Jackson=name)
    print(re)