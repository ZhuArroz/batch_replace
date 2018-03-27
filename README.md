# 该代码为Python3脚本，用于批量替换
**运行命令如下：<br/>**
python new_batch_rep_ALL.py test.txt pair.tsv<br/>
“test.txt”原始文本，“pair.tsv”是批量替换的配置文件，运行上述命令后，自动生成：<br/>
test.txt_ALL_AFTER_REPLACEMENT<br/>


**有关tsv（Tab-separated values）文件：**<br/>
该文件的一行分四列（tab隔开）：<br/>
例如：on	^aa	AA	CR<br/>
第一列：on或者off，on表示执行这一行的转换，off表示不执行<br/>
第二列：查找的内容（old string）<br/>
第三列：查找的内容需要转换成的内容（new string）<br/>
第四列：可以为空，表示：不区分大小写，并且不按照正则表达式进行转换<br/>
　　　　可以为C，表示：区分大小写，并且不按照正则表达式进行转换<br/>
　　　　可以为R，表示：不区分大小写，并且按照正则表达式进行转换<br/>
　　　　可以为CR，表示：区分大小写，并且按照正则表达式进行转换<br/>
　　　　用得比较多的情况是：C和CR两种。<br/>
