%%
n=10;a=0;b=3;
h=(b-a)/n;
x=linspace(a,b,n+1);
y(1)=0;
for i=1:n 
   if i==1
    y(i+1)=y(i)+h;
   else 
    y(i+1)=y(i)+h*(y(i)/x(i)-2*y(i)^2);
   end
end  
y_exact= @(x) x./(1+x.^2)
figure(3)
plot(x, y,'-+r',x,y_exact(x),'-*b');
%%
syms y(x); % be careful performance issue.
dsolve(diff(y)==exp(x)-100*y,y(0)==1)
sh Anaconda3-2019.07-Linux-x86_64.sh


