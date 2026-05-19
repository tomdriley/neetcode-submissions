func twoSum(nums []int, target int) []int {
    numIdx := make(map[int]int)

    for j, num := range nums {
        i, exists := numIdx[target - num]
        if exists {
            return []int{i,j}
        }
        numIdx[num] = j
    }
    return nil
}
