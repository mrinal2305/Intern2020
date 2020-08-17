const freq_arr = (arr) => {
    var out = new Array(3).fill(0); // Initializing an array of constant length with 0
    arr.forEach(element => {
        if(element < 1) out[0]++;
        else if(element >=1 && element <2) out[1]++;
        else out[2]++;
    });
    console.log(out)
}

var arr = [1,2,3,4,5,1,2,2,3]
freq_arr(arr);