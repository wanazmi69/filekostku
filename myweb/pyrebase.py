from crypt import methods
import pyrebase


def _init_(self, config):
    config = {
        "apiKey": "AIzaSyCCW6ZzVbpfJy12HA-BsGOtC2teUx0LzTs",
        "authDomain": "kost-malindo.firebaseapp.com",
        "databaseURL": "https://kost-malindo-default-rtdb.asia-southeast1.firebasedatabase.app",
        "projectId": "kost-malindo",
        "storageBucket": "kost-malindo.appspot.com",
        "messagingSenderId": "857163534034",
        "appId": "1:857163534034:web:5774d0581591ab11d4670b",
        "measurementId": "G-JCVNJRESMD",
    }
    self.api_key = config
    
    firebase = pyrebase.initialize_app(self.api_key)
    _authen = firebase.auth()
    
    
def login(request):
    if request == "POST":
        _init_._authen.create_user_with_email_and_password(email, password)