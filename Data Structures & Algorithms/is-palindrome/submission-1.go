func isPalindrome(s string) bool {
    canonical := []rune{}
    for _, sRune := range s {
        if (sRune <= 'z' && sRune >= 'a') || (sRune <= '9' && sRune >= '0') {
            canonical = append(canonical, sRune)
        } else if sRune <= 'Z' && sRune >= 'A' {
            canonical = append(canonical, sRune - 'A' + 'a')
        }
    }

    for i, sRune := range canonical {
        pair := canonical[len(canonical) - 1 - i]
        if (sRune != pair) {
            return false
        }
    }
    return true
}
