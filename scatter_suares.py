import matplotlib.pyplot as plt 


x_values = range(1, 5000)
y_values = [x**3 for x in x_values]


plt.style.use('seaborn')
fix, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Set1, s = 10)

#set chart title and label axes
ax.set_title("Square Numbers", fontsize = 24)
ax.set_xlabel("Wert", fontsize = 14)
ax.set_ylabel("Quadrat des Wertes", fontsize = 14)



#set size of tick labels
ax.tick_params(axis= 'both', which='major', labelsize=14)
ax.axis([0, 5300, 0, 5100**3])

plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()