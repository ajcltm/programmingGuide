- DecimalFormat
~~~java
import java.text.*;

class DecimalFormatEx {
    public void main (String[] args) {
        double number = 1234567.89;
        pattern1 = "0"; // 1234568
        pattern2 = "0.0"; // 1234567.9
        pattern3 = "0000000000.0000"; // 0001234567.8900
        pattern4 = "##########.####"; // 1234567.89
        pattern5 = "#,###.##"; // 1,234,567.89
        pattern6 = "#.#%"; // 12345678%
        pattern7 = "'#'#,###"; // #1,234,568

        DecimalFormat df = new DecimalFormat(patter1);
        String result = df.format(number);
    }
}
~~~