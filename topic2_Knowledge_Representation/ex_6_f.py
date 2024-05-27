import rdflib

if __name__ == '__main__':
    path_to_graph = "TMDB.ttl"
    g = rdflib.Graph()
    g.parse(path_to_graph, format='turtle')

    query_f = '''        
    SELECT DISTINCT ?title ?popularity
        WHERE {
            ?movie a :Movie;
                :popularity ?popularity;
                :title ?title.
        }'''
    query_result = g.query(query_f)

    ##for row in query_result:
      ##print(row)
    
    query_vars = query_result.vars
    result_list = [
        {
            var.toPython(): row[var].toPython()
            for var in query_vars
        }
        for row in query_result
    ]
    result_max = result_list[0]
    result_min = result_list[0]
    for result in result_list:
        if result["?popularity"] > result_max["?popularity"]:
            result_max = result
        elif result["?popularity"] < result_min["?popularity"]:
            result_min = result
    print(result_max)
    print(result_min)
    