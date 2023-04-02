use rand::Rng;
use std::io;

fn create_secret_number() -> String {
    let mut rng = rand::thread_rng();
    let x = rng.gen_range(0..=999);
    x.to_string()
}

fn get_guess() -> u32 {
    let mut input_text = String::new();

    while input_text.len() != 3 {
        input_text.clear();
        println!("Please enter 3 digit number");
        io::stdin()
            .read_line(&mut input_text)
            .expect("failed to read input");
        input_text = input_text.trim().to_string();
    }

   input_text.trim().parse::<u32>().unwrap()

}

fn process(guess: String, secret_number: &String) -> Result<String, String> {
    let mut res = Vec::new();
    if guess == *secret_number {
        return Ok("Correct".to_string());
    } else {
        let zipped = guess.chars().zip(secret_number.chars());
        let secret_vec: Vec<String> = secret_number.chars().map(|c| c.to_string()).collect();
        for (a_val, b_val) in zipped {
            if a_val == b_val {
                res.push("Fermi")
            } else if secret_vec.contains(&a_val.to_string()) {
                res.push("Pico")
            }else {
                res.push("Bagles")
            }
        }
        return Err(res.join(" ").to_string());
    }
}

fn main() {
    let secret_number = create_secret_number();
    println!("{} sec", secret_number);
    let mut i = 0;
    loop {
        if i == 10 {
            println!("Game Over");
            break;
        }
        let guess_result = get_guess();

        let process_result = process(guess_result.to_string(), &secret_number);

        match process_result {
            Err(msg) => println!("{}", msg),
            Ok(..) => {
                println!("Correct!");
                break;
            }
        }
        i += 1;
    }
}
