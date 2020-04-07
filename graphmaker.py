#%%
import matplotlib.pyplot as plt
x = [13714,438848,877696,3510784,14043136]
x2 = [13714,438848,877696]

# %% WHERE SELECT


y_S = [0.00872374,0.36960118,0.7209808,3.10654306,14.76947768]
y_M = [0.00852944, 0.23936404,0.47752148,1.85637676,7.52274314]
y_N = [0.0204988,0.70753306,1.57221028,11.0932327333,61.11157664]

# Create plots with pre-defined labels.
plt.plot(x, y_S, label='MySQL')
plt.plot(x, y_N, label='MySQL (N)')
plt.plot(x, y_M, label='MongoDB')
plt.legend(prop={'size': 12})
plt.xlabel('Number of rows')
plt.ylabel('Time')
plt.savefig('whereselectorder.png', dpi=300)
plt.show()
# %%
# %%

y_S = [0.01100806,6.76396422,14.16675534,81.39203194,396.45387]
y_M = [0.02292838,0.97658454,1.83709875,7.62395288,39.38610376]
y_N = [0.18144292,13.18182844,64.64303954]

# Create plots with pre-defined labels.
plt.plot(x, y_S, label='MySQL')
plt.plot(x2, y_N, label='MySQL (N)')
plt.plot(x, y_M, label='MongoDB')
plt.legend(prop={'size': 12})
plt.xlabel('Number of rows')
plt.ylabel('Time')
plt.savefig('wherebiggerthan.png', dpi=300)
plt.show()

# %%

y_S = [0.01883966,0.49301376,0.97285572,3.86612438, 15.64708246]
y_M = [0.02060598,0.47419018,0.93042724,3.684332,14.66278396]
y_N = [0.0180218,0.018055,0.01747106, 0.0180753,0.01819784]

# Create plots with pre-defined labels.
plt.plot(x, y_S, label='MySQL')
plt.plot(x, y_N, label='MySQL (N)')
plt.plot(x, y_M, label='MongoDB')
plt.legend(prop={'size': 12})
plt.xlabel('Number of rows')
plt.ylabel('Time')
plt.savefig('uniquevalues.png', dpi=300)
plt.show()

# %%

y_S = [0.4862193000000019,14.774550499999997,29.460182599999996,169.271523,893.1797744]
y_M = [0.4965974999999929,10.3063201,19.8084318,81.6818316,406.11787089999996]
y_N = [1.0586079999999924,24.936907200000007,49.397535600000005,205.32487279999998,751.7366415]

# Create plots with pre-defined labels.
plt.plot(x, y_S, label='MySQL')
plt.plot(x, y_N, label='MySQL (N)')
plt.plot(x, y_M, label='MongoDB')
plt.legend(prop={'size': 12})
plt.xlabel('Number of rows')
plt.ylabel('Time')
plt.savefig('insertdb.png', dpi=300)
plt.show()

# %%

y_S = [0.04700308,1.7780666,3.35185524,14.40811664,53.27937518]
y_M = [0.01562358, 0.51391494,0.91402764,4.035426,16.33024722]
y_N = [0.0513652,1.72301472,3.1520862, 13.60865028,51.0600305]

# Create plots with pre-defined labels.
plt.plot(x, y_S, label='MySQL')
plt.plot(x, y_N, label='MySQL (N)')
plt.plot(x, y_M, label='MongoDB')
plt.legend(prop={'size': 12})
plt.xlabel('Number of rows')
plt.ylabel('Time')
plt.savefig('changerows.png', dpi=300)
plt.show()

# %%

y_S = [0.0219883000002028, 1.4191093000000023,1.7935453000000052,9.038744299999962, 49.05277299999989]
y_M = [0.007669599999985621, 0.2173468000000014,0.45480029999998806,1.7595146000000454,7.584323900000015]
y_N = [0.01983210000003055, 1.4278837000000522,1.7374849999999924, 7.315774799999872,33.0807509]

# Create plots with pre-defined labels.
plt.plot(x, y_S, label='MySQL')
plt.plot(x, y_N, label='MySQL (N)')
plt.plot(x, y_M, label='MongoDB')
plt.legend(prop={'size': 12})
plt.xlabel('Number of rows')
plt.ylabel('Time')
plt.savefig('deleterowswhere.png', dpi=300)
plt.show()

# %%


# %%
