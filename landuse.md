# 三江平原耕地质量实验报告
[TOC]
## 作者
大家好，我是东北师范大学2020级吴蒙蔚，这是我大二下空间分析大作业，从4月23日世界读书日开始，到5月1日劳动节,我一直在肝这份作业。
做作业的过程中，书本里抽象的概念变得生动起来，看似轻松的步骤方法，殊不知经历了多少人接力造轮子，不断封装复杂的算法，最后呈现出来简单的接口。弄懂复杂算法的意义在哪里，在于接下来的运用，数值分析课讲到了常微分方程的欧拉法，matlab一行代码可以得到结果，但老师带着我们推了一节课，结果重要吗？方法才是关键，思想才是闪闪发光之处.
 ## 摘要
 三江平原的耕地质量关乎民生，一份合理的耕地质量得分图有着重要的意义.
   - 首先是设置各个指标的权重：从日常经验来看，积温，有机质，坡度对耕地质量评估的权重应该是高的，分别是0.15，0.2，0.2，我们选择土地去耕作时，也基本就看看是不是温度够，坡度缓，有机质丰富，其实植物生长还需要三大营养素：氮磷钾，这个也是重要的指标，于是权重均为0.1，坡向在东北平原地区并不如丘陵高山地区重要，故设为0.05。最后是降水，因为东北地区整体降水足，和西北缺水地区不同，故其降水权重设为0.1.
   - 其次是整理思路：
     - 我们首先需要什么数据？土壤，积温，降水，地形，土地利用类型。
     - 其次是怎么处理？积温是个难题，因为我们得到的WorldClim的数据是月平均气温，如果月均气温低于10，那么这个月的积温不能用30$\cdot$(月平均气温)来替代，应该适当缩小。
     - 一共8个指标，需要8个栅格。
     - 土壤数据转4次栅格，然后根据分类表重分类可以得到4个指标分数的栅格，
     - GDEM地形数据可以得到坡度坡向2个指标分数的栅格。
     - 降水和积温用栅格计算器得到累积的5个月的降水和积温再按照分类表重分类得到2个指标的得分栅格，
     - 最后按照权重将8个指标加起来，得到总的质量。
     - 然后通过土地利用图提取出耕地的质量得分，再运用分割栅格的自然断点法得到5级土地，分区统计得到各县市的耕地质量得分。
     - 最后提高分辨率：重采样，得到100m的栅格数据
  

 
 

 ## 数据来源：


