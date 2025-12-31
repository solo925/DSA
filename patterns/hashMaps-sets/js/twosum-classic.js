// Given an array of integers and a target, return true if any two numbers add up to the target.


function TwoSum(array,target){

    let seen = new Set();
     for (let num in array){
        if(seen.has(target-num)) return true;
        seen.add(num);
     }

 

    return false;
}