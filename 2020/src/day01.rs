use itertools::Itertools;
use std::fs;

fn main() {
    let file = fs::read_to_string("2020/day01.txt").unwrap();

    for num in 2..4 {
        let result: u32 = file
            .lines()
            .map(|s| s.parse().unwrap())
            .combinations(num)
            .filter_map(|entries| {
                if entries.iter().sum::<u32>() == 2020 {
                    Some(entries.iter().product())
                } else {
                    None
                }
            })
            .next()
            .unwrap();
        println!("{}", result);
    }
}
