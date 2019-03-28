初始建立数据库，使用neo4j-import工具，可支持并行，可扩展的大规模CSV文件数据导入。

所需的基本CSV文件由两部分组成，一个为构建节点用的CSV，一个为把节点联系起来的关系CSV。

实例如下所示：

建立演员个体节点：

| :ID（也可不为数字,理解为主码） | name(也可包含age等属性) | :LABEL（可以多个标签） |
| ------------------------------ | ----------------------- | ---------------------- |
| 15631                          | “Keanu Reeves”          | Actor                  |
| 15632                          | “Laurence Fishburne”    | Actor                  |
| 15633                          | “Carrie-Anne Moss”      | Actor                  |

 

建立电影个体：

| :ID   | title,year                    | :LABEL       |
| ----- | ----------------------------- | ------------ |
| 15634 | “The Matrix”,1999             | Movie        |
| 15635 | “The Matrix Reloaded”,2003    | Movie;Sequel |
| 15636 | “The Matrix Revolutions”,2003 | Movie;Sequel |

 

为电影与演员创建关系：

| :START_ID | Role(可理解为关系的属性) | :END_ID | :TYPE(可理解为关系名) |
| --------- | ------------------------ | ------- | --------------------- |
| 15631     | “Neo”                    | 15634   | ACTS_IN               |
| 15631     | “Neo”                    | 15635   | ACTS_IN               |
| 15631     | “Neo”                    | 15636   | ACTS_IN               |
| 15632     | “Morpheus”               | 15634   | ACTS_IN               |
| 15632     | “Morpheus”               | 15635   | ACTS_IN               |
| 15632     | “Morpheus”               | 15636   | ACTS_IN               |
| 15633     | “Trinity”                | 15634   | ACTS_IN               |
| 15633     | “Trinity”                | 15635   | ACTS_IN               |
| 15633     | “Trinity”                | 15636   | ACTS_IN               |

 

导入数据库后知识图谱示例：

![1553777652173](README.assets/1553777652173.png)