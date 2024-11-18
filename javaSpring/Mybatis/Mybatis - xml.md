
- interface
~~~java
package org.hgtech.guidearchiveweb.dao;  
  
import org.apache.ibatis.annotations.Mapper;  
import org.hgtech.guidearchiveweb.domain.FileVO;  
  
import java.util.List;  
  
@Mapper  
public interface FileInfoDao {  
  
    void insert(FileVO fileVO);  
  
    List<FileVO> selectAll();  
  
    FileVO selectLast();  
  
    List<FileVO> selectByForeignId(int foreignId);  
  
    FileVO selectById(int id);  
  
    void delete(int id);  
  
    void update(FileVO fileVO);  
}
~~~
-  namespace 설정
~~~xml
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE mapper PUBLIC "//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >  
<mapper namespace="org.hgtech.guidearchiveweb.mapper.MapperClass">
 (생략)
</mapper>
~~~

- insert
~~~xml
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE mapper PUBLIC "//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >  
<mapper namespace="org.hgtech.guidearchiveweb.mapper.MapperClass">  
    <insert id="insert">  
        insert into tbl_file (foreign_id, file_name, file_path, file_type) values (#{foreign_id}, #{file_name}, #{file_path}, #{file_type})  
    </insert> 
</mapper>
~~~

- select
~~~xml
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE mapper PUBLIC "//mybatis.org/DTD Mapper 3.0//EN" "http://mybatis.org/dtd/mybatis-3-mapper.dtd" >  

반환 타입이 List<VO>인 경우에도 resultType을 VO로 설정함

<mapper namespace="org.hgtech.guidearchiveweb.mapper.MapperClass">
    <select id="selectAll" resultType="org.hgtech.guidearchiveweb.domain.FileVO">  
        select * from tbl_file  
    </select>  
  
    <select id="selectLast" resultType="org.hgtech.guidearchiveweb.domain.FileVO">  
        select * from tbl_file order by id desc limit 1  
    </select>  
  
    <select id="selectByForeignId" resultType="org.hgtech.guidearchiveweb.domain.FileVO">  
        select * from tbl_file where foreign_id = #{foreign_id}  
    </select>  
  
    <select id="selectById" resultType="org.hgtech.guidearchiveweb.domain.FileVO">  
        select * from tbl_file where id = #{id}  
    </select>  
</mapper>
~~~

- delete
~~~xml
<delete id="delete">  
    delete from tbl_file where id = #{id}  
</delete>  
~~~

- update
~~~xml
<update id="update">  
    update tbl_file set foreign_id = #{foreign_id}, file_name=#{file_name}, file_path = #{file_path}, file_type = #{file_type} where id=#{id}  
</update>
~~~