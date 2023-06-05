from flask import Flask, jsonify, abort, make_response, request, json
from event import Event
from online_event import OnlineEvent

ev_online = OnlineEvent('Live of Python')
ev_online2 = OnlineEvent('Live of Javascript')
ev = Event('Class of Python','São Paulo')
events = [ev, ev_online, ev_online2]



app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Flask configurated with success!</h1>'

@app.route('/api/events/')
def event_list():
    dict_events = []
    for ev in events:
        dict_events.append(ev.__dict__)
    return jsonify(dict_events)

@app.route('/api/events/', methods=['POST'])
def create_event(): 
    data = json.loads(request.data)
    name = data.get('name')
    local = data.get('local')

    if not name:
        abort(400, "'Name' is required")
    if local:
        event = Event(name=name, local=local)
    else:
        event = Event(name=name)
    events.append(event)
    return {
        'id': event.id,
        'url': f'/api/events/{event.id}/'
    }

@app.errorhandler(400)
def not_found(error):
    data_error = {'Error': str(error)}
    return (jsonify(data_error), 400)

@app.errorhandler(404)
def not_found(error):
    data_error = {'Error': str(error)}
    return (jsonify(data_error), 404)

@app.route('/api/events/<int:id>/')
def event_detail(id):
    for ev in events:
        if ev.id == id:
            return jsonify(ev.__dict__)
    abort(404, 'Id not found')

@app.route('/api/events/<int:id>/', methods=['DELETE'])
def event_delete(id):
    for ev in events:
        if ev.id == id:
            events.remove(ev)
            return jsonify(id=id)
    abort(404, 'Id not found')

