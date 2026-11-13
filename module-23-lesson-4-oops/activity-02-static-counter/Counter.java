//run this program using javac Counter.java - > java Counter
class Counter {
	//uncomment the below lines to know the importance of static keyword

	int number=10;
	//static int number=10;
	// To try the static version: comment out "int number=10;" above and uncomment the static line.
	// Without static: each object has its own copy -> prints 11, 11, 11
	// With static:    all objects share one copy   -> prints 13, 13, 13

	void increment(){
		number=number+1;
	}
	public static void main(String[] args) {
		Counter obj1=new Counter();
		Counter obj2=new Counter();
		Counter obj3=new Counter();
		//Guess the answer
		obj1.increment();
		obj2.increment();
		obj3.increment();

		//to check your answers (the lesson had these lines commented out)
		System.out.println(obj1.number);
		System.out.println(obj2.number);
		System.out.println(obj3.number);
	}
}
