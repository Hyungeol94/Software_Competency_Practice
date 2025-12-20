//https://leetcode.com/problems/delete-columns-to-make-sorted/?envType=daily-question&envId=2025-12-20
//944. Delete Columns to Make Sorted

/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    const n = strs.length
    const m = strs[0].length
    let count = 0

    for (let i = 0; i < m; i++) { 
        let prev = "a".charCodeAt(0);
        let is_sorted = true;
        for (let j = 0; j < n; j++) { 
            const c = strs[j].charCodeAt(i)
            if (prev > c) {
                is_sorted = false;
                break;
            }
            prev = c
        }
        if (!is_sorted) {
            count++;
        }
    }

    return count
};