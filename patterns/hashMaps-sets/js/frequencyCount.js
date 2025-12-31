// Given a string, return an object showing how many times each character appears.

function FrequencyCount(str) {
    const freq = new Map()
    for(let ch of str){
        freq.set(ch,(freq.get(ch) || 0)+1)
    }

    return Object.fromEntries(freq)

}