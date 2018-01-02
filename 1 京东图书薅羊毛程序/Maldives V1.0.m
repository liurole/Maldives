function [ stack_1, stack_2 ] = Maldives V1.0( )
% Maldives V1.0
% 京东薅羊毛程序
% 用于使用600-450图书优惠券
% 由于总价不过1200，故将其分为两组，使其一组的总价为600
% 优惠不再来啊

bEnd = 1;
% 售价
stack_1  = [21.90 45.80 63.80 37.00 49.50 28.30 41.00 61.40 69.40 37.10 56.10 49.40 70.30 84.60 94.10 43.80 46.60 101.20];
stack_2 = zeros(size(stack_1));

while (bEnd)
    t = sum(stack_1);
    if (t > 601)||(t<600)
        i = randi([1 18]);
        temp1 = stack_1(i);
        temp2 = stack_2(i);
        stack_1(i) = temp2;
        stack_2(i) = temp1;
    else
        bEnd = 0;
    end  
end
























end

