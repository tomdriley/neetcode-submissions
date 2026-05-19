func hasDuplicate(nums []int) bool {
    seen := make(map[int]bool)

    for _, num := range nums {
        _, exists := seen[num]
        if exists {
            return true
        }
        seen[num] = true
    }

    return false
}
