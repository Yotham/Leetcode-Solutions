use std::collections::HashSet;
impl Solution {
    pub fn contains_duplicate(nums: Vec<i32>) -> bool {
        let mut check = HashSet::new();
        for &num in &nums{
            if !check.insert(num){
                return true;
            }
        }

        false
    }
}