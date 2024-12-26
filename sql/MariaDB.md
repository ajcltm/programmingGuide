Windows 환경에서 MariaDB를 설치 및 실행하고, 콘솔에서 사용할 수 있는 기능들과 계정 관리 관련 내용을 포함한 사용법을 설명드리겠습니다.

---

## **MariaDB 설치**

1. [MariaDB 다운로드 페이지](https://mariadb.org/download/)에서 Windows 버전을 다운로드합니다.
2. 설치 중 아래 설정을 주의 깊게 설정합니다.
    - **서비스 이름**: 기본값 유지 또는 필요시 변경.
    - **루트 계정 비밀번호**: 반드시 설정.
    - **포트 번호**: 기본값(3306) 사용 또는 필요시 변경.
3. 설치 후 `Command Prompt(명령 프롬프트)` 또는 `PowerShell`을 통해 MariaDB를 사용할 준비를 합니다.

---

## **MariaDB 서비스 시작/중지**

MariaDB가 Windows 서비스로 설치되었으므로 명령 프롬프트에서 다음 명령어를 사용할 수 있습니다.

### 서비스 시작:

```cmd
net start MariaDB
```

### 서비스 중지:

```cmd
net stop MariaDB
```

---

## **MariaDB 접속**

MariaDB에 접속하려면 명령 프롬프트를 열고 다음 명령어를 실행합니다:

```cmd
mysql -u root -p
```

- `-u root`: `root` 계정으로 로그인.
- `-p`: 비밀번호 입력을 요구.

비밀번호를 입력하면 MariaDB 셸로 들어갑니다.

---

## **계정 관리**

MariaDB에서는 계정 생성, 권한 부여 및 수정이 중요합니다.

### 새 계정 생성:

```sql
CREATE USER 'new_user'@'localhost' IDENTIFIED BY 'password123';
```

- `'new_user'`: 계정 이름.
- `'localhost'`: 이 계정은 로컬 접속만 허용. 원격 접속을 허용하려면 `'%@%'` 사용.
- `'password123'`: 계정 비밀번호.

### 계정에 권한 부여:

```sql
GRANT ALL PRIVILEGES ON *.* TO 'new_user'@'localhost';
```

- `ALL PRIVILEGES`: 모든 권한 부여.
- `*.*`: 모든 데이터베이스와 모든 테이블에 대한 권한.

변경 사항 적용:

```sql
FLUSH PRIVILEGES;
```

### 계정 비밀번호 변경:

```sql
ALTER USER 'new_user'@'localhost' IDENTIFIED BY 'new_password123';
```

### 계정 삭제:

```sql
DROP USER 'new_user'@'localhost';
```

---

## **데이터베이스 및 테이블 작업**

### 데이터베이스 생성:

```sql
CREATE DATABASE my_database;
```

### 데이터베이스 선택:

```sql
USE my_database;
```

### 테이블 생성:

```sql
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    role VARCHAR(100),
    salary DECIMAL(10, 2)
);
```

### 데이터 삽입:

```sql
INSERT INTO employees (name, role, salary) 
VALUES ('Alice', 'Manager', 75000.00);
```

### 데이터 조회:

```sql
SELECT * FROM employees;
```

### 데이터 업데이트:

```sql
UPDATE users SET name = 'Jane Doe' WHERE id = 1;
```


### 데이터 삭제:

```sql
DELETE FROM users WHERE id = 1;
```

### 테이블 삭제:

```sql
DROP TABLE users;
```


---

## **Windows 명령 프롬프트 팁**

### 현재 MariaDB 상태 확인:

MariaDB가 실행 중인지 확인하려면:

```cmd
sc query MariaDB
```

### 특정 명령어 실행 후 MariaDB 종료:

명령 프롬프트에서 단일 명령 실행 후 종료하려면:

```cmd
mysql -u root -p -e "SHOW DATABASES;"
```

### 스크립트 실행:

SQL 파일을 실행하려면:

```cmd
mysql -u root -p < script.sql
```

---

## **원격 접속 허용**

MariaDB를 원격에서 접속 가능하게 설정하려면 아래 과정을 수행합니다:

1. **MariaDB 설정 파일 수정**  
설정 파일 경로: `C:\Program Files\MariaDB xx.x\data\my.ini`  
`bind-address` 항목을 찾고 `0.0.0.0`으로 변경:

```ini
bind-address=0.0.0.0
```

1. **방화벽 설정**  
Windows 방화벽에서 MariaDB 포트(기본값 3306)를 허용합니다:

```cmd
netsh advfirewall firewall add rule name="MariaDB" dir=in action=allow protocol=TCP localport=3306
```

3. **원격 사용자 생성 및 권한 부여**  

MariaDB 셸에서 실행:
```sql
CREATE USER 'remote_user'@'%' IDENTIFIED BY 'password123';
GRANT ALL PRIVILEGES ON *.* TO 'remote_user'@'%' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

---

이제 Windows 환경에서 MariaDB를 효율적으로 사용할 수 있습니다. 추가적으로 원하시는 기능이 있으면 알려주세요!