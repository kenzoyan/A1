#%%
from pyecharts import Bar, Overlap,Line,Grid,Pie
import pandas as pd
df= pd.read_csv("C:\\Users\\57070\\Desktop\\visualization\\experiment\\census2000.csv")



Male1900= df[(df['Sex'] == 1)&(df['Year'] == 1900)]['People']
Female1900= df[(df['Sex'] == 2)&(df['Year'] == 1900)]['People']
Male2000 = df[(df['Sex'] == 1)&(df['Year'] == 2000)]['People']
Female2000=df[(df['Sex'] == 2)&(df['Year'] == 2000)]['People']

#People Group
num1900=df[df['Year'] == 1900]
sum1900=[]
sum1900.append(num1900[(num1900['Age']<26)]['People'].sum())
sum1900.append(num1900[(num1900['Age']>26)&(num1900['Age']<66)]['People'].sum())
sum1900.append(num1900[(num1900['Age']>65)]['People'].sum())

num2000=df[df['Year'] == 2000]
sum2000=[]
sum2000.append(num2000[(num2000['Age']<26)]['People'].sum())
sum2000.append(num2000[(num2000['Age']>26)&(num2000['Age']<66)]['People'].sum())
sum2000.append(num2000[(num2000['Age']>65)]['People'].sum())


#float  --> int
Male1900int= Male1900/1000
Female1900int= Female1900/1000
Male2000int = Male2000/1000
Female2000int=Female2000/1000
Male1900int.astype("int")
Female1900int.astype("int")
Male2000int.astype("int")
Female2000int.astype("int")

#sex ratio
#1900
aa=Male1900.reset_index(drop=True)
bb=Female1900.reset_index(drop=True)
sexRatio1900=pd.DataFrame({'a':aa,'b':bb})
sexRatio1900['ratio']=sexRatio1900['a']*100/sexRatio1900['b']
#2000
aa=Male2000.reset_index(drop=True)
bb=Female2000.reset_index(drop=True)
sexRatio2000=pd.DataFrame({'a':aa,'b':bb})
sexRatio2000['ratio']=sexRatio2000['a']*100/sexRatio2000['b']
#print(sexRatio2000)
#bar
attr = [i for i in range(0,95,5)]
bar = Bar("Census of US in 1900 and 2000")
bar.add("Male1900", attr, Male1900int,is_stack=True)
bar.add("Female1900", attr, Female1900int,is_stack=True,xaxis_name="Age",
            xaxis_name_size=20,
            yaxis_name='Population(Thousand)',
            yaxis_name_size=15,
            yaxis_name_pos='end',
            yaxis_line_color='#4682B4',)
bar1=Bar()
bar1.add("Male2000", attr, Male2000int, is_stack=True)
bar1.add("Female2000", attr, Female2000int,is_stack=True)

#line
line1=Line()
v1=sexRatio1900['ratio'].round(decimals=2)
line1.add('Ratio 1900',[i for i in range(19)],v1,
            yaxis_force_interval=20, yaxis_max=120,yaxis_min=20)

line2=Line()
v2=sexRatio2000['ratio'].round(decimals=2)
line2.add('Ratio 2000',[i for i in range(19)],v2,
            yaxis_force_interval=20, 
            yaxis_max=120,yaxis_min=20,
            yaxis_line_color='#CD5555',
            yaxis_name='Sex Ratio',
            yaxis_name_pos='end',
            )
#overline
overlap=Overlap("Census of US in 1900/2000",width=1400,height=700)
overlap.add(bar)
overlap.add(bar1)
overlap.add(line1,yaxis_index=1,is_add_yaxis=True)
overlap.add(line2,yaxis_index=1,is_add_yaxis=True)

#pie
pie=Pie('Group Share in 1900 and 2000',subtitle='1900                                                          2000',
            subtitle_text_size=30,
            title_pos='center',title_top='50%', width=1400,title_text_size=20 )
pie.add(
    name="1900",
    attr=['Under 25','21--65', 'Over 65'],
    value=sum1900,
    center=[25, 75],
    is_random=True,
    radius=[0, 25],
    rosetype="area",
    is_label_show=True,
    
)
pie.add(
    name="2000",
    attr=['Under 25','21--65', 'Over 65'],
    value=sum2000,
    center=[75, 75],
    is_random=True,
    radius=[0, 25],
    rosetype="area",
    is_legend_show=True,
    is_label_show=True,
    legend_orient="vertical",
    legend_pos="center",
    legend_top='60%'
)

#show the final charts
grid = Grid(width=1400,height=700)
grid.add(overlap, grid_bottom="60%")
grid.add(pie, grid_bottom="60%")
grid.render()


