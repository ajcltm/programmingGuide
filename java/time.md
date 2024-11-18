- Calendar
    - 현재 날짜
        ~~~java
        # import java.util.*; 
        Calendar today = Calendar.getInstance();
        int year = today.get(Calendar.YEAR);
        int month = today.get(Calendar.MONTH);
        int date = today.get(Calendar.DATE); # 0~11
        int hour = today.get(Calendar.HOUR_OF_DAY); 
        int minute = today.get(Calendar.MINUTE);
        int second = today.get(Calendar.SECOND);
        int millisecond = today.get(Calendar.MILLISECOND);
        ~~~