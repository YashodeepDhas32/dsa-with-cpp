function linearSearch(arr, key) {
  for(let i=0; i<arr.length; i++) {
    if(arr[i] === key) {
      return i;
    }
  }          
  return -1;
} 
// compares all the elements with the key until matching is found
// either returns the index of element if found in array or return -1 if not found
console.log(linearSearch([10, 9, 8, 2, 12, 14], 2));