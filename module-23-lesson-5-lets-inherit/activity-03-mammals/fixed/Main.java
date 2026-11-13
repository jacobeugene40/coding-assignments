//this activity is mainly to explain Hierarchical inheritance
// Working version: obj.hum() is called on a Human object instead of a Lion.
//parent class
class Mammals{
	void mam(){
		System.out.println("Inside Mammals Class");
		}
}
//child class
class Lion extends Mammals{
	void roar(){
		System.out.println("Inside Lion class ");
		}
}
//child
class Human extends Mammals{
	void hum(){
		System.out.println("Inside Human");
		}
}

class Main{
	public static void main(String args[]){
	Lion obj=new Lion();
	obj.roar();
	obj.mam();
	Human person=new Human();//hum() needs a Human object
	person.hum();
	person.mam();
	}
}
