impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        let mut sset = Vec::new();
        let mut tset = Vec::new();
        for c in s.chars(){
            sset.push(c);
        }
        for c in t.chars(){
            tset.push(c);
        }
        sset.sort();
        tset.sort();
        let ret = sset == tset;
        ret
    }
}