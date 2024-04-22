use rand::{thread_rng, Rng}; 
fn main() {
    let mut rng = thread_rng();
    let n = rng.gen_range(1..11); 
    println!("Starting Collatz sequence for: {}", n);
    print_collatz_sequence(n);
}

fn print_collatz_sequence(mut n: i32) {
    while n != 1 {
        println!("{}", n);
        n = if n % 2 == 0 {
            n / 2
        } else {
            3 * n + 1
        };
    }
    println!("1"); // La séquence se termine toujours par 1
}
