fn main() {
    let mut a = 0;
    let mut b = 1;

    println!("Fibonacci Series:");
    for _ in 0..10 { 
        println!("{}", a);
        let temp = a + b;
        a = b;
        b = temp;
    }
}
