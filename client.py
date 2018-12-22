import requests


def update_graph():
    graph = {
        'foo': ['baz', 'bar'],
        'baz': ['koo'],
        'koo': ['bra']
    }

    response = requests.post('http://localhost:5000/', json=graph)
    print(response.text)

    
def test():
    response = requests.get('http://localhost:5000/degree_of_separation/koo/foo')
    print(response.text)
