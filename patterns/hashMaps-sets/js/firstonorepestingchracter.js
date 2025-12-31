// Given a string, find the first non-repeating character.
// If none exists, return null.
// Time: O(n)
// Pattern: Frequency + second scan


function NonRepeating(str){

    let repeat =  new Map();

    for(let ch of str){
        repeat.set(ch,(repeat.get(ch)||0)+1)

    }

    for (let ch of str){
        if(repeat.get(ch) ===1){
            return ch;
        }
    }

    return null;
}

console.log(NonRepeating("programmer")) 