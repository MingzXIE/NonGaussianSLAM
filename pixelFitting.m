fileName = 'coordinates.txt';
sample = load(fileName);
x = sample(:,1);
y = sample(:,2);

[fx,xi]=ksdensity(x);
subplot(411)
plot(x)
title('distribution of x coordinates)')
subplot(412)
plot(xi,f)
title('density function of y coordinates')

[fy,yi]=ksdensity(y);
subplot(413)
plot(y)
title('distribution of y coordinates')
subplot(414)
plot(yi,fy)
title('density function of y coordinates')
