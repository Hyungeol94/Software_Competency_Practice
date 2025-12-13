//https://leetcode.com/problems/coupon-code-validator/?envType=daily-question&envId=2025-12-13
//3606. Coupon Code Validator

/**
 * @param {string[]} code
 * @param {string[]} businessLine
 * @param {boolean[]} isActive
 * @return {string[]}
 */

var validateCoupons = function(code, businessLine, isActive) {
    var compareFn = (a, b) => {
        if (businessLine[a] != businessLine[b]) { 
            return businessLine[a].charCodeAt(0) - businessLine[b].charCodeAt(0)
        } else { 
            return code[a] < code[b] ? -1 : 1
        }
    }

    const validCodeIndices = []
    const regExp = /^[\w]+$/g
    const validCategories = ["electronics", "grocery", "pharmacy", "restaurant"]
    for (const [i, couponCode] of code.entries()) { 
        if (!couponCode.match(regExp)) { 
            continue
        }
        if (!validCategories.includes(businessLine[i])) { 
            continue
        }
        if (!isActive[i]) { 
            continue
        }
        validCodeIndices.push(i)
    }

    validCodeIndices.sort(compareFn)
    return validCodeIndices.map((index) => code[index])
};