import rdflib

if __name__ == '__main__':
    path_to_graph = "iai_mauchamp_chelidze/topic2_Knowledge_Representation/exercice_6/TMDB.ttl"
    g = rdflib.Graph()
    g.parse(path_to_graph, format='turtle')

    query_a = '''SELECT DISTINCT ?department
            WHERE {
            ?crew a :Crew;
                :department ?department.
            }
    '''
    query_b = '''
            SELECT DISTINCT ?name
            WHERE {
            ?company a :Company;
                :name ?name.
            }
    '''

    query_c = '''SELECT DISTINCT ?title
            WHERE {
                ?movie a :Movie;
                    :Keywords ?keyword;
                    :title ?title.
                ?keyword a :Keywords;
                    :name 'julius caesar'.
            }
    '''
    query_result = g.query(query_b)

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
    for result in result_list:
        print(result)