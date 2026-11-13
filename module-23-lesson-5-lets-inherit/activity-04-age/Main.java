class Main {

    int age;
    Main(int age){
        age = age;          // BUG on purpose: assigns the parameter to itself, so the field stays 0
		//this.age = age;   // swap the lines: "this.age" is the object's field, "age" is the parameter
    }

    public static void main(String[] args) {
        Main obj = new Main(24);
        System.out.println("obj.age = " + obj.age);
    }
}
