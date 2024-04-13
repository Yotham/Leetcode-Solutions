use std::collections::HashMap;

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {      
        fn sort_string(s:&str) -> String{
            let mut c: Vec<char> = s.chars().collect();
            c.sort_unstable();
            c.into_iter().collect()
        }
        let mut storage = HashMap::new();
        for word in &strs{
            let word = sort_string(&word[..]);
            storage.insert(word,Vec::<String>::new());
        }
        for word in &strs{
            let sorted = sort_string(&word[..]);
            if storage.contains_key(&sorted){
                if let Some(vec) = storage.get_mut(&sorted){
                    vec.push(word.to_string());
                }
            }
        }
        let mut ret = Vec::new();
        for (key,value) in storage.into_iter(){
            ret.push(value);
        }
        ret
        
    }
}