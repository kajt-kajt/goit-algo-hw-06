## Опис даних

У якості прикладу графа візьмемо набір задач для побудови нового середовища для сайту.
Вершини графа - задачі, ребра - залежності між ними. 
Граф орієнтований та ациклічний (циклічні залежності між задачами не мають сенсу).

Для зручності застосування базових алгоритмів додамо ще 2 вершини - "start" та "end". 
"start" матиме вихідні ребра до всіх вершин без залежностей (ті, з яких можна починати проект).
"end" має вхідні ребра з усіх вершин, які не є залежностями для інших.

Вага ребер у графі - це оцінка складності вихідної вершини.

## Задача 1

Візуалізація графа:
![Figure_1](./Figure_1.png "")

Базові характеристики:

```
Let's display some graph properties.
General characteristics:  DiGraph with 16 nodes and 29 edges
Nodes properties: 
start  ->  {'layer': 1000}
   node degre:  2
   betweenness centrality:  0.0
end  ->  {'layer': 965}
   node degre:  3
   betweenness centrality:  0.0
SYS01  ->  {'title': 'Create new AWS account', 'estimate': 1, 'layer': 995}
   node degre:  2
   betweenness centrality:  0.030952380952380953
NET01  ->  {'title': 'Get new internal subnet assignment from Network Architect', 'estimate': 1, 'layer': 995}
   node degre:  2
   betweenness centrality:  0.030952380952380953
NET02  ->  {'title': 'Create new VPC', 'estimate': 4, 'layer': 990}
   node degre:  4
   betweenness centrality:  0.17142857142857143
SEC01  ->  {'title': 'Basic security settings of new AWS account', 'estimate': 8, 'layer': 985}
   node degre:  4
   betweenness centrality:  0.06666666666666668
SYS03  ->  {'title': 'Create ssh bastion host EC2', 'estimate': 16, 'layer': 985}
   node degre:  5
   betweenness centrality:  0.12380952380952381
SYS04  ->  {'title': 'Create web-nodes EC2', 'estimate': 16, 'layer': 980}
   node degre:  3
   betweenness centrality:  0.0
SYS05  ->  {'title': 'Create database RDS instances', 'estimate': 4, 'layer': 980}
   node degre:  4
   betweenness centrality:  0.02142857142857143
SYS06  ->  {'title': 'Create Redis cluster instances (ElastiCache)', 'estimate': 4, 'layer': 980}
   node degre:  3
   betweenness centrality:  0.005952380952380953
SYS07  ->  {'title': 'Create glusterfs EC2 cluster', 'estimate': 8, 'layer': 980}
   node degre:  4
   betweenness centrality:  0.014285714285714287
SYS08  ->  {'title': 'Create Load balancer', 'estimate': 2, 'layer': 980}
   node degre:  3
   betweenness centrality:  0.005952380952380953
SYS09  ->  {'title': 'Setup monitoring for new instances', 'estimate': 8, 'layer': 975}
   node degre:  7
   betweenness centrality:  0.04642857142857143
OPS03  ->  {'title': 'Create deploy pipeline', 'estimate': 16, 'layer': 975}
   node degre:  7
   betweenness centrality:  0.05238095238095239
SYS12  ->  {'title': 'Setup backups', 'estimate': 4, 'layer': 975}
   node degre:  3
   betweenness centrality:  0.005952380952380953
TEST01  ->  {'title': 'Test new environment functionality', 'estimate': 24, 'layer': 970}
   node degre:  2
   betweenness centrality:  0.004761904761904762
Edges properties: 
('start', 'SYS01')  ->  {'weight': 0}
('start', 'NET01')  ->  {'weight': 0}
('SYS01', 'NET02')  ->  {'weight': 1}
('NET01', 'NET02')  ->  {'weight': 1}
('NET02', 'SEC01')  ->  {'weight': 4}
('NET02', 'SYS03')  ->  {'weight': 4}
('SEC01', 'SYS05')  ->  {'weight': 8}
('SEC01', 'SYS06')  ->  {'weight': 8}
('SEC01', 'SYS08')  ->  {'weight': 8}
('SYS03', 'SYS04')  ->  {'weight': 16}
('SYS03', 'SYS07')  ->  {'weight': 16}
('SYS03', 'SYS09')  ->  {'weight': 16}
('SYS03', 'OPS03')  ->  {'weight': 16}
('SYS04', 'SYS09')  ->  {'weight': 16}
('SYS04', 'OPS03')  ->  {'weight': 16}
('SYS05', 'SYS09')  ->  {'weight': 4}
('SYS05', 'OPS03')  ->  {'weight': 4}
('SYS05', 'SYS12')  ->  {'weight': 4}
('SYS06', 'SYS09')  ->  {'weight': 4}
('SYS06', 'OPS03')  ->  {'weight': 4}
('SYS07', 'SYS09')  ->  {'weight': 8}
('SYS07', 'OPS03')  ->  {'weight': 8}
('SYS07', 'SYS12')  ->  {'weight': 8}
('SYS08', 'SYS09')  ->  {'weight': 2}
('SYS08', 'OPS03')  ->  {'weight': 2}
('SYS09', 'end')  ->  {'weight': 0}
('OPS03', 'TEST01')  ->  {'weight': 16}
('SYS12', 'end')  ->  {'weight': 0}
('TEST01', 'end')  ->  {'weight': 0}
```
