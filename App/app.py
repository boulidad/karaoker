from flask import Flask
from flask_restplus import Api, Resource, fields
from werkzeug.contrib.fixers import ProxyFix
#import events

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)
api = Api(app, version='1.0', title='Karaoker API',
    description='A base of Karaoker API',
)



######################
# events - Start 
######################

eventns = api.namespace('events', description='Events')

event = api.model('Evnet', {
    'id': fields.Integer(readonly=True, description='The event unique identifier'),
    'name': fields.String(required=True, description='The event name')
})



class EventDAO(object):
    def __init__(self):
        self.counter = 0
        self.events = []

    def get(self, id):
        for event in self.events:
            if event['id'] == id:
                return event
        api.abort(404, "Event {} doesn't exist".format(id))

    def create(self, data):
        event = data
        event['id'] = self.counter = self.counter + 1
        self.events.append(event)
        return event

    def update(self, id, data):
        event = self.get(id)
        event.update(data)
        return event

    def delete(self, id):
        event = self.get(id)
        self.events.remove(todo)



EVENTDAO = EventDAO()
EVENTDAO.create({'name': 'Michals Birthday'})
EVENTDAO.create({'name': 'Holocost memorial day'})
EVENTDAO.create({'name': 'my Karaoke party'})


@eventns.route('/events')
class Events(Resource):

    # Shows a list of all songqueue, and lets you POST to add new tasks
    @eventns.doc('list of events')
    @eventns.marshal_list_with(event)
    def get(self):
        ## List all tasks
        return EVENTDAO.event

    @eventns.doc('create event')
    @eventns.expect(event)
    @eventns.marshal_with(event, code=201)
    def post(self):
        # Create a new task
        return EVENTDAO.create(api.payload), 201


@eventns.route('/events/<int:id>')
@eventns.response(404, 'event not found')
@eventns.param('id', 'The event identifier')

class Event(Resource):
    #Show a single todo item and lets you delete them
    @eventns.doc('get events')
    @eventns.marshal_with(event)
    def get(self, id):
        #Fetch a given resource
        return EVENTDAO.get(id)

    @eventns.doc('delete_event')
    @eventns.response(204, 'event deleted')
    def delete(self, id):
        #Delete a task given its identifier
        EVENTDAO.delete(id)
        return '', 204

    @eventns.expect(event)
    @eventns.marshal_with(event)
    def put(self, id):
        #Update a task given its identifier
        return EVENTDAO.update(id, api.payload)

######################
# events - End
######################

##############################
#. Song - Start 
##############################

songsns = api.namespace('songs', description='songs with lyrics and chords')

song = api.model('Song', {
    'id': fields.Integer(readonly=True, description='The event unique identifier'),
    'name': fields.String(required=True, description='The event name'),
    'url': fields.String(required=True, description='url from which we extract the song'),
    'lyrics': fields.String(required=False, description='extracted lyrics of the song'),
    'chords': fields.String(required=False, description='extracted lyricchords of the song'),
    'approved': fields.String(required=True, description='was the song approved by the MC/admin')
})



class SongDAO(object):
    def __init__(self):
        self.counter = 0
        self.songs = []

    def get(self, id):
        for song in self.songs:
            if song['id'] == id:
                return song
        api.abort(404, "song {} doesn't exist".format(id))

    def create(self, data):
        song = data
        song['id'] = self.counter = self.counter + 1
        self.songs.append(song)
        return song

    def update(self, id, data):
        song = self.get(id)
        song.update(data)
        return song

    def delete(self, id):
        song = self.get(id)
        self.songs.remove(song)



