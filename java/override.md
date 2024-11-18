- to_string
~~~java
public class Employee{
	public String name;
	public String department;
	public String level;
	public int basicAnnualSalary;
	
	public String toString() {
		return "(name=" + name + ", department=" + department + ", level=" + level + ", basicAnnualSalary=" + basicAnnualSalary +")" ;
	}
}
~~~