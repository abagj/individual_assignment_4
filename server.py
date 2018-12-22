import math
import flask


graph = {}

def find_dos(a, b, visited=None):
    if visited is None:
        visited = set()

    # Detect cycles
    if a in visited or a not in graph:
        return math.inf

    visited.add(a)
    if b in graph[a]:
        return 0

    dos = math.inf
    for n in graph[a]:
        new_dos = 1 + find_dos(n, b)
        dos = min(dos, new_dos)

    return dos

app = flask.Flask(__name__)

@app.route('/', methods=['POST'])
def set_graph():
    graph.clear()
    graph.update(flask.request.get_json())
    return flask.jsonify(message='Graph updated', graph=graph)

@app.route('/degree_of_separation/<origin>/<destination>')
def degree_of_separation(origin, destination):
    return str(find_dos(origin, destination))
