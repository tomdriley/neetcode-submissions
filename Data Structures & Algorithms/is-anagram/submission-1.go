import "slices"

func isAnagram(s string, t string) bool {
    if len(s) != len(t) {
        return false
    }

    sChars := []rune(s)
    tChars := []rune(t)

    slices.Sort(sChars)
    slices.Sort(tChars)

    for i := range sChars {
        if (sChars[i] != tChars[i]) {
            return false
        }
    }

    return true
}