SONGDAO = SongDAO()
SONGDAO.create({'name': 'נתתי לה חיי','url':'www.google.com','approved':False})
SONGDAO.create({'name': 'hey jude','url':'www.google.com','approved':True,'lyrics':'<div class="i4J0ge"><div class="NFQFxe siXlze yp1CPe mod" data-attrid="kc:/music/recording_cluster:lyrics" data-md="113" style="clear:none"><!--m--><div data-hveid="CAcQAA" data-ved="2ahUKEwiGzK7B5fPnAhURCpQKHQBFAKMQsEwwAXoECAcQAA"><div class="uHNKed"><div class="Oh5wg"><div class="PZPZlf" data-lyricid="Lyricfind002-1417911"><div jsname="Vinbg" class="bbVIQb"><div jsname="U8S5sf" class="ujudUb"><span jsname="YS01Ge">Hey Jude, don\'t make it bad</span><br><span jsname="YS01Ge">Take a sad song and make it better</span><br><span jsname="YS01Ge">Remember to let her into your heart</span><br><span jsname="YS01Ge">Then you can start to make it better</span></div><div jsname="U8S5sf" class="ujudUb"><span jsname="YS01Ge">Hey Jude, don\'t be afraid</span><br><span jsname="YS01Ge">You were made to go out and get her</span><br><span jsname="YS01Ge">The minute you let her under your skin</span><br><span jsname="YS01Ge">Then you begin to make it better</span></div><div jsname="U8S5sf" class="ujudUb"><span jsname="YS01Ge">And anytime you feel the pain</span><br><span jsname="YS01Ge">Hey Jude, refrain</span><br><span jsname="YS01Ge">Don\'t carry the world upon your shoulders</span><br><span jsname="YS01Ge">For well you know that it\'s a fool</span><br><span jsname="YS01Ge">Who plays it cool</span><br><span jsname="YS01Ge">By making his world a little colder</span><br><span jsname="YS01Ge">Na-na-na, na, na</span><br><span jsname="YS01Ge">Na-na-na, na</span></div><div jsname="U8S5sf" class="ujudUb"><span jsname="YS01Ge">Hey Jude, don\'t let me down</span><br><span jsname="YS01Ge">You have found her, now go and get her (let it out and let it in)</span><br><span jsname="YS01Ge">Remember to let her into your heart (hey Jude)</span><br><span jsname="YS01Ge">Then you can start to make it better</span></div><div jsname="U8S5sf" class="ujudUb WRZytc OULBYb"><span jsname="YS01Ge">So let it out and let it in</span><br><span jsname="YS01Ge">Hey Jude, begin</span><br><span jsname="YS01Ge">You\'re waiting for someone to perform with</span><br><span jsname="YS01Ge">And don\'t you know that it\'s</span><span>… </span></div></div><div jsname="WbKHeb" class="bbVIQb"><div jsname="U8S5sf" class="ujudUb u7wWjf" data-mh="-1"><span jsname="YS01Ge">So let it out and let it in</span><br><span jsname="YS01Ge">Hey Jude, begin</span><br><span jsname="YS01Ge">You\'re waiting for someone to perform with</span><br><span jsname="YS01Ge">And don\'t you know that it\'s just you</span><br><span jsname="YS01Ge">Hey Jude, you\'ll do</span><br><span jsname="YS01Ge">The movement you need is on your shoulder</span><br><span jsname="YS01Ge">Na-na-na, na, na</span><br><span jsname="YS01Ge">Na-na-na, na, yeah</span></div><div jsname="U8S5sf" class="ujudUb xpdxpnd" data-mh="-1" aria-hidden="true"><span jsname="YS01Ge">Hey Jude, don\'t make it bad</span><br><span jsname="YS01Ge">Take a sad song and make it better</span><br><span jsname="YS01Ge">Remember to let her under your skin</span><br><span jsname="YS01Ge">Then you\'ll begin to make it better</span><br><span jsname="YS01Ge">Better better better better better, ah!</span></div><div jsname="U8S5sf" class="ujudUb WRZytc xpdxpnd" data-mh="-1" aria-hidden="true"><span jsname="YS01Ge">Na, na, na, na-na-na na (yeah! Yeah, yeah, yeah, yeah, yeah, yeah)</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude (Jude Jude, Judy Judy Judy Judy, ow wow!)</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na (my, my, my)</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude (Jude, Jude, Jude, Jude, Jude)</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na (yeah, yeah, yeah)</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude (yeah, you know you can make it, Jude, Jude, you\'re not gonna break it)</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na (don\'t make it bad, Jude, take a sad song and make it better)</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude (oh Jude, Jude, hey Jude, wa!)</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na (oh Jude)</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude (hey, hey, hey, hey)</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na (hey, hey)</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude (now, Jude, Jude, Jude, Jude, Jude)</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na (Jude, yeah, yeah, yeah, yeah)</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude (na-na-na-na-na-na-na-na-na)</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na (yeah, make it, Jude)</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude (yeah yeah yeah yeah yeah! Yeah! Yeah! Yeah! Yeah!)</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na (yeah, yeah yeah, yeah! Yeah! Yeah!)</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span><br><span jsname="YS01Ge">Na, na, na, na-na-na na</span><br><span jsname="YS01Ge">Na-na-na na, hey Jude</span></div></div></div><div class="j04ED">Source:&nbsp;<a href="https://www.lyricfind.com/" data-ved="2ahUKEwiGzK7B5fPnAhURCpQKHQBFAKMQ5s4FKAAwAXoECAcQAQ" ping="/url?sa=t&amp;source=web&amp;rct=j&amp;url=https://www.lyricfind.com/&amp;ved=2ahUKEwiGzK7B5fPnAhURCpQKHQBFAKMQ5s4FKAAwAXoECAcQAQ">LyricFind</a></div><div class="xpdxpnd PZPZlf" data-lyricid="Lyricfind002-1417911" data-mh="-1" data-ved="2ahUKEwiGzK7B5fPnAhURCpQKHQBFAKMQycMBKAEwAXoECAcQAg" aria-hidden="true"><div class="auw0zb">Songwriters: John Lennon /  Paul McCartney</div><div class="auw0zb">Hey Jude lyrics © Sony/ATV Music Publishing LLC</div></div></div></div></div><!--n--></div></div>',
                'chords':'    D                   A           A7                   D<br>Hey Jude, don’t make it bad, take a sad song and make it better<br>  G                           D                    A       A7      D<br>Remember to let her into your heart, then you can start to make it better<br> <br>    D               A               A7                 D<br>Hey Jude, don’t be afraid, you were made to go out and get her <br>    G                             D                A      A7      D<br>The minute you let her under your skin, then you begin to make it better<br> <br>[Chorus]<br> <br>D7                       G         Bm      Em           G         A7              D<br>And anytime you feel the pain, hey Jude, refrain, don’t carry the world upon your shoulders<br>D7                            G        Bm       Em      G          A7             D<br>For well you know that it\'s a fool who plays it cool by making his world a little colder<br> <br>[Interlude]<br> <br>D        D7    A7<br>Da da da da da da da da<br> <br>[Verse]<br> <br>    D                  A              A7                    D<br>Hey Jude, don’t let me down, you have found her, now go and get her<br>  G                           D                   A        A7      D<br>Remember to let her into your heart, then you can start to make it better<br> <br>[Chorus]<br> <br>D7                       G       Bm      Em          G           A7            D<br>So let it out and let it in, hey Jude, begin, you\'re waiting for someone to perform with<br>D7                                G        Bm           Em      G            A7              D<br>And don’t you know that it\'s just you, hey Jude, you\'ll do, the movement you need is on your shoulders<br> <br>[Interlude]<br> <br>D        D7    A7<br>Da da da da da da da da<br> <br>[Verse]<br> <br>    D                   A           A7                   D<br>Hey Jude, don’t make it bad, take a sad song and make it better<br>  G                            D                A      A7      D<br>Remember to let her under your skin, then you begin to make it better<br> <br>[Outro]<br> <br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude<br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude<br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude<br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude<br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude<br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude<br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude<br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude<br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude<br>D        C           G                D<br>Na na na na na na na na na na na, hey Jude . . . . . <br> <br>* Alternates:<br> <br>Capo V<br> <br>D  = C<br>A  = G<br>A7 = G7<br>D7 = C7<br>G  = F<br>Em = Dm<br>C  = Bb<br> <br>open<br> <br>D  = F<br>A  = C<br>A7 = C7<br>D7 = F7<br>G  = Bb<br>Em = Gm<br>C  = Eb','url':'https://tabs.ultimate-guitar.com/tab/the-beatles/hey-jude-chords-1061739'})
