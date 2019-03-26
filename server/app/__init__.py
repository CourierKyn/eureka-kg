from .models import graph

graph.schema.create_uniqueness_constraint("Word", "name")
graph.schema.create_uniqueness_constraint("Category", "name")
graph.schema.create_uniqueness_constraint("SubCategory", "name")