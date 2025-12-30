// simple findduplicates
// Given an array of integers,
//  return true if any value appears more than once, 
//  otherwise return false.

function FindDuplicates(array){
    const value_appeared =  new Set()

    for (let num of array){
        if (value_appeared.has(num)) {
            return true;
        }
        value_appeared.add(num);

    }
    return false;
}


console.log(FindDuplicates([1,2,3,1])) // true
console.log(FindDuplicates([1,2,3,4])) // false
console.log(FindDuplicates([1,1,1,3,3,4,3,2,4,2])) // true