SONGDAO.create({'name': 'who let the dogs our','url':'www.google.com','approved':False})


@songsns.route('/songs')
class Songs(Resource):

    # Shows a list of all songqueue, and lets you POST to add new tasks
    @songsns.doc('list of events')
    @songsns.marshal_list_with(event)
    def get(self):
        ## List all tasks
        return SONGDAO.songs

    @songsns.doc('create event')
    @songsns.expect(song)
    @songsns.marshal_with(song, code=201)
    def post(self):
        # Create a new task
        return SONGDAO.create(api.payload), 201


@songsns.route('/songs/<int:id>')
@songsns.response(404, 'event not found')
@songsns.param('id', 'The event identifier')

class Song(Resource):
    #Show a single todo item and lets you delete them
    @songsns.doc('get events')
    @songsns.marshal_with(song)
    def get(self, id):
        #Fetch a given resource
        return SONGDAO.get(id)

    @songsns.doc('delete_song')
    @songsns.response(204, 'song deleted')
    def delete(self, id):
        #Delete a task given its identifier
        SONGDAO.delete(id)
        return '', 204

    @songsns.expect(song)
    @songsns.marshal_with(song)
    def put(self, id):
        #Update a task given its identifier
        return SONGDAO.update(id, api.payload)


##############################
#. Song - Emd 
##############################




