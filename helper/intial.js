// importing functions
"use strict";
// using import ,export of node
var freq = require('./frequencyDetail.js')
var freq10 = require('./frequency10.js')
// Clean cache when node is not working aur update it
var admin = require("firebase-admin");

var serviceAccount = require("./key.json");

admin.initializeApp({
  credential: admin.credential.cert(serviceAccount),
  databaseURL: "https://tourist-bot-hilapp.firebaseio.com"
});

var cloudDB = admin.firestore(); //Our database
//-------------
const fetchData = async () => {
  let sentimentData = [];
  try {
    await cloudDB.collection("sentFinal").get().then((querySnapshot) => {
      querySnapshot.forEach((doc) => {
        sentimentData.push(
          {
            date: doc.id,
            value: doc.data()
          }
        );
      });
      // For sub,polar only random interval
      var subject = freq.freqSubjectivity(sentimentData); // Range 0-0.39
      var polar   = freq.freqPolarity(sentimentData) // Range 0 - 0.15
      // freq mean random interval for emotions
      var anger = freq.freqAnger(sentimentData); // Range 0 - 16
      var sad   = freq.freqSad(sentimentData); // Range 0-40
      var joy   = freq.freqJoy(sentimentData);  //Range 0-55
      var fear  = freq.freqFear(sentimentData) //Range 0-14
      // freq10 mean interval 10 for emotions
      var joy10 = freq10.freqTen(sentimentData,0);
      var sad10 = freq10.freqTen(sentimentData,1);
      var anger10 = freq10.freqTen(sentimentData,2);
      var fear10  = freq10.freqTen(sentimentData,3);
      // Output the data
      console.log(fear10)
    });
    // setData(sentimentData);
  } catch (error) {
    console.log(error);
  }
}

fetchData()
