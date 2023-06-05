from flask import Flask, jsonify, abort, make_response
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
