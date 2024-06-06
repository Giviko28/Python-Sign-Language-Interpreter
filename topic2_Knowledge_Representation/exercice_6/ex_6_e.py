import rdflib

if __name__ == '__main__':
    path_to_graph = "TMDB.ttl"
    g = rdflib.Graph()
    g.parse(path_to_graph, format='turtle')

    query_d='''        
    SELECT DISTINCT ?title ?revenue
        WHERE {
            ?movie a :Movie;
                :revenue ?revenue;
                :title ?title.
        }
        ORDER BY DESC(?revenue)
        LIMIT 1
        '''
    query_result = g.query(query_d)

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
    for result in result_list:
        if result["?revenue"] > result_max["?revenue"]:
            result_max = result
    print(result_max)
    