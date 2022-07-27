binarySearch = (arr, key) => {
    let start = 0;
    let end = arr.length - 1;
    while(start <= end) {
			let mid = parseInt((end + start)/2);
			if(arr[mid] === key) {
				return mid;
			}
			else if(arr[mid] > key) {
				end = mid - 1;
			}
			else {	
				start = mid + 1; 
			}
    }
    return -1;
}

// binary search is efficient form of search algorithm where key is searched
// on basis of comparing key with middle element of array reducing size by half 
// in each newer iteration if key is not found in previous iteration

console.log(binarySearch([10, 20, 30, 40, 50, 60], 60));