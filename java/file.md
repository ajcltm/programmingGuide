- File
~~~java
import java.io.File;

public class FileEx2 {
	public static void main(String[] args) {
		
		// 실제로는 없는 경로를 file로 설정
		File file = new File("C:\\Users\\rltpr\\Desktop\\T-Story");
		File file2 = new File("C:\\Users\\rltpr\\Desktop\\T-Story2\\06-11\\Blog");
		// 경로가 없기 때문에 당연히 else문을 실행
		if(file.exists()) {
			System.out.println("파일 or 경로가 존재합니다.");
		} else {
			System.out.println("파일 or 경로가 없습니다.");
		}
		// file에 해당하는 경로를 생성합니다.
		// mkdir은 경로를 하나씩 생성한다
		file.mkdir();
		// mkdirs는 여러개의 경로를
		// 한번에 설정하고자 할때 사용한다. 
		file2.mkdirs();
		
	}
}
~~~