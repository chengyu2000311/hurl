from app import app


@app.route("/query-match-none")
def query_match_none():
    return "Hello World!"
