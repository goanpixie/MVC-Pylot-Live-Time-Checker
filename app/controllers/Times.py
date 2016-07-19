"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
from time import strftime

class Times(Controller):
    def __init__(self, action):
        super(Times, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.
        """
        self.load_model('WelcomeModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        print "get this route running"
        time = strftime("%b %d, %Y") 
        hrSec= strftime("%H:%M %p")
        return self.load_view('index.html',time=time,hrSec=hrSec)

