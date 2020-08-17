// Anger Frequency -------------
const freq = (sentimentData,type) => {
    var out = new Array(10).fill(0); // Initializing an array of constant length with 0
    sentimentData.forEach(elem => {
      if(type == 0) element = elem.value.joy;
      else if(type == 1) element = elem.value.sad;
      else if(type == 2) element = elem.value.anger;
      else element = elem.value.fear;

      if (element < 10) out[0]++;
      else if (element >= 10 && element < 20) out[1]++;
      else if (element >= 20 && element < 30) out[2]++;
      else if (element >= 30 && element < 40) out[3]++;
      else if (element >= 40 && element < 50) out[4]++;
      else if (element >= 50 && element < 60) out[5]++;
      else if (element >= 60 && element < 70) out[6]++;
      else if (element >= 70 && element < 80) out[7]++;
      else if (element >= 80 && element < 90) out[8]++;
      else out[9]++;
    })
    var out = {
      "<10": out[0],
      "10-20": out[1],
      "20-30": out[2],
      "30-40": out[3],
      "40-50": out[4],
      "50-60": out[5],
      "60-70": out[6],
      "70-80": out[7],
      "80-90": out[8],
      "90-100": out[9],
    }
    return out;
}

// exporting each fn
exports.freqTen = freq; 
