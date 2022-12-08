T-SQL 即 Transact-SQL，是 SQL 在 Microsoft SQL Server 上的增强版，它是用来让应用程序与 SQL Server 沟通的主要语言。

T-SQL 提供标准 SQL 的 DDL 和 DML 功能，加上延伸的函数、系统预存程序以及程式设计结构(例如 IF 和 WHILE)让程式设计更有弹性。

> 在SSMS总，选中词语如 `CREATE DATABASE`，再按 `F1`。 会打开该主题（`CEATE DATABASE`）的 SQL Server 联机帮助文档。

# 语法规范

## 语法约定

| 约定            | 用于                                                         |
| :-------------- | :----------------------------------------------------------- |
| 大写            | Transact-SQL 关键字。                                        |
| *斜体*          | 用户提供的 Transact-SQL 语法的参数。                         |
| **粗体**        | 完全按显示原样键入数据库名称、表名称、列名、索引名称、存储过程、实用工具、数据类型名称和文本。 |
| 下划线          | 指示当语句中省略了包含带下划线的值的子句时应用的默认值。     |
| \| （垂直条）   | 分隔括号或大括号中的语法项。 只能使用其中一项。              |
| `[ ]`（方括号） | 可选语法项。 不要键入方括号。                                |
| {}（大括号）    | 必选语法项。 不要键入大括号。                                |
| [ ...*n*]       | 指示前面的项可以重复 *n* 次。 匹配项由逗号分隔。             |
| [...n ]         | 指示前面的项可以重复 *n* 次。 每一项由空格分隔。             |
| ;               | Transact-SQL 语句终止符。 虽然此版本的 SQL Server 中大部分语句都不需要分号，但今后发布的版本需要分号。 |
| `<label> ::=`   | 语法块的名称。 使用此约定，可以对能在一条语句中的多个位置使用的过长语法段或语法单元进行分组和标记。 可使用语法块的各个位置用括在尖括号内的标签指明：`<label>`。  集是表达式的集合，例如 `<grouping set>`；列表是集的集合，例如` <composite element list>`。 |

## 书写规范





# 语言元素

## 常规

### EXECUTE

```mssql
-- Syntax for SQL Server 2019

Execute a stored procedure or function  
[ { EXEC | EXECUTE } ]  
    {   
      [ @return_status = ]  
      { module_name [ ;number ] | @module_name_var }   
        [ [ @parameter = ] { value   
                           | @variable [ OUTPUT ]   
                           | [ DEFAULT ]   
                           }  
        ]  
      [ ,...n ]  
      [ WITH <execute_option> [ ,...n ] ]  
    }  
[;]  

Execute a character string  
{ EXEC | EXECUTE }   
    ( { @string_variable | [ N ]'tsql_string' } [ + ...n ] )  
    [ AS { LOGIN | USER } = ' name ' ]  
[;]  

Execute a pass-through command against a linked server  
{ EXEC | EXECUTE }  
    ( { @string_variable | [ N ] 'command_string [ ? ]' } [ + ...n ]  
        [ { , { value | @variable [ OUTPUT ] } } [ ...n ] ]  
    )   
    [ AS { LOGIN | USER } = ' name ' ]  
    [ AT linked_server_name ]  
    [ AT DATA_SOURCE data_source_name ]  
[;]  

<execute_option>::=  
{  
        RECOMPILE   
    | { RESULT SETS UNDEFINED }   
    | { RESULT SETS NONE }   
    | { RESULT SETS ( <result_sets_definition> [,...n ] ) }  
}   

<result_sets_definition> ::=   
{  
    (  
         { column_name   
           data_type   
         [ COLLATE collation_name ]   
         [ NULL | NOT NULL ] }  
         [,...n ]  
    )  
    | AS OBJECT   
        [ db_name . [ schema_name ] . | schema_name . ]   
        {table_name | view_name | table_valued_function_name }  
    | AS TYPE [ schema_name.]table_type_name  
    | AS FOR XML   
}  
```



* CHECKPOINT

```sql
CHECKPOINT [ checkpoint_duration ]
```



## 控制流



## 游标



## 表达式

## 运算符

## 变量

Transact-SQL 局部变量是可以保存单个特定类型数据值的对象。 

> * 一些 Transact-SQL 系统函数的名称以两个 at 符号 (@@) 开头。 尽管在旧版 SQL Server 中，@@ 函数称为全局变量，但 @@ 函数不是变量，不具有等同于变量的行为。 @@函数是系统函数，语法遵循函数规则。
> * 不能在视图中使用变量。
> * 事务回滚不影响对变量所做的更改。

### 语法

#### 声明变量

指定一个名称。 名称的首字符必须为一个 @。

```mssql
DECLARE @LastName NVARCHAR(30), @FirstName NVARCHAR(20), @StateProvince NCHAR(2);
```

#### 设置变量

