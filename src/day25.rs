use std::collections::HashMap;

#[derive(Copy, Clone)]
enum State {
    A,
    B,
    C,
    D,
    E,
    F,
}

fn main() {
    let mut tape: HashMap<i32, bool> = HashMap::new();
    let mut cursor = 0;
    let mut state = State::A;

    for _ in 0..12964419 {
        let value = tape.entry(cursor).or_insert(false);

        state = match (state, *value) {
            (State::A, false) => { *value =  true; cursor += 1; State::B },
            (State::A,  true) => { *value = false; cursor += 1; State::F },
            (State::B, false) => { *value = false; cursor -= 1; State::B },
            (State::B,  true) => { *value =  true; cursor -= 1; State::C },
            (State::C, false) => { *value =  true; cursor -= 1; State::D },
            (State::C,  true) => { *value = false; cursor += 1; State::C },
            (State::D, false) => { *value =  true; cursor -= 1; State::E },
            (State::D,  true) => { *value =  true; cursor += 1; State::A },
            (State::E, false) => { *value =  true; cursor -= 1; State::F },
            (State::E,  true) => { *value = false; cursor -= 1; State::D },
            (State::F, false) => { *value =  true; cursor += 1; State::A },
            (State::F,  true) => { *value = false; cursor -= 1; State::E },
        }
    }

    let sum: u32 = tape.values().map(|&v| v as u32).sum();
    println!("{}", sum);
}
