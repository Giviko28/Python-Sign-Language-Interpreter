from SPARQLWrapper import SPARQLWrapper, JSON

def run_query(query):
    sparql = SPARQLWrapper("http://localhost:3030/sparql")
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()

def highest_profit_movie():
    query = """
    PREFIX : <https://www.themoviedb.org/kaggle-export/>
    SELECT ?movie_title (MAX(?profit) AS ?highest_profit)
    WHERE {
        ?movie a :Movie;
               :title ?movie_title;
               :revenue ?revenue;
               :budget ?budget.
        BIND((?revenue - ?budget) AS ?profit)
    }
    GROUP BY ?movie_title
    ORDER BY DESC(?highest_profit)
    LIMIT 1
    """
    return run_query(query)
  
  
def highest_loss_movie():
    query = """
    PREFIX : <https://www.themoviedb.org/kaggle-export/>
      SELECT ?movie_title ?loss
      WHERE {
        ?movie a :Movie;
          :title ?movie_title;
          :revenue ?revenue;
          :budget ?budget.
        BIND((?budget - ?revenue) AS ?loss)
      }
      ORDER BY DESC(?loss)
      LIMIT 1
    """
    return run_query(query)
  
def actor_longest_name():
    query = """
    PREFIX : <https://www.themoviedb.org/kaggle-export/>
        SELECT ?actor ?name (STRLEN(?name) AS ?nameLength)
        WHERE {
          ?actor a :Cast;
            :name ?name.
        }
        ORDER BY DESC(STRLEN(?name))
        LIMIT 1

    """
    return run_query(query)

def shortest_movie_title():
    query = """
    PREFIX : <https://www.themoviedb.org/kaggle-export/>
    SELECT ?movie_title
    WHERE {
        ?movie a :Movie;
               :title ?movie_title.
    }
    ORDER BY ASC(strlen(str(?movie_title)))
    LIMIT 1
    """
    return run_query(query)

def most_expensive_movie_per_time():
    query = """
    PREFIX : <https://www.themoviedb.org/kaggle-export/>
    SELECT ?movie_title (?budget/?runtime AS ?cost_per_minute) ?budget ?runtime
    WHERE {
        ?movie a :Movie;
               :title ?movie_title;
               :budget ?budget;
               :runtime ?runtime.
        FILTER(?runtime > 0)
    }
    ORDER BY DESC(?cost_per_minute)
    LIMIT 1
    """
    return run_query(query)

def lowest_budget_popularity():
    query = """
    PREFIX : <https://www.themoviedb.org/kaggle-export/>
    SELECT ?movie_title ?budget
    WHERE {
        ?movie a :Movie;
               :title ?movie_title;
               :budget ?budget;
               :popularity ?popularity.
        FILTER(?popularity >= 10.0)
    }
    ORDER BY ASC(?budget)
    LIMIT 1
    """
    return run_query(query)

def highest_revenue_popularity_lte_1():
    query = """
    PREFIX : <https://www.themoviedb.org/kaggle-export/>
    SELECT ?movie_title ?revenue
    WHERE {
        ?movie a :Movie;
               :title ?movie_title;
               :revenue ?revenue;
               :popularity ?popularity.
        FILTER(?popularity <= 1.0)
    }
    ORDER BY DESC(?revenue)
    LIMIT 1
    """
    return run_query(query)

if __name__ == '__main__':
    print("Highest profit movie:", highest_profit_movie())
    print("---------------------------------------------")
    print("Highest loss movie:", highest_loss_movie)
    print("---------------------------------------------")
    print("Actor with the longest name:", actor_longest_name())
    print("---------------------------------------------")
    print("Movie with the shortest title:", shortest_movie_title())
    print("---------------------------------------------")
    print("Most expensive movie per time:", most_expensive_movie_per_time())
    print("---------------------------------------------")
    print("Lowest budget movie with popularity >= 10:", lowest_budget_popularity())
    print("---------------------------------------------")
    print("Highest revenue movie with popularity <= 1:", highest_revenue_popularity_lte_1())
