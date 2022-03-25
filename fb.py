import pyrebase

config = {
  "apiKey": "AIzaSyA2TCq7KKE8hD_p8hfJo1yEAIE7QLovlt4",
  "authDomain": "babycare-7a592.firebaseapp.com",
  "databaseURL": "https://babycare-7a592-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "babycare-7a592",
  "storageBucket": "babycare-7a592.appspot.com",
  "messagingSenderId": "566603872652",
  "appId": "1:566603872652:web:205236a0dba59514bffea9",
  "measurementId": "G-QC5980E8BZ"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
