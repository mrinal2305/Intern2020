import * as firebase from 'firebase';
import "firebase/firebase-storage";

var firebaseConfig = {
    apiKey: "AIzaSyC8rYPRvmeE8nuBIK8fum_BwcxYdD0KVig",
    authDomain: "tourist-bot-hilapp.firebaseapp.com",
    databaseURL: "https://tourist-bot-hilapp.firebaseio.com",
    projectId: "tourist-bot-hilapp",
    storageBucket: "tourist-bot-hilapp.appspot.com",
    messagingSenderId: "903028130242",
    appId: "1:903028130242:web:43780bc4bdf541d95e565b"
  };
  
export const App = firebase.initializeApp(firebaseConfig);
storage = App.storage('gs://express-b0920.appspot.com/');       

// return this.storage.ref('profilePhotos').child(key).getDownloadURL(); // Accessing a image url