### 1. [NASA earthdata搜索网站](https://search.earthdata.nasa.gov/search/)，可以用来查找GDEM数据
   - IDM下载器[下载](https://www.internetdownloadmanager.cn/download)
   - 举例：N47 E132条带的GDEM数据 https://data.lpdaac.earthdatacloud.nasa.gov/lp-prod-protected/ASTGTM.003/ASTGTMV003_N47E132_dem.tif
      （更改N,E后面数字可以获取其他经纬度的影像）
    - <img src="/image/GDEM.jpg" width=100/> 
### 2. Worldclim
  [2010-2018年各月降水](https://data.biogeo.ucdavis.edu/data/worldclim/v2.1/base/wc2.1_30s_prec.zip) ，[各月平均温度](https://data.biogeo.ucdavis.edu/data/worldclim/v2.1/base/wc2.1_30s_tavg.zip)
### 3. 行政区数据来源 
  因为是2021年9月下载的，所以不知道来源，这是文件——[谷歌云盘地址](
  https://drive.google.com/file/d/1ckfxhP74KSR9q2N1sR2lSATJIzFOWfLs/view?usp=sharing)
### 4. 土壤数据
  由郭笑怡老师提供——[谷歌云盘地址]（侵删）(https://drive.google.com/file/d/1koLqOBiK6T_KUlUT7OzyhThgSBR4HV19/view?usp=sharing)  
### 5. [GlobaLand30数据](http://www.globallandcover.com/)
  所用条带：N52_45，N53_45  
  
## 数据处理分析工具：Arcgis pro



## 数据处理方法：
 

 

### Extract by Mask            
![m](/image/dem%E5%8C%BA%E5%9F%9F.jpg)                               
![dem](/image/ext_dem.jpg)                                               
### FeatureclassToFeatureclass 
 ![fea](/image/feature.jpg)                                           
  ![tupian](/image/feature7.jpg)  
### Extract By Attribute 
![屏幕截图 2022-04-29 221130.jpg](https://s2.loli.net/2022/04/29/YTZwcFGp4xhVkqd.jpg)
![屏幕截图 2022-04-29 221130.jpg](https://s2.loli.net/2022/04/29/FNpjeLBJ6y49KEC.jpg)
### 降水处理                  
 ![prep](/image/%E9%99%8D%E6%B0%B4%E5%A4%84%E7%90%86.jpg)           
 ![al_prep](/image/allprep.jpg)   
 ![屏幕截图 2022-04-29 221130.jpg](https://s2.loli.net/2022/04/29/cuAUQEoFp59mOwD.jpg)
### 土壤处理                   
  ![Nraster](/image/%E9%87%8D%E5%88%86%E7%B1%BB%E5%9C%9F%E5%A3%A4.jpg) 
   ![soi](/image/soil_pro.jpg)  
    ![cfltr](/image/soil_reclas.jpg) 
### 坡度坡向                   
 ![pos](/image/%E5%9D%A1%E5%BA%A6%E5%9D%A1%E5%90%91.jpg)              
  ![podu](/image/%E5%9C%B0%E5%9B%BE%E4%BB%A3%E6%95%B0%E5%9D%A1%E5%BA%A6.jpg) 
 ### 积温初步方法               
  ![yanmo](/image/%E7%A7%AF%E6%B8%A91.jpg)                             
   ![jiwen3](/image/%E7%A7%AF%E6%B8%A93.jpg)                                  
### 积温天数比重法             
 ![caij](/image/%E7%A7%AF%E6%B8%A92.jpg)                              
  ![jiwen](/image/reclass_jiwen.jpg)                                         


                                           
### 重分类坡度坡向             
![po](/image/%E9%87%8D%E5%88%86%E7%B1%BB%E5%9D%A1.jpg)               
![屏幕截图 2022-04-29 221130.jpg](https://s2.loli.net/2022/04/29/oKanCykeJcAzGpg.jpg)                                               
                                       
                                         


    

| 范围重分类                                                                                                                   | **语法**                |
| ---------------------------------------------------------------------------------------------------------------------------- | ----------------------- |
| [Remap range 帮助](https://pro.arcgis.com/zh-cn/pro-app/2.8/arcpy/spatial-analyst/an-overview-of-transformation-classes.htm) | RemapRange (remapTable) |


| remapTable | 参数                                   | 说明                                             |
| ---------- | -------------------------------------- | ------------------------------------------------ |
|            | [[startValue, endValue, newValue],...] | 用于将旧值（按范围指定）重映射为新值的重映射表。 |

| 有机质/%    | 全氮/%        | 全磷/%         | 全钾/%        | 坡向              | 坡度       | 积温           | 降水           |
| ----------- | ------------- | -------------- | ------------- | ----------------- | ---------- | -------------- | -------------- |
|             |               |                |               | [-1,0,75]         |
|             |               |                |               | [247.5,292.5,70]  |
|             |               |                |               | [292.5,337.5,60]  |
|             |               |                |               | [337.5,360,50]    |
|             | [0.5,100,100] |                |               | [202.5,247.5,80]  |            |
| [0,2,40]    | [0,0.1,50]    | [0,0.05,40]    | [0,1.5,40]    | [0,22.5,50]       | [0,2,100]  | [0,2000,10]    | [0,450,70]     |
| [2,4,50]    | [0.1,0.2,60]  | [0.05,0.07,50] | [1.5,1.9,50]  | [22.5,67.5,60]    | [2,6,80]   | [2000,2200,30] | [450,500,80]   |
| [4,6,60]    | [0.2,0.3,70]  | [0.07,0.1,60]  | [1.9,2.1,70]  | [67.5,112.5,80]   | [6,15,60]  | [2200,2400,50] | [500,550,90]   |
| [6,8,80]    | [0.3,0.4,80]  | [0.1,0.15,80]  | [2.1,2.5,80]  | [112.5,157.5,90]  | [15,25,40] | [2400,2600,70] | [550,1000,100] |
| [8,100,100] | [0.4,0.5,90]  | [0.15,100,100] | [2.5,100,100] | [157.5,202.5,100] | [25,90,0]  | [2600,4000,90] |


### 加权求总体质量得分


![imath](/image/%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE%202022-04-29%20172047.jpg)
### 自然断点法分割栅格 
**Jenks natural breaks optimization seems to be one dimensional k-means** 
There are two steps that must be repeated:

- Calculate the sum of squared deviations from the class means (SDCM).
- Choose a new way of dividing the data into classes, perhaps by moving one or more data points from one class to a different one.
New class deviations are then calculated, and the process is repeated until the sum of the within class deviations reaches a minimal value.      
 ![nb2](/image/natura_b2.jpg)                                         
  ![nb](/image/natura_break.jpg)    
### 分区统计
![zonal](/image/zonal.jpg)
![zonal](/image/zonal2.jpg)


### 重采样 
![rasample](/image/rasample7.jpg) 
![resample8](/image/resample8.jpg)
## 未解疑问

 
 用栅格计算器的条件函数反复嵌套来重分类坡度坡向,笨拙但有用且不失优雅，反而reclassify坡度坡向时，会报错，下面就是报错，我累了，我还是不知道为啥不能重分类



```python
remap=RemapRange([[0,22.5,50],
[22.5,67.5,60],
[67.5,112.5,80],
[112.5,157.5,90],
[-1,0,75],
[157.5,202.5,100],
[202.5,247.5,80],
[247.5,292.5,70],
[292.5,337.5,60],
[337.5,360,50]])         
reclass_aspect=Reclassify("aspect","Value",remap)
reclass_aspect.save("reclass_aspect")
```
>ERROR 000628: Cannot set input into parameter in_raster.

## 代码流程

```python

import arcpy
from arcpy.sa import *

#--------通过sql的where语句"Name IN ('双鸭山市', '鹤岗市', '佳木斯市')"-------
#--------从要素类到要素类----------------------------------------------------
arcpy.FeatureClassToFeatureClass_conversion(
    r"C:\Users\17503\Desktop\市界.shp",
    r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb",
    "city","Name IN ('双鸭山市', '鹤岗市', '佳木斯市')")
#---------按属性提取 Globaland3土地利用栅格-----------------------------------------------
attExtract = ExtractByAttributes("globaland30", "VALUE = 10") 
attExtract.save(r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\agriculture")
#---------按掩膜提取三江平原三市的耕地栅格----------------------------------------------------
etr_agriculture=ExtractByMask(attExtract,r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\city")
etr_agriculture.save("etr_agriculture")
#------------------------------------按掩膜批量提取降水数据-----------------------------------------------

extract=[]
for i in range(5,10):
    extract.append(ExtractByMask(r"C:\Users\17503\Downloads\wc21_30s_prec\wc21_30s_prec_0{i}.tif".format(i=i),
                            r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\etr_agriculture"))
    
#-------------------------相加栅格并重分类降水数据--------------------------------   

all_prep=extract[0]+extract[1]+extract[2]+extract[3]+extract[4]
all_prep.save(r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\all_prep")
remap=RemapRange([[0,450,70],[450,500,80],[500,550,90],[550,1000,100]])
reclass_prep=Reclassify("all_prep","Value",remap)
reclass_prep.save("reclass_prep")

#--------------------------------------普通积温算法----------------
from arcpy.analysis import *
arcpy.env.workspace=r"C:\Users\17503\Downloads\Compressed\wc2.1_30s_tavg\积温"
N1=Raster("wc21_30s_tavg_09(1).tif")
N2=Raster("wc21_30s_tavg_09(2).tif")
N3=Raster("wc21_30s_tavg_09(3).tif")
N4=Raster("wc21_30s_tavg_09(4).tif")
N5=Raster("wc21_30s_tavg_09(5).tif")
out_ras=N1+N2+N3+N4+N5
out_ras.save("output.tif")
etr_temp=ExtractByMask("output.tif",
r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\etr_agriculture")
etr_temp.save(r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\etr_temp")

#-------如果平均积温小于10，应该乘的天数，应小于30，平均气温越低，天数小于10的概率越大--------
#-------设月平均气温是 n 且 n<10,则求积温时，乘天数为30*n/(10),即 3n-----------------------
etr=[]
for i in range(1,6):
#循环：按掩膜提取，并存到数组etr里，python数组从0开始  
    etr.append(ExtractByMask("wc21_30s_tavg_09({i}).tif".format(i=i),
                     r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\etr_agriculture"))
  #Con函数判断月均气温是否小于10，如果是，则赋值3n^2，否则便直接=30n
    etr[i-1]=Con(etr[i-1]<10,etr[i-1]*etr[i-1]*3,etr[i-1]*30)
    etr[i-1].save(r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\etr_tempr{i}".format(i=i))
    
out_temp2=etr[0]+etr[1]+etr[2]+etr[3]+etr[4]
out_temp2.save(r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb\etrfinal")
    
#---------------积温重分类，Remap_Range映射:[start,end,value]把从 start到 end 之间的值映射成 value-------------------------    
    
    
arcpy.env.workspace=r"C:\Users\17503\Documents\ArcGIS\Projects\MyProject1\MyProject1.gdb"
remap=RemapRange([[0,2000,10],[2000,2200,30],[2200,2400,50],[2400,2600,70],[2600,3000,90]])
Reclassify("etrfinal","Value",remap)
reclass=Reclassify("etrfinal","Value",remap)
reclass.save("reclass_temp")    


#----------SoilData土壤数据先裁剪再通过PolygonToRaster栅格化，再重分类，反复4次--------------------------
#----------------裁剪------------------------
Clip(r"C:\Users\17503\Desktop\study\SoilData\土壤数据.shp","县clip","土clip")
#------------按有机质栅格化，重分类------------
arcpy.conversion.PolygonToRaster("土clip","有机质","yjw_ras")
remap=RemapRange([[0,2,40],[2,4,50],[4,6,60],[6,8,80],[8,100,100]])
reclass_yjw=Reclassify("yjw_ras","Value",remap)
reclass_yjw.save("reclass_yjw")
#------------按全磷栅格化，重分类------------
arcpy.conversion.PolygonToRaster("土clip","全磷","ql_ras")
remap=RemapRange([[0,0.05,40],[0.05,0.07,50],[0.07,0.1,60],[0.1,0.15,80],[0.15,100,100]])
reclass_ql=Reclassify("ql_ras","Value",remap)
reclass_ql.save("reclass_ql")
#------------按全氮栅格化，重分类------------
arcpy.conversion.PolygonToRaster("土clip","全氮","qN_ras")
remap=RemapRange([[0,0.1,50],[0.1,0.2,60],[0.2,0.3,70],[0.3,0.4,80],[0.4,0.5,90],[0.5,100,100]])
reclass_qN=Reclassify("qN_ras","Value",remap)
reclass_qN.save("reclass_qN")
#------------按全钾栅格化，重分类------------
arcpy.conversion.PolygonToRaster("土clip","全钾","qK_ras")
remap=RemapRange([[0,1.5,40],[1.5,1.9,50],[1.9,2.1,70],[2.1,2.5,80],[2.5,100,100]])
reclass_qK=Reclassify("qK_ras","Value",remap)
reclass_qK.save("reclass_qK")

#----------坡度坡向---------------------
#-------省略 Mosaic环节，对不起，"ASTGTMV003_N45E129_dem.tif"就是 Mosaic之后的 GDEM数据-----------
extra_dem=ExtractByMask("ASTGTMV003_N45E129_dem.tif","县clip")
extra_dem.save("extra_dem")
#地图代数
#-----------坡度----------
slope=Slope("extra_dem")
slope.save("slope")
#----------坡向-----------
aspect=Aspect("extra_dem")
aspect.save("aspect")
#----------根据Con函数逐步分类坡度-----------
reclass_slope=Con(slope<=2.0,100,
Con(slope<=6.0,80,
Con(slope<=15.0,60,
Con(slope<=25.0,40,20))))
reclass_slope.save("reclass_slope")
#---------根据Con函数逐步分类坡向----------------------------
reclass_aspect=Con(aspect<=-1.0,75,Con(aspect<=22.5,50,
    Con(aspect<=67.5,60,Con(aspect<=112.5,80,
        Con(aspect<=157.5,90,Con(aspect<=202.5,100,
        Con(aspect<=247.5,80,
        Con(aspect<=292.5,70,
        Con(aspect<=337.5,60,
        Con(aspect<=360,50,0))))))))))
#-----------加权算总耕地质量栅格-------------------------
quality=reclass_prep*0.1+reclass_aspect*0.05+reclass_slope*0.2+reclass*0.15+reclass_yjw*0.2+reclass_qK*0.1+reclass_qN*0.1+reclass_ql*0.1
quality.save("quality")
#------------自然断点法分割栅格------------------------
outslice = Slice("quality",5,"NATURAL_BREAKS")
outslice.save("outslice")
#-----------分区统计-----------------------------------
zonal=ZonalStatistics("县clip","OBJECTID",outslice,"MEAN")
#-------------修改栅格大小：重采样--------------------------------------
arcpy.Resample_management("Extract_outs1","outresample","0.000025 0.000025","NEAREST")
```







