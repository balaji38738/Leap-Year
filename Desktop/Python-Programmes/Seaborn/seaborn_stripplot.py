import matplotlib.pyplot as plt 
import seaborn as sns 
   
subjects =['English', 'Math', 'Science', 'History'] 
marks =[88, 77, 90, 95] 
ax = sns.stripplot(subjects, marks)
ax.set(xlabel ='Days', ylabel ='Amount_spend') 
plt.title('My first graph')
plt.show() 