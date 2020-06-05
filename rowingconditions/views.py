from rowingconditions import server

@server.route('/')
def index():
    return 'Hello Flask app'