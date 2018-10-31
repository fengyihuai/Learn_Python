# -*- coding: UTF-8 -*-
#2.身体质量指数BMI的计算
print('请输入姓名：')
name = input()
height, weight = eval(input('请输入身高（厘米）和体重（千克）[用逗号隔开]：'))
BMI = weight/((0.01*height)**2)
print('您的BMI指数为:{:.2f}'.format(BMI))
nat, dom='' ,''
if BMI<18.5:
    nat, dom='偏瘦', '偏瘦'
elif 18.5<=BMI<24:
    nat, dom = '正常', '正常'
elif 24<=BMI<25:
    nat, dom = '正常', '偏胖'
elif 25<=BMI<28:
    nat, dom = '偏胖', '偏胖'
elif 28<=BMI<30:
    nat, dom = '偏胖', '肥胖'
else:
    nat, dom = '肥胖', '肥胖'
print('您的国际BMI指标是{0},国内BMI指标是{1}'.format(nat,dom))

print()