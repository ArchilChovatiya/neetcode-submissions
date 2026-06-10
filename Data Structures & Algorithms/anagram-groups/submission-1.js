class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        const results = {}
        for (let s of strs){
            const anag = new Array(26).fill(0);
            for( let i in s){
                anag[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
            }
            if (results[anag.toString()]==null){
                results[anag.toString()]=[]
            }
            results[anag.toString()].push(s)
        } 
        const final_result=[]
        for (let key in results){
            final_result.push(results[key])
        }
        return final_result
    }
}
