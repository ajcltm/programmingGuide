
### OneToMany
---
#### mapper.xml 선언

- 어떤 repository에 관한 mapper 인지 선언
~~~xml
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE mapper PUBLIC "//mybatis.org/DTD Mapper 3.0//EN"  http://mybatis.org/dtd/mybatis-3-mapper.dtd" >  
<mapper namespace="org.hgtech.blog.repository.BlogboardimgRepository">  
</mapper>
~~~

#### SQL join문과 java class method 연결

- id : java repository class의 어떤 method에 관한 sql 쿼리인지 선언
- resultMap : SQL 쿼리 결과 출력되는 테이블을 어떤 xml resultMap태그와 연결할 것인지 선언
---
~~~xml
<select id="selectAll" resultMap="blogResultMap">  
    select  
        b.bid as b_bid, 
        b.regdate as regdate,
        b.moddate as moddate,
        b.title as title,
        b.subtitle as subtitle,
        b.content as content,
        i.iid as iid,
        i.bid as i_bid,
        i.imgname as imgname,
        i.imgpath as imgpath,
        i.imgtype as imgtype
    from tbl_blogboard as b
    left join tbl_blogimg as i 
    on b.bid = i.bid
    order by b.bid asc , iid asc
</select>
~~~

#### SQL 결과 테이블과 java 데이터 객체와 연결
- resultMap 태그 활용
- id : resultMap 이름 선언
- type : mapper 결과 반환하는 java 데이터 객체 선언
- id 태그 : id가 동일한 SQL row는 하나의 java 데이터 인스턴스로 인식
- property : 맵핑되는 java 데이터 객체의 속성 지정
- column : 맵핑되는 SQL 결과 테이블의 컬럼 지정
- collection : java 데이터 객체 중 List<>에 해당하는 속성에 대해 기술
- ofType : List 안에 해당하는 java 데이터 객체 지정

~~~xml
<resultMap id="blogResultMap" type="org.hgtech.blog.domain.BlogboardimgVO">  
    <id property="bid" column="b_bid"/>  
    <result property="regdate" column="regdate"/>  
    <result property="moddate" column="moddate"/>  
    <result property="title" column="title"/>  
    <result property="subtitle" column="subtitle"/>  
    <result property="content" column="content"/>  
    <collection property="imglist" ofType="org.hgtech.blog.domain.BlogimgVO">  
        <id property="iid" column="iid"/>  
        <result property="bid" column="i_bid"/>  
        <result property="imgname" column="imgname"/>  
        <result property="imgpath" column="imgpath"/>  
        <result property="imgtype" column="imgtype"/>  
    </collection>
</resultMap>
~~~

#### mapper 전체 코드
~~~xml
<?xml version="1.0" encoding="UTF-8"?>  
<!DOCTYPE mapper PUBLIC "//mybatis.org/DTD Mapper 3.0//EN"  http://mybatis.org/dtd/mybatis-3-mapper.dtd" >  
<mapper namespace="org.hgtech.blog.repository.BlogboardimgRepository">
	<resultMap id="blogResultMap" type="org.hgtech.blog.domain.BlogboardimgVO">  
	    <id property="bid" column="b_bid"/>  
	    <result property="regdate" column="regdate"/>  
	    <result property="moddate" column="moddate"/>  
	    <result property="title" column="title"/>  
	    <result property="subtitle" column="subtitle"/>  
	    <result property="content" column="content"/>  
	    <collection property="imglist" ofType="org.hgtech.blog.domain.BlogimgVO">  
	        <id property="iid" column="iid"/>  
	        <result property="bid" column="i_bid"/>  
	        <result property="imgname" column="imgname"/>  
	        <result property="imgpath" column="imgpath"/>  
	        <result property="imgtype" column="imgtype"/>  
	    </collection>
	</resultMap>

	<select id="selectAll" resultMap="blogResultMap">  
	    select  
	        b.bid as b_bid, 
	        b.regdate as regdate,
	        b.moddate as moddate,
	        b.title as title,
	        b.subtitle as subtitle,
	        b.content as content,
	        i.iid as iid,
	        i.bid as i_bid,
	        i.imgname as imgname,
	        i.imgpath as imgpath,
	        i.imgtype as imgtype
	    from tbl_blogboard as b
	    left join tbl_blogimg as i 
	    on b.bid = i.bid
	    order by b.bid asc , iid asc
	</select>
</mapper>
~~~