```mssql
-- Set their values.
SET @FirstNameVariable = N'Amy';
SET @PostalCodeVariable = N'BA5 3HX';

-- Use them in the WHERE clause of a SELECT statement.
SELECT LastName, FirstName, JobTitle, City, StateProvinceName, CountryRegionName
FROM HumanResources.vEmployee
WHERE FirstName = @FirstNameVariable
   OR PostalCode = @PostalCodeVariable;
GO
```



#### 在脚本中应用变量

- 作为计数器计算循环执行的次数或控制循环执行的次数。
- 保存数据值以供控制流语句测试。
- 保存存储过程返回代码要返回的数据值或函数返回值。

```mssql
-- Create the table.
CREATE TABLE TestTable (cola INT, colb CHAR(3));
GO
SET NOCOUNT ON;
GO
-- Declare the variable to be used.
DECLARE @MyCounter INT;

-- Initialize the variable.
SET @MyCounter = 0;

-- Test the variable to see if the loop is finished.
WHILE (@MyCounter < 26)
BEGIN;
   -- Insert a row into the table.
   INSERT INTO TestTable VALUES
       -- Use the variable to provide the integer value
       -- for cola. Also use it to generate a unique letter
       -- for each row. Use the ASCII function to get the
       -- integer value of 'a'. Add @MyCounter. Use CHAR to
       -- convert the sum back to the character @MyCounter
       -- characters after 'a'.
       (@MyCounter,
        CHAR( ( @MyCounter + ASCII('a') ) )
       );
   -- Increment the variable to count this iteration
   -- of the loop.
   SET @MyCounter = @MyCounter + 1;
END;
GO
SET NOCOUNT OFF;
GO
-- View the data.
SELECT cola, colb
FROM TestTable;
GO
DROP TABLE TestTable;
GO
```



## 事务



# 数据类型

