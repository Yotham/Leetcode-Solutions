impl Solution {
    pub fn is_palindrome(s: String) -> bool {
        let mut storage = Vec::new();
        for letter in s.chars(){
            if letter.is_alphabetic() | letter.is_digit(10){
                let letter = letter.to_lowercase().next().unwrap();
                storage.push(letter);
            }
        }

        let check: Vec<char> = storage.iter().cloned().rev().collect();
        check == storage
    }
}