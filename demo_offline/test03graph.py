# Note: the module name is psycopg, not psycopg3
import psycopg

# AgensGraph 연결 설정
connection_string = "host=localhost port=5432 dbname=test user=sam password=dooley"

try:
    # Connect to an existing database
    with psycopg.connect(connection_string) as conn:

        # Open a cursor to perform database operations
        with conn.cursor() as cur:

            # AGE 확장 로드
            #cur.execute("LOAD 'age';")
            #cur.execute("SET search_path = ag_catalog, \"$user\", public;")
            
            # 간단한 그래프 쿼리 테스트
            cur.execute("CREATE GRAPH my_graph;")
            cur.execute("SET graph_path = my_graph;")
            cur.execute("CREATE (:Person {name: 'Alice'})-[:KNOWS]->(:Person {name: 'Bob'});")
            cur.execute("MATCH (n) RETURN n;")
            result = cur.fetchall()
            print(result)

except Exception as e:
    print("Connection failed:", e)