from flask import Flask, url_for

app = Flask(__name__)


def has_no_empty_params(rule):
    defaults = rule.defaults if rule.defaults is not None else ()
    arguments = rule.arguments if rule.arguments is not None else ()
    return len(defaults) >= len(arguments)


@app.route("/test")
def test():
    return 'test'

@app.route("/test1")
def test1():
    return 'test1'

@app.route("/test2")
def test2():
    return 'test2'

@app.errorhandler(404)
def handle_errors(e: int):
    links = []
    for rule in app.url_map.iter_rules():
        if "GET" in rule.methods and has_no_empty_params(rule):
            url = url_for(rule.endpoint, **(rule.defaults or {}))
            links.append(url)
    return '<br>'.join(links)


if __name__ == '__main__':
    app.run(debug=True)
