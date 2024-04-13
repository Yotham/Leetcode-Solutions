use std::collections::HashMap;
impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        //let ret = Vec::new();
        let mut hash = HashMap::new();
        let mut counter = 0;
        for &num in &nums{
            if hash.contains_key(&num){
                let value = hash.get(&num).unwrap();
                let ret: Vec<i32> = vec![*value,counter];
                return ret;
            }
            let sol = target - num;
            hash.insert(sol,counter);
            counter +=1;
        }

        Vec::new()
    }
}