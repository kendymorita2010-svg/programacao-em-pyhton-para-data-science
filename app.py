


import statistics
import pandas as pd
import matplotlib.pyplot as plt



d = pd.read_csv('dados_estudantes.csv')
df  =  pd.DataFrame(d)


fig,ax= plt.subplots()


print()


notas_por_genero = df.groupby('gender')['exam_score'].mean()



# plt.bar(df['gender'], notas_por_genero )


notas_por_genero.plot(kind = 'bar', color = ['red', 'blue', 'yellow'])


plt.show()