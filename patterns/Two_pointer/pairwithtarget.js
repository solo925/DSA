// Given a sorted array of integers, return true if there exists a pair that adds up to a target.
// opposite ends(pattern)

function PairWithTsrget(nums,target){
    let left = 0
    let right = nums.length-1
    
    while (left < right){
        let sum = nums[left] + nums[right]
        if(sum === target) return true;
        if(sum < target ){
            left++
        }
        right--;
    }

    return false;
}