* [日期和时间](https://docs.microsoft.com/zh-cn/sql/t-sql/data-types/date-and-time-types)
  * DATE，精度为天，0001-01-01 到 9999-12-31
  * DATETIME，3.33毫秒精度，1753 年 1 月 1 日到 9999 年 12 月 31 日
  * DATETIME2，DATETIME升级版，100纳秒精度
  * DATETIMEOFFSET，100纳秒的精度，范围公元1年1月1日到公元9999年12月31日

* 精确数值
  * 即整数，MONEY数据类型就是BIGINT小数点前移四位

* 近似数
  * 即非常大但不要求极度精确的数，往往以浮点数的形式保存。
* 字符串
  * 非UNICODE字符串
    * CHAR、VARCHAR、VARCHAR(MAX)、TEXT
    * 前两者最大能存储8000个字符，后两者最多能存储$2^{31}$个字符
  * UNICODE字符串
    * 在非UNICODE字符串类型前加上N表示Unicode
    * 比相对应的非UNICODE字符串类型存储的字符要少一半。
* 二进制字符串
  * BINARY、VARBINARY、VARBINARY(MAX)、IMG
  * 相对于字符串而言，单位从字符变成了字节（对ASCII码而言是一样的）

## 其他数据类型

### HierarchyID

树形层次结构（Hierarchy）经常出现在有结构的数据中，T-SQL新增数据类型HierarchyID， 其长度可变，用于存储层次结构中的路径。HierarchyID表示的层次结构是树形的，由应用程序来生成和分配 HierarchyID的值，建立父子节点之间的关系。

HierarchyID数据类型支持深度优先顺序的比较，对于两个HierarchyID值 a和b，a<b意味着，在深度优先遍历时，先遍历到a，后遍历到b，也就是说，值越小，越接近根节点。

对Hierarchy数据类型创建索引，是按照深度优先，先左后右的顺序来排序的。左和右是根据节点的值来判断的，在同一深度上，值较小的节点在父节点的左边。

### 空间几何

平面空间数据类型 **geometry** 在 SQL Server 中作为公共语言运行时 (CLR) 数据类型实现。 此类型表示欧几里得（平面）坐标系中的数据。

SQL Server 支持 **geometry** 空间数据类型的一组方法。 这些方法包括开放地理空间信息联盟 (OGC) 标准和对该标准的一组 Microsoft 扩展所定义的 **geometry** 方法。



除此之外还有UNIQUEIDENTIFIER、CUROSR、XML、空间地理等其他数据类型

## 示例

### 数据类型测试

```sql
SELECT   
     CAST('2007-05-08 12:35:29. 1234567 +12:15' AS time(7)) AS 'time'   
    ,CAST('2007-05-08 12:35:29. 1234567 +12:15' AS date) AS 'date'   
    ,CAST('2007-05-08 12:35:29.123' AS smalldatetime) AS   
        'smalldatetime'   
    ,CAST('2007-05-08 12:35:29.123' AS datetime) AS 'datetime'   
    ,CAST('2007-05-08 12:35:29.1234567+12:15' AS datetime2(7)) AS   
        'datetime2'  
    ,CAST('2007-05-08 12:35:29.1234567 +12:15' AS datetimeoffset(7)) AS   
        'datetimeoffset'  
    ,CAST('2007-05-08 12:35:29.1234567+12:15' AS datetimeoffset(7)) AS  
        'datetimeoffset IS08601';  

```



```sql
DECLARE @datetimeoffset datetimeoffset(4) = '12-10-25 12:32:10 +01:00';  
DECLARE @date date= @datetimeoffset;  
SELECT @datetimeoffset AS '@datetimeoffset ', @date AS 'date';  
--Result  
@datetimeoffset                    @datetime2  
---------------------------------- ----------------------  
1912-10-25 12:24:32.1277 +10:00    1912-10-25 12:24:32.12  
  
--(1 row(s) affected)  
```



### 和ODBC对接



# 基础语句

## CREATE

可以通过create语句创建的对象很多很多，[参见MS官方文档](https://docs.microsoft.com/zh-cn/sql/t-sql/statements/create-aggregate-transact-sql)

常用的有Database，table等

### CRATE DATABASE

```mssql
CREATE DATABASE database_name
[ CONTAINMENT = { NONE | PARTIAL } ]
[ ON
      [ PRIMARY ] <filespec> [ ,...n ]
      [ , <filegroup> [ ,...n ] ]
      [ LOG ON <filespec> [ ,...n ] ]
]
[ COLLATE collation_name ]
[ WITH <option> [,...n ] ]
[;]
```

* `ON`显式指定用来存储数据库数据部分的磁盘文件
  * `PRIMARY`指定关联的 `<filespec>`列表定义主文件。如果没有指定`PRIMARY`，那么 `CREATE DATABASE `语句中列出的第一个文件将成为主文件。
  * `LOG ON `指定显式定义用来存储数据库日志的磁盘文件（日志文件），如果没有指定 `LOG ON`，将自动创建一个日志文件，其大小为该数据库的所有数据文件大小总和的 25% 或 512 KB，取两者之中的较大者。
* COLLATE collation_name 指定数据库的默认排序规则。 如果没有指定排序规则，则将 SQL Server 实例的默认排序规则分配为数据库的排序规则。

关于`filespec`和`filegroup`描述如下

```mssql
<filespec> ::=
{
(
    NAME = logical_file_name ,
    FILENAME = { 'os_file_name' | 'filestream_path' }
    [ , SIZE = size [ KB | MB | GB | TB ] ]
    [ , MAXSIZE = { max_size [ KB | MB | GB | TB ] | UNLIMITED } ]
    [ , FILEGROWTH = growth_increment [ KB | MB | GB | TB | % ] ]
)
}

<filegroup> ::=
{
FILEGROUP filegroup name [ [ CONTAINS FILESTREAM ] [ DEFAULT ] | CONTAINS MEMORY_OPTIMIZED_DATA ]
    <filespec> [ ,...n ]
}
```



其他可选项：

```mssql
<option> ::=
{
      FILESTREAM ( <filestream_option> [,...n ] )
    | DEFAULT_FULLTEXT_LANGUAGE = { lcid | language_name | language_alias }
    | DEFAULT_LANGUAGE = { lcid | language_name | language_alias }
    | NESTED_TRIGGERS = { OFF | ON }
    | TRANSFORM_NOISE_WORDS = { OFF | ON}
    | TWO_DIGIT_YEAR_CUTOFF = <two_digit_year_cutoff>
    | DB_CHAINING { OFF | ON }
    | TRUSTWORTHY { OFF | ON }
    | PERSISTENT_LOG_BUFFER=ON ( DIRECTORY_NAME='<Filepath to folder on DAX formatted volume>' )
}
```

### CRATE TABLE

```mssql
CREATE TABLE
    { database_name.schema_name.table_name | schema_name.table_name | table_name }
    [ AS FileTable ]
    ( {   <column_definition>
        | <computed_column_definition>
        | <column_set_definition>
        | [ <table_constraint> ] [ ,... n ]
        | [ <table_index> ] }
          [ ,...n ]
          [ PERIOD FOR SYSTEM_TIME ( system_start_time_column_name
             , system_end_time_column_name ) ]
      )
    [ ON { partition_scheme_name ( partition_column_name )
           | filegroup
           | "default" } ]
    [ TEXTIMAGE_ON { filegroup | "default" } ]
    [ FILESTREAM_ON { partition_scheme_name
           | filegroup
           | "default" } ]
    [ WITH ( <table_option> [ ,...n ] ) ]
[ ; ]
  

```

其中：

```mssql
<column_definition> ::=
column_name <data_type>
    [ FILESTREAM ]
    [ COLLATE collation_name ]
    [ SPARSE ]
    [ MASKED WITH ( FUNCTION = ' mask_function ') ]
    [ [ CONSTRAINT constraint_name ] DEFAULT constant_expression ]
    [ IDENTITY [ ( seed,increment ) ]
    [ NOT FOR REPLICATION ]
    [ GENERATED ALWAYS AS ROW { START | END } [ HIDDEN ] ]
    [ NULL | NOT NULL ]
    [ ROWGUIDCOL ]
    [ ENCRYPTED WITH
        ( COLUMN_ENCRYPTION_KEY = key_name ,
          ENCRYPTION_TYPE = { DETERMINISTIC | RANDOMIZED } ,
          ALGORITHM = 'AEAD_AES_256_CBC_HMAC_SHA_256'
        ) ]
    [ <column_constraint> [, ...n ] ]
    [ <column_index> ]
  
<data_type> ::=
[ type_schema_name . ] type_name
    [ ( precision [ , scale ] | max |
        [ { CONTENT | DOCUMENT } ] xml_schema_collection ) ]
  
<column_constraint> ::=
[ CONSTRAINT constraint_name ]
{     { PRIMARY KEY | UNIQUE }
        [ CLUSTERED | NONCLUSTERED ]
        [
            WITH FILLFACTOR = fillfactor
          | WITH ( < index_option > [ , ...n ] )
        ]
        [ ON { partition_scheme_name ( partition_column_name )
            | filegroup | "default" } ]
  
  | [ FOREIGN KEY ]
        REFERENCES [ schema_name . ] referenced_table_name [ ( ref_column ) ]
        [ ON DELETE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ ON UPDATE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ NOT FOR REPLICATION ]
  
  | CHECK [ NOT FOR REPLICATION ] ( logical_expression )
}
  
<column_index> ::=
 INDEX index_name [ CLUSTERED | NONCLUSTERED ]
    [ WITH ( <index_option> [ ,... n ] ) ]
    [ ON { partition_scheme_name (column_name )
         | filegroup_name
         | default
         }
    ]
    [ FILESTREAM_ON { filestream_filegroup_name | partition_scheme_name | "NULL" } ]
  
<computed_column_definition> ::=
column_name AS computed_column_expression
[ PERSISTED [ NOT NULL ] ]
[
    [ CONSTRAINT constraint_name ]
    { PRIMARY KEY | UNIQUE }
        [ CLUSTERED | NONCLUSTERED ]
        [
            WITH FILLFACTOR = fillfactor
          | WITH ( <index_option> [ , ...n ] )
        ]
        [ ON { partition_scheme_name ( partition_column_name )
        | filegroup | "default" } ]
  
    | [ FOREIGN KEY ]
        REFERENCES referenced_table_name [ ( ref_column ) ]
        [ ON DELETE { NO ACTION | CASCADE } ]
        [ ON UPDATE { NO ACTION } ]
        [ NOT FOR REPLICATION ]
  
    | CHECK [ NOT FOR REPLICATION ] ( logical_expression )
]
  
<column_set_definition> ::=
column_set_name XML COLUMN_SET FOR ALL_SPARSE_COLUMNS
  
< table_constraint > ::=
[ CONSTRAINT constraint_name ]
{
    { PRIMARY KEY | UNIQUE }
        [ CLUSTERED | NONCLUSTERED ]
        (column [ ASC | DESC ] [ ,...n ] )
        [
            WITH FILLFACTOR = fillfactor
           |WITH ( <index_option> [ , ...n ] )
        ]
        [ ON { partition_scheme_name (partition_column_name)
            | filegroup | "default" } ]
    | FOREIGN KEY
        ( column [ ,...n ] )
        REFERENCES referenced_table_name [ ( ref_column [ ,...n ] ) ]
        [ ON DELETE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ ON UPDATE { NO ACTION | CASCADE | SET NULL | SET DEFAULT } ]
        [ NOT FOR REPLICATION ]
    | CHECK [ NOT FOR REPLICATION ] ( logical_expression )

< table_index > ::=
{  
    {  
      INDEX index_name  [ UNIQUE ] [ CLUSTERED | NONCLUSTERED ]
         (column_name [ ASC | DESC ] [ ,... n ] )
    | INDEX index_name CLUSTERED COLUMNSTORE
    | INDEX index_name [ NONCLUSTERED ] COLUMNSTORE (column_name [ ,... n ] )
    }
    [ WITH ( <index_option> [ ,... n ] ) ]
    [ ON { partition_scheme_name (column_name )
         | filegroup_name
         | default
         }
    ]
    [ FILESTREAM_ON { filestream_filegroup_name | partition_scheme_name | "NULL" } ]
  
}

<table_option> ::=
{  
    [DATA_COMPRESSION = { NONE | ROW | PAGE }
      [ ON PARTITIONS ( { <partition_number_expression> | <range> }
      [ , ...n ] ) ]]
    [ FILETABLE_DIRECTORY = <directory_name> ]
    [ FILETABLE_COLLATE_FILENAME = { <collation_name> | database_default } ]
    [ FILETABLE_PRIMARY_KEY_CONSTRAINT_NAME = <constraint_name> ]
    [ FILETABLE_STREAMID_UNIQUE_CONSTRAINT_NAME = <constraint_name> ]
    [ FILETABLE_FULLPATH_UNIQUE_CONSTRAINT_NAME = <constraint_name> ]
    [ SYSTEM_VERSIONING = ON [ ( HISTORY_TABLE = schema_name . history_table_name
        [, DATA_CONSISTENCY_CHECK = { ON | OFF } ] ) ] ]
    [ REMOTE_DATA_ARCHIVE =
      {
          ON [ ( <table_stretch_options> [,...n] ) ]
        | OFF ( MIGRATION_STATE = PAUSED )
      }
    ]   
    [ DATA_DELETION = ON  
          {( 
             FILTER_COLUMN = column_name,   
             RETENTION_PERIOD = { INFINITE | number {DAY | DAYS | WEEK | WEEKS 
                              | MONTH | MONTHS | YEAR | YEARS }
        )}  
     ]
}
  
<table_stretch_options> ::=
{  
    [ FILTER_PREDICATE = { null | table_predicate_function } , ]
      MIGRATION_STATE = { OUTBOUND | INBOUND | PAUSED }
 }   
  
<index_option> ::=
{
    PAD_INDEX = { ON | OFF }
  | FILLFACTOR = fillfactor
  | IGNORE_DUP_KEY = { ON | OFF }
  | STATISTICS_NORECOMPUTE = { ON | OFF }
  | STATISTICS_INCREMENTAL = { ON | OFF }
  | ALLOW_ROW_LOCKS = { ON | OFF }
  | ALLOW_PAGE_LOCKS = { ON | OFF }
  | OPTIMIZE_FOR_SEQUENTIAL_KEY = { ON | OFF }
  | COMPRESSION_DELAY= {0 | delay [Minutes]}
  | DATA_COMPRESSION = { NONE | ROW | PAGE | COLUMNSTORE | COLUMNSTORE_ARCHIVE }
       [ ON PARTITIONS ( { <partition_number_expression> | <range> }
       [ , ...n ] ) ]
}
<range> ::=
<partition_number_expression> TO <partition_number_expression>
```





## ALTER

### ALTER TABLE

```mssql
ALTER TABLE { database_name.schema_name.table_name | schema_name.table_name | table_name }
{
    ALTER COLUMN column_name
    {
        [ type_schema_name. ] type_name
            [ (
                {
                   precision [ , scale ]
                 | max
                 | xml_schema_collection
                }
            ) ]
        [ COLLATE collation_name ]
        [ NULL | NOT NULL ] [ SPARSE ]
      | { ADD | DROP }
          { ROWGUIDCOL | PERSISTED | NOT FOR REPLICATION | SPARSE | HIDDEN }
      | { ADD | DROP } MASKED [ WITH ( FUNCTION = ' mask_function ') ]
    }
    [ WITH ( ONLINE = ON | OFF ) ]
    | [ WITH { CHECK | NOCHECK } ]
  
    | ADD
    {
        <column_definition>
      | <computed_column_definition>
      | <table_constraint>
      | <column_set_definition>
    } [ ,...n ]
      | [ system_start_time_column_name datetime2 GENERATED ALWAYS AS ROW START
                [ HIDDEN ] [ NOT NULL ] [ CONSTRAINT constraint_name ]
            DEFAULT constant_expression [WITH VALUES] ,
                system_end_time_column_name datetime2 GENERATED ALWAYS AS ROW END
                   [ HIDDEN ] [ NOT NULL ][ CONSTRAINT constraint_name ]
            DEFAULT constant_expression [WITH VALUES] ,
        ]
       PERIOD FOR SYSTEM_TIME ( system_start_time_column_name, system_end_time_column_name )
    | DROP
     [ {
         [ CONSTRAINT ][ IF EXISTS ]
         {
              constraint_name
              [ WITH
               ( <drop_clustered_constraint_option> [ ,...n ] )
              ]
          } [ ,...n ]
          | COLUMN [ IF EXISTS ]
          {
              column_name
          } [ ,...n ]
          | PERIOD FOR SYSTEM_TIME
     } [ ,...n ]
    | [ WITH { CHECK | NOCHECK } ] { CHECK | NOCHECK } CONSTRAINT
        { ALL | constraint_name [ ,...n ] }
  
    | { ENABLE | DISABLE } TRIGGER
        { ALL | trigger_name [ ,...n ] }
  
    | { ENABLE | DISABLE } CHANGE_TRACKING
        [ WITH ( TRACK_COLUMNS_UPDATED = { ON | OFF } ) ]
  
    | SWITCH [ PARTITION source_partition_number_expression ]
        TO target_table
        [ PARTITION target_partition_number_expression ]
        [ WITH ( <low_priority_lock_wait> ) ]

    | SET
        (
            [ FILESTREAM_ON =
                { partition_scheme_name | filegroup | "default" | "NULL" } ]
            | SYSTEM_VERSIONING =
                  {
                      OFF
                  | ON
                      [ ( HISTORY_TABLE = schema_name . history_table_name
                          [, DATA_CONSISTENCY_CHECK = { ON | OFF } ]
                          [, HISTORY_RETENTION_PERIOD =
                          {
                              INFINITE | number {DAY | DAYS | WEEK | WEEKS
                  | MONTH | MONTHS | YEAR | YEARS }
                          }
                          ]
                        )
                      ]
                  }
            | DATA_DELETION =  
                {
                      OFF 
                    | ON  
                        [(  [ FILTER_COLUMN = column_name ]   
                            [, RETENTION_PERIOD = { INFINITE | number {DAY | DAYS | WEEK | WEEKS 
                                    | MONTH | MONTHS | YEAR | YEARS }}]   
                        )]
                   }
    | REBUILD
      [ [PARTITION = ALL]
        [ WITH ( <rebuild_option> [ ,...n ] ) ]
      | [ PARTITION = partition_number
           [ WITH ( <single_partition_rebuild_option> [ ,...n ] ) ]
        ]
      ]
  
    | <table_option>
    | <filetable_option>
    | <stretch_configuration>
}
[ ; ]
  
```



## INSERT

```mssql
[ WITH <common_table_expression> [ ,...n ] ]  
INSERT   
{  
        [ TOP ( expression ) [ PERCENT ] ]   
        [ INTO ]   
        { <object> | rowset_function_limited   
          [ WITH ( <Table_Hint_Limited> [ ...n ] ) ]  
        }  
    {  
        [ ( column_list ) ]   
        [ <OUTPUT Clause> ]  
        { VALUES ( { DEFAULT | NULL | expression } [ ,...n ] ) [ ,...n     ]   
        | derived_table   
        | execute_statement  
        | <dml_table_source>  
        | DEFAULT VALUES   
        }  
    }  
}  
[;]  
  
<object> ::=  
{   
    [ server_name . database_name . schema_name .   
      | database_name .[ schema_name ] .   
      | schema_name .   
    ]  
  table_or_view_name  
}  
  
<dml_table_source> ::=  
    SELECT <select_list>  
    FROM ( <dml_statement_with_output_clause> )   
      [AS] table_alias [ ( column_alias [ ,...n ] ) ]  
    [ WHERE <search_condition> ]  
        [ OPTION ( <query_hint> [ ,...n ] ) ]  
```



### BULK INSERT

在 SQL Server 中以用户指定的格式将数据文件导入到数据库表或视图中

```mssql
BULK INSERT
   { database_name.schema_name.table_or_view_name | schema_name.table_or_view_name | table_or_view_name }
      FROM 'data_file'
     [ WITH
    (
   [ [ , ] BATCHSIZE = batch_size ]
   [ [ , ] CHECK_CONSTRAINTS ]
   [ [ , ] CODEPAGE = { 'ACP' | 'OEM' | 'RAW' | 'code_page' } ]
   [ [ , ] DATAFILETYPE =
      { 'char' | 'native'| 'widechar' | 'widenative' } ]
   [ [ , ] DATA_SOURCE = 'data_source_name' ]
   [ [ , ] ERRORFILE = 'file_name' ]
   [ [ , ] ERRORFILE_DATA_SOURCE = 'data_source_name' ]
   [ [ , ] FIRSTROW = first_row ]
   [ [ , ] FIRE_TRIGGERS ]
   [ [ , ] FORMATFILE_DATA_SOURCE = 'data_source_name' ]
   [ [ , ] KEEPIDENTITY ]
   [ [ , ] KEEPNULLS ]
   [ [ , ] KILOBYTES_PER_BATCH = kilobytes_per_batch ]
   [ [ , ] LASTROW = last_row ]
   [ [ , ] MAXERRORS = max_errors ]
   [ [ , ] ORDER ( { column [ ASC | DESC ] } [ ,...n ] ) ]
   [ [ , ] ROWS_PER_BATCH = rows_per_batch ]
   [ [ , ] ROWTERMINATOR = 'row_terminator' ]
   [ [ , ] TABLOCK ]

   -- input file format options
   [ [ , ] FORMAT = 'CSV' ]
   [ [ , ] FIELDQUOTE = 'quote_characters']
   [ [ , ] FORMATFILE = 'format_file_path' ]
   [ [ , ] FIELDTERMINATOR = 'field_terminator' ]
   [ [ , ] ROWTERMINATOR = 'row_terminator' ]
    )]
```



### GUI



## UPDATE

```mssql
-- Syntax for SQL Server and Azure SQL Database  

[ WITH <common_table_expression> [...n] ]  
UPDATE   
    [ TOP ( expression ) [ PERCENT ] ]   
    { { table_alias | <object> | rowset_function_limited   
         [ WITH ( <Table_Hint_Limited> [ ...n ] ) ]  
      }  
      | @table_variable      
    }  
    SET  
        { column_name = { expression | DEFAULT | NULL }  
          | { udt_column_name.{ { property_name = expression  
                                | field_name = expression }  
                                | method_name ( argument [ ,...n ] )  
                              }  
          }  
          | column_name { .WRITE ( expression , @Offset , @Length ) }  
          | @variable = expression  
          | @variable = column = expression  
          | column_name { += | -= | *= | /= | %= | &= | ^= | |= } expression  
          | @variable { += | -= | *= | /= | %= | &= | ^= | |= } expression  
          | @variable = column { += | -= | *= | /= | %= | &= | ^= | |= } expression  
        } [ ,...n ]   
  
    [ <OUTPUT Clause> ]  
    [ FROM{ <table_source> } [ ,...n ] ]   
    [ WHERE { <search_condition>   
            | { [ CURRENT OF   
                  { { [ GLOBAL ] cursor_name }   
                      | cursor_variable_name   
                  }   
                ]  
              }  
            }   
    ]   
    [ OPTION ( <query_hint> [ ,...n ] ) ]  
[ ; ]  
  
<object> ::=  
{   
    [ server_name . database_name . schema_name .   
    | database_name .[ schema_name ] .   
    | schema_name .  
    ]  
    table_or_view_name}  
```



# 查询和SELECT

select配得上单独一节

## SELECT子句



### 从已有数据创建新表

```mssql
select * into new_table from source_table [condition]
```



# 函数

## 聚合函数



## 分析函数





## 转换

CAST和CONVERT，将表达式由一种数据类型转换为另一种数据类型。

```sql
-- CAST Syntax:  
CAST ( expression AS data_type [ ( length ) ] )  
  
-- CONVERT Syntax:  
CONVERT ( data_type [ ( length ) ] , expression [ , style ] )
```







# 存储过程

## 系统存储过程

* 活动异地复制`sp_wait_for_database_copy_sync`
* 数据库引擎存储过程
  * `sp_help`
  * `sp_attach_db`
  * `sp_execute`
  * 等等
* 分布式查询存储过程
* 全文搜索存储过程
* 管理数据库存储过程





# SQL Server和T-SQL实战

## 安装SQL Server并连接Server

### Install Rules

![image-20201110202158766](C:\Users\Five\Desktop\note\img\image-20201110202158766.png)

选择版本，确认条款

### Feature Selection

![image-20201110202341475](C:\Users\Five\Desktop\note\img\image-20201110202341475.png)

关于这些Features的具体介绍，详见后文，可按需选择。

### Configuration

需要配置Instance、PolyBase、Java Install Location、Server、Database Engine、Analysis Services、Integration Services、Distributed Replay等信息。

![image-20201111125852043](C:\Users\Five\Desktop\note\img\image-20201111125852043.png)

![image-20201111130507082](C:\Users\Five\Desktop\note\img\image-20201111130507082.png)

除了Database Engine基本都是直接next了。

![image-20201111131912457](C:\Users\Five\Desktop\note\img\image-20201111131912457.png)

### 连接数据库

![image-20201111142735472](C:\Users\Five\Desktop\note\img\image-20201111142735472.png)

（Server Type如果是数据库应该选Database Engine）

这里的Server name好像指的是host，也就是Computer Name，而不是实例名称MSSQLSERVER。直接输localhost也可。

## 创建和管理数据库

```sql
CREATE DATABASE TestData  
GO
```

默认以`System Database`中的`model`数据库为模板，创建新的数据库。

```mssql
CREATE DATABASE database_name
[ CONTAINMENT = { NONE | PARTIAL } ]
[ ON
      [ PRIMARY ] <filespec> [ ,...n ]
      [ , <filegroup> [ ,...n ] ]
      [ LOG ON <filespec> [ ,...n ] ]
]
[ COLLATE collation_name ]
[ WITH <option> [,...n ] ]
[;]
```

### 移动数据库

#### 分离数据库

分离数据库是指将数据库从 SQL Server 实例中删除，但使数据库在其数据文件和事务日志文件中保持不变。 之后，就可以使用这些文件将数据库附加到任何 SQL Server实例，包括分离该数据库的服务器。

* 如果进行复制，数据库必须是未发布的
* 删除所有数据库快照，才能分离数据库
* 不可以分离系统数据库
* 无法分离可疑状态的数据库

```mssql
EXEC sp_detach_db 'DatabaseName', 'true';  
```



#### 附加数据库

``` mssql
EXEC master.dbo.sp_attach_db @filename1 = N'path/database.mdf' , @dbname = N'DatabaseName'

```





### 数据库元信息查询

```sql
 select * from sys.databases
```

![image-20201111155858811](C:\Users\Five\Desktop\note\img\image-20201111155858811.png)

## 创建和管理表

```mssql
USE TestDatabase
go

-- Create Database
CREATE TABLE dbo.Products  
   (ProductID int PRIMARY KEY NOT NULL,  
   ProductName varchar(25) NOT NULL,  
   Price money NULL,  
   ProductDescription varchar(max) NULL)  
GO  

-- 插入记录Standard syntax  
-- 可以不指定column，只要keep the values in order，但不推荐，因为不太符合代码易读性原则
INSERT dbo.Products (ProductID, ProductName, Price, ProductDescription)  
    VALUES (1, 'Clamp', 12.48, 'Workbench clamp')  
GO

-- 删除表中所有行
TRUNCATE TABLE TestData.dbo.Products;
GO

-- Returns ProductName and the Price including a 7% tax  
-- Provides the name CustomerPays for the calculated column  
SELECT ProductName, Price * 1.07 AS CustomerPays  
    FROM dbo.Products  
GO
```

此语句包含称为架构的可选元素 (`dbo.`)。 架构是拥有表的数据库对象。 如果您是管理员，则 `dbo` 是默认架构。 `dbo` 代表数据库所有者。

#### ALTER TABLE

##### 添加新列和约束

```mssql
ALTER TABLE dbo.doc_exa ADD column_b VARCHAR(20) NULL ;
```

添加带约束的列


```mssql
ALTER TABLE dbo.doc_exc ADD column_b VARCHAR(20) NULL
    CONSTRAINT exb_unique UNIQUE ;
```

##### 删除列和约束

```mssql
-- Remove a single column.
ALTER TABLE dbo.doc_exb DROP COLUMN column_b ;
GO
-- Remove multiple columns.
ALTER TABLE dbo.doc_exb DROP COLUMN column_c, column_d;
```



##### 更改列定义

更改数据类型

```mssql
ALTER TABLE dbo.doc_exy ALTER COLUMN column_a DECIMAL (5, 2) ;
```

更改列名

```mssql
EXEC sp_rename 'DATABASE.OLD_COLUMN_NAME', 'DATABASE.NEW_COLUMN_NAME'
```

删除列

```mssql
ALTER TABLE dbo.doc_exb DROP COLUMN column_b ;
```



##### 更改表定义



### DROP TABLE

```mssql
DROP TABLE { database_name.schema_name.table_name | schema_name.table_name | table_name }
[;]  
```



## 创建和管理视图

```sql
CREATE VIEW vw_Names  
   AS  
   SELECT ProductName, Price FROM Products;  
GO   
```

一个视图大概就对应一个预执行的`SELECT`语句。



## 数据录入和管理

### INSERT

```mssql
INSERT INTO Production.UnitMeasure  
VALUES (N'FT2', N'Square Feet ', '20080923'), (N'Y', N'Yards', '20080923')
    , (N'Y3', N'Cubic Yards', '20080923');  
```



#### 最佳实践

使用 @@ROWCOUNT 函数返回插入到客户端应用程序的行数。

可以使用 `INSERT INTO <target_table> SELECT <columns> FROM <source_table>` 高效地将大量行从一个表（例如临时表）传输到按最小方式记录日志的其他表中。 按最小方式记录日志可以提高语句的性能，减少在事务期间此操作填充可用事务日志空间的可能性。

### UPDATE



## 创建和管理过程

```sql
CREATE PROCEDURE pr_Names @VarPrice money  
   AS  
   BEGIN  
      -- The print statement returns text to the user  
      PRINT 'Products less than ' + CAST(@VarPrice AS varchar(10));  
      -- A second statement starts here  
      SELECT ProductName, Price FROM vw_Names  
            WHERE Price < @varPrice;  
   END  
GO

EXECUTE pr_Names 10.00;  
GO  
```

# NOTE

> 在单个批处理中提交多条语句时，可以用关键字 GO 分隔各语句。 当批处理只包含一条语句时，GO 是可选的。

> `DatabaseEngine`可安装为区分大小写或不区分大小写。 
>
> 如果`DatabaseEngine`区分大小写进行安装，则对象名必须始终具有相同的大小写。
>
> 如果`DatabaseEngine`按不区分大小写进行安装，则不同大小写的两个表名被视为同一个表。

>在sysobjects系统表中，在数据库中创建的每个对象（例如约束、默认值、日志、规则以及存储过程）都有对应一行，`select * from sysobjects where xtype='U'`就为数据库中的表了。
>
>或者`select * from sys.tables`



## OSQL&SQLCMD

SQL Server命令行工具

![image-20201111143342556](C:\Users\Five\Desktop\note\img\image-20201111143342556.png)

连接成功后会显示`1>`，好像连`show databases`的命令也没有。提示`could not find stored procedure 'show'`

用`go`结束语句并执行。





[^1]:[数据库快速入门指南](https://www.quackit.com/database/tutorial/)
[^2]:[SQL Server快速入门指南](https://www.quackit.com/sql_server/sql_server_2014/tutorial/)

[^3]:https://www.jianshu.com/p/140c6064378c
[^4]:[巨硬官方文档](https://docs.microsoft.com/zh-cn/sql/sql-server/)