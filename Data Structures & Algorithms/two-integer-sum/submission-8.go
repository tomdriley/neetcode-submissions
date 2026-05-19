func twoSum(nums []int, target int) []int {
    numIdx := make(map[int]int)

    for i, num := range nums {
        numIdx[num] = i
    }

    for i, num := range nums {
        j, exists := numIdx[target - num]
        if i != j && exists {
            return []int{i,j}
        }
    }
    return nil
}
