# 季节变动预测大作业
## 吴蒙蔚
## Matlab实现季节变动预测
```matlab
length=input('please input data length');
data=input('please input data');
out_arr(length+1)=0;
data(length+1)=0;
n(length+1)=0;
s1(length+1)=0;
s2(length+1)=0;
a(length+1)=0;
b(length+1)=0;
nxi(length+1)=0;
%读取数据
for i=1:length
    n(i)=data(i);
end
%三次滑动平均
if length<3
    for i=1:length
        out_arr(i)=n(i);end
end
%我在这里把空缺值补全了
if length>=3
    out_arr(1)=(5*n(1)+2*n(2)-n(3))/6;
     for i=2:length-1
         out_arr(i)=(n(i)+n(i-1)+n(i+1))/3;
     end
     out_arr(length)=(5*n(length)+2*n(length-1)-n(length-2))/6;   
end
disp(out_arr);
%相除得到粗略季节系数
for i=1:length
    nxi(i)=n(i)/out_arr(i);
end
%校正
index=[0,0,0,0];
for i=1:length
    if mod(i,4)==1
        index(1)=nxi(i)+index(1);
    end
    if mod(i,4)==2
        index(2)=nxi(i)+index(2);
    end
        
    if mod(i,4)==3
        index(3)=nxi(i)+index(3);
    end
     if mod(i,4)==0
        index(4)=nxi(i)+index(4);
     end
end
for i=1:4
    index(i)=index(i)/sum(index)*4;
end
disp("校正后的季节性指标")
disp(index);
%二次指数平滑

al=input("请输入权重下降速度alpha");
for i=2:length
   n(i)=al*n(i)+(1-al)*n(i-1);
   s1(i)=n(i);
end
disp(s1);
for i=2:length
 n(i)=al*n(i)+(1-al)*n(i-1);
   s2(i)=n(i);
end
disp(s2);
%求模型a_t,b_t
for i=2:length
    a(i)=2*s1(i)-s2(i);
end
for i=2:length
    b(i)=al/(1-al)*(s1(i)-s2(i));
end
disp("a的值为")
disp(a);
disp("b的值为")
disp(b);
k=input("请输入预测的数据长度");
disp("预测值为")
for i=1:k
x=mod(i,4);
if x==0
  disp((a(length)+b(length)*i)*index(4));
else
    disp((a(length)+b(length)*i)*index(x));
end
end
```
# C#实现季节变动预测
```C
Console.WriteLine("请输入数据长度");
int length = Convert.ToInt32(Console.ReadLine());
double[] n = new double[length];
double[] nxi = new double[length];/*季节系数*/

Console.WriteLine("请输入所有数据");
for (int i = 0; i < length; i++)
{
    n[i] = Convert.ToDouble(Console.ReadLine());
}
/*  求三次滑动平均3*/


 double[] linearSmooth3(double[] in_arr, int N)
{
    double[] out_arr = new double[in_arr.Length];
    int i; if (N < 3)
    {
        for (i = 0; i <= N - 1; i++) { out_arr[i] = in_arr[i]; }
    }
    else
    {
        out_arr[0] = (5.0 * in_arr[0] + 2.0 * in_arr[1] - in_arr[2]) / 6.0;
        for (i = 1; i <= N - 2; i++) { out_arr[i] = (in_arr[i - 1] + in_arr[i] + in_arr[i + 1]) / 3.0; }
        out_arr[N - 1] = (5.0 * in_arr[N - 1] + 2.0 * in_arr[N - 2] - in_arr[N - 3]) / 6.0;
    }
    return out_arr;
}

Console.WriteLine("这里是初步的季节系数");
/*原数据除滑动平均数据*/
for (int i = 0; i < n.Length; i++) {
    Console.WriteLine(linearSmooth3(n, 12)[i]);
    nxi[i]=n[i] / linearSmooth3(n, 12)[i];
    Console.WriteLine(nxi[i]);

}
/*季节性指标*/
double spring = nxi[0] + nxi[4] + nxi[8];
double summer = nxi[1] + nxi[5] + nxi[9];
double fall = nxi[2] + nxi[6] + nxi[10];
double winter = nxi[3] + nxi[7] + nxi[11];
/* 校正*/
Console.WriteLine("这里是校正后的季节指标");
double sum=spring+summer+fall+winter;
double []index=new double[n.Length];
index[0] = spring / sum * 4;
index[1]  = summer / sum * 4;
index[2]= fall / sum * 4;
index[3] = winter / sum*4;
Console.WriteLine($"{ index[0]},{ index[1]},{ index[2]},{ index[3]}");
Console.WriteLine("请输入权重下降的速度alpha");
double alpha=Convert.ToDouble(Console.ReadLine());
Console.WriteLine("一次指数平滑");
/*一次指数平滑*/
double[] n1=new double[length];
double[] n2 = new double[length];
for (int i = 1; i < length; i++)
{
    n[i] =(1-alpha)* n[i-1] + (alpha) * n[i];
    n1[i] = n[i];
    Console.WriteLine($"{n[i]}");
}
/*二次*/
Console.WriteLine("二次指数平滑");
for (int i = 1; i < length; i++)
{
    n[i] = (1 - alpha) * n[i - 1] + (alpha) * n[i];
    Console.WriteLine($"{n[i]}");
    n2[i] = n[i];
}
/*模型的a,b*/
Console.WriteLine("模型的a,b");
double a=2*n1[length-1]-n2[length-1];
double b=alpha/(1-alpha)*(n1[length-1]-n2[length-1]);
Console.WriteLine($"{a}and{b}");
/*预测*/
Console.WriteLine("请输入您将要往后预测的阶段数k");
double k = Convert.ToDouble(Console.ReadLine());
for (int i = 1; i < k+1; i++) {
    double y = (a + b * i) * index[(i-1) % 4];
    Console.WriteLine(y);
}
```