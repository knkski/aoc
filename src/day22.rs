use std::fs::File;
use std::io::Read;
use std::collections::HashMap;


fn infect(ref mut grid: &mut HashMap<(i32, i32), u8>, bursts: u32, smart: bool) -> u32 {
    let mut position = (0, 0);
    let mut direction = 0;
    let mut total = 0;

    for _ in 0..bursts {
        let node = *grid.get(&position).unwrap_or(&0) as u32;

        total += match (node, smart) {
            (0, false) => 1,
            (2,  true) => 1,
            (_,     _) => 0,
        };

        grid.insert(position, match (node, smart) {
            (0,  true) => 2,
            (0, false) => 1,
            (1,  true) => 3,
            (1, false) => 0,
            (2,     _) => 1,
            (3,     _) => 0,
                     _ => unreachable!(),
        });

        direction += match node {
            0 => -1,
            1 =>  1,
            2 =>  0,
            3 =>  2,
            _ => unreachable!(),
        };

        direction %= 4;

        // Rust `%` operator does remainder, which doesn't work with negative numbers
        // in the way that we need.
        direction = if direction >= 0 { direction } else { direction + 4 };

        position = match (direction, position) {
            (0, (x, y)) => (x - 1, y    ),
            (1, (x, y)) => (x    , y + 1),
            (2, (x, y)) => (x + 1, y    ),
            (3, (x, y)) => (x    , y - 1),
                      _ => unreachable!(),
        };
    }

    total
}


fn main() {
    let mut f = File::open("day22.txt").expect("Couldn't read file!");
    let mut contents = String::new();
    f.read_to_string(&mut contents).expect("Couldn't read file!");

    let mut grid: HashMap<(i32, i32), u8> = HashMap::new();

    contents.split_whitespace().enumerate().for_each(|(i, row)| {
        row.chars().enumerate().for_each(|(j, item)| {

            grid.insert((-12 + (i as i32), -12 + (j as i32)), match item {
                '#' => 1,
                '.' => 0,
                _   => unreachable!(),
            });
        })
    });

    println!("{}", infect(&mut grid.clone(), 10000, false));
    println!("{}", infect(&mut grid.clone(), 10000000, true));
}
