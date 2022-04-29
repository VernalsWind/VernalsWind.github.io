syms y(x); % be careful performance issue.
dsolve(diff(y)==exp(x)-100*y,y(0)==1);