##############################
#. songqueue. Start
##############################
songqueuens = api.namespace('songqueue', description='manage songs queue')

songqueue = api.model('SongInQueue', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'Singer': fields.String(required=True, description='name of Singer'),
    'songId': fields.Integer(required=True, description='ID of the song in songs')
    })


class QueueDAO(object):
    def __init__(self):
        self.counter = 0
        self.songqueue = []

    def get(self, id):
        for song in self.songqueue:
            if song['id'] == id:
                return song
        api.abort(404, "queue {} doesn't exist".format(id))

    def create(self, data):
        song = data
        song['id'] = self.counter = self.counter + 1
        self.songqueue.append(song)
        return song

    def update(self, id, data):
        song = self.get(id)
        tosongdo.update(data)
        return song

    def delete(self, id):
        song = self.get(id)
        self.songqueue.remove(song)


QDAO = QueueDAO()
QDAO.create({'Singer': 'Meir','songId':1})
QDAO.create({'Singer': 'Shai','songId':3})
QDAO.create({'Singer': 'Yael','songId':2})


@songqueuens.route('/todo')
class TodoList(Resource):
    '''Shows a list of all songqueue, and lets you POST to add new tasks'''
    @songqueuens.doc('list_songqueue')
    @songqueuens.marshal_list_with(songqueue)
    def get(self):
        '''List all tasks'''
        return QDAO.songqueue

    @songqueuens.doc('create_todo')
    @songqueuens.expect(songqueue)
    @songqueuens.marshal_with(songqueue, code=201)
    def post(self):
        '''Create a new task'''
        return QDAO.create(api.payload), 201


@songqueuens.route('/todo/<int:id>')
@songqueuens.response(404, 'Todo not found')
@songqueuens.param('id', 'The task identifier')
class Todo(Resource):
    '''Show a single todo item and lets you delete them'''
    @songqueuens.doc('get_todo')
    @songqueuens.marshal_with(songqueue)
    def get(self, id):
        '''Fetch a given resource'''
        return QDAO.get(id)

    @songqueuens.doc('delete_songqueue')
    @songqueuens.response(204, 'songqueue deleted')
    def delete(self, id):
        '''Delete a task given its identifier'''
        QDAO.delete(id)
        return '', 204

    @songqueuens.expect(songqueue)
    @songqueuens.marshal_with(songqueue)
    def put(self, id):
        '''Update a task given its identifier'''
        return QDAO.update(id, api.payload)

##############################
#. songqueue. End
##############################


################################################    


if __name__ == '__main__':
    app.run(debug=True)
