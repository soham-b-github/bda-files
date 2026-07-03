class vehicle{
  void car(){
    System.out.println("This vehicle has 4 tyres!");
  }
  
  void cycle(){
    System.out.println("This vehicle has 2 tyres!");
  }
}

class inheritance-multilevel-practice extends vehicle{
  pubilc static void main(String args[]){
    herohonda ob = new herohonda();
    ob.car();
    ob.cycle();
  }
}
