# Utilizing MapReduce to implement frequent doubleton itemsets

## The project utilizes MapReduce and AWS to form doubleton sets.

### Input File
The original data is stored in transaction.dat. Each line is a transaction containing multiple items separated by space (item1 item2 item3 · · · itemn)
The input file was stored on Amazon S3.

***The scripts are run on EMR cluster***
### The mapper class
The map function would take this original file and generate an intermediate output. The input key would be line number in input file. The input value would be the content in each line. The output key would be the doubleton itemsets. The output value is 1.
***For example:***
1 2 3 ⇒ ((1,2),1), ((1,3),1), ((2,3),1)
2 3 ⇒ ((2,3),1)

### The reducer class
The reduce function would aggregate all values for each key. The output key would be itemsets.The output value is the number of occurrence of each corresponding key. In the example case, it will generate the following outputs: ***((2,3),2)***
