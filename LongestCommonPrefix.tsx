function longestCommonPrefix(strs: string[]): string {
    
    var longestPrefix = ""
    var shortestWord = 1000
    var currentChar = ""
    
    for (var word of strs) {
        if (word.length < shortestWord) {
            shortestWord = word.length
        }
    }
    
    
    for (var i = 0; i < shortestWord; i++) {
        currentChar = ""
        
        var notTheSame = false 
        
        // For each word 
        for (var word of strs) {
            if (currentChar == "") {
                currentChar = word[i]
            }

            if (currentChar != word[i]) {
                notTheSame = true
            }
        }
        if (!notTheSame) {
            longestPrefix += currentChar
        } else {
            break
        }
    }

    return longestPrefix
        
};
