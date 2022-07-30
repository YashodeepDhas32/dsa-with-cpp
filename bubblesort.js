function bubbleSort(arr) {
    // passes
    for(let i=0; i<arr.length-1; i++) {
        // comparisons
        for(let j=0; j<arr.length-1; j++) {
            if(arr[j] > arr[j+1]) {
                [arr[j], arr[j+1]] = [arr[j+1], arr[j]]
            }
        }
    }
}
var arr = [10, 2, 8, 21, 4];
bubbleSort(arr);
for(let i=0; i<arr.length; i++) {
    console.log(arr[i]);
}