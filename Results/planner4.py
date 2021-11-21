from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt

startPos = [[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64],
	[0.64, 0.64],
	[0.64, 0.64],
	[0.64, 0.64]]
res = 0.08

def map_plot(map, index):
	for i in range(len(map)):
		for j in range(len(map[0])):
			plt.scatter(startPos[index][0] + i*res, startPos[index][1] - j*res, c=str(1/(1+np.exp(map[i][j]))))
	plt.title(f'Robot planning path around obstacle - map {index + 1}')
	plt.xlabel('x (m)')
	plt.ylabel('y (m)')
	plt.grid()

def path_plot(path):
	print(path)

	plt.scatter(path[0][0], path[0][1], c='darkred', s=50, label='init pos', zorder=10)
	plt.scatter(path[-1][0], path[-1][1], c='orange', s=50, label='final pos', zorder=10)
	plt.plot(path[:,0], path[:,1], c='r', marker='.', markersize=20, label='path')
	plt.legend()

def paths():
	pos = [
		[0, 0],
		[0.14, -0.01],
		[0.38, -0.02],
		[0.53, -0.00],
		[0.67, 0.01],
		[0.81, 0.01],
		[0.96, -0.00],
		[1.10, 0.00]
	]

	path = [
		[[0.24, 0.00],
		[0.48, 0.00],
		[0.72, 0.00],
		[0.96, 0.00],
		],
		[[0.48, 0.00],
		[0.72, 0.00],
		[0.96, 0.00],
		],
		[[0.62, -0.02],
		[0.86, -0.02],
		[1.10, -0.02],
		],
		[[0.77, -0.00],
		[1.01, -0.00],
		],
		[[0.91, 0.01],
		],
		[[1.05, 0.01],
		],
		[[1.20, -0.00],
		],
		[[1.10, 0.00]]
	]
	
	maps = [
		[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -17.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -0.8, -18.6, -18.6, -17.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[2.8, 2.4, -0.5, -1.7, -2.5, -4.2, -21.2, -17.8, -18.6, -17.8, -14.1, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[4.2, 4.1, 0.0, -3.4, -3.4, -22.0, -20.0, -0.3, 6.1, 0.5, 13.0, 27.3, 0.0, 0.0, 0.0, 0.0, ],
[5.5, 6.9, 2.4, -4.4, -23.7, -22.9, -15.0, 29.6, 30.5, 29.1, 29.1, 29.1, 27.7, 0.0, 0.0, 0.0, ],
[6.9, 6.9, 5.2, -18.3, -22.0, -22.9, -13.1, 30.5, 30.5, 29.1, 29.1, 30.5, 49.6, 1.4, 0.0, 0.0, ],
[16.0, 8.9, -9.5, -15.5, -22.4, -19.3, 6.5, 46.6, 50.6, 45.7, 1.7, 32.8, 0.0, 0.0, 0.0, 0.0, ],
],
		[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -17.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -0.8, -18.6, -18.6, -17.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[2.8, 2.4, -0.5, -1.7, -2.5, -4.2, -21.2, -17.8, -18.6, -17.8, -14.1, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[4.2, 4.1, 0.0, -3.4, -3.4, -22.0, -20.0, -0.3, 6.1, 0.5, 13.0, 27.3, 0.0, 0.0, 0.0, 0.0, ],
[5.5, 6.9, 2.4, -4.4, -23.7, -22.9, -15.0, 29.6, 30.5, 29.1, 29.1, 29.1, 27.7, 0.0, 0.0, 0.0, ],
[6.9, 6.9, 5.2, -18.3, -22.0, -22.9, -13.1, 30.5, 30.5, 29.1, 29.1, 30.5, 49.6, 1.4, 0.0, 0.0, ],
[16.0, 8.9, -9.5, -15.5, -22.4, -19.3, 6.5, 46.6, 50.6, 45.7, 1.7, 32.8, 0.0, 0.0, 0.0, 0.0, ],
],
		[[6.1, -6.9, -13.1, -16.5, -22.4, -21.2, 2.1, 0.0, 0.0, 0.0, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, ],
[0.0, 5.5, -14.3, -18.0, -22.7, -23.7, -5.1, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, ],
[-1.7, -3.4, 2.6, -16.8, -22.0, -7.6, -9.3, -5.9, -2.5, -1.7, -1.7, -1.7, -2.5, -2.5, -2.5, -2.5, ],
[-2.8, -2.0, 1.9, -1.1, -6.8, -7.6, -8.0, -7.6, -5.1, -2.5, -1.7, -2.5, -2.5, -1.7, -1.7, -1.7, ],
[-1.6, -1.1, -0.6, -0.7, -6.8, -6.2, -7.6, -9.3, -7.6, -5.1, -3.4, -2.5, -1.7, -1.7, -2.5, -2.5, ],
[-0.3, -0.4, -1.7, -4.2, -5.4, -6.2, -4.2, -9.3, -5.9, -7.5, -4.2, -3.4, -3.4, -2.5, -0.8, -1.7, ],
[-0.3, -2.5, -3.4, -3.4, -6.5, -7.6, -5.9, -8.4, -7.7, -3.9, -3.0, -4.2, -4.2, -3.4, -3.4, -1.6, ],
[0.6, -1.9, -2.4, -4.8, -7.2, -7.0, -4.0, -0.4, 3.3, 6.8, 3.5, -0.1, -3.5, -3.4, -2.5, -1.4, ],
[-0.8, -0.8, -1.2, 1.3, 1.7, 3.5, 6.1, 6.3, 10.9, 13.0, 5.5, 4.4, -3.4, -3.2, -1.7, 0.0, ],
[-0.8, -0.8, -0.8, 3.9, 3.9, 6.1, 8.3, 5.5, 10.6, 13.7, 12.4, -0.8, -3.2, -1.7, -1.0, 0.0, ],
[-0.8, -1.7, -1.7, 3.5, 5.1, 5.1, 6.6, 10.7, 13.8, 7.7, 0.0, 0.0, -0.8, -1.0, 0.0, 0.0, ],
[0.0, -1.7, -1.7, -1.7, -1.7, -0.3, 1.6, 1.5, 0.0, 0.0, 0.0, 0.0, -0.8, 0.0, 0.0, 0.0, ],
[0.0, 0.0, -0.8, -0.8, -0.8, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
],
		[[6.1, -6.9, -13.1, -16.5, -22.4, -21.2, 2.1, 0.0, 0.0, 0.0, -0.8, -0.8, -0.8, -0.8, -0.8, -0.8, ],
[0.0, 5.5, -14.3, -18.0, -22.7, -23.7, -5.1, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, -1.7, ],
[-1.7, -3.4, 2.6, -16.8, -22.0, -7.6, -9.3, -5.9, -2.5, -1.7, -1.7, -1.7, -2.5, -2.5, -2.5, -2.5, ],
[-2.8, -2.0, 1.9, -1.1, -6.8, -7.6, -8.0, -7.6, -5.1, -2.5, -1.7, -2.5, -2.5, -1.7, -1.7, -1.7, ],
[-1.6, -1.1, -0.6, -0.7, -6.8, -6.2, -8.5, -11.0, -9.3, -6.8, -4.2, -3.4, -2.5, -2.5, -3.4, -3.4, ],
[-0.3, -0.4, -1.7, -4.2, -5.4, -6.2, -4.2, -10.2, -9.3, -10.1, -6.8, -5.9, -5.9, -5.1, -2.5, -3.4, ],
[-0.3, -2.5, -3.4, -3.4, -6.5, -8.5, -5.9, -10.1, -11.9, -8.2, -3.8, -6.8, -5.9, -5.9, -5.9, -4.1, ],
[0.6, -1.9, -2.4, -4.8, -8.0, -7.8, -4.0, -1.7, 2.8, 4.7, 1.1, -2.6, -6.0, -5.9, -4.2, -3.1, ],
[-0.8, -0.8, -1.2, 1.3, 0.9, 2.7, 6.1, 8.0, 17.0, 13.9, 4.3, 2.4, -5.4, -4.9, -5.1, -3.4, ],
[-0.8, -0.8, -0.8, 3.0, 3.0, 5.2, 8.3, 8.3, 17.6, 16.5, 12.6, -2.0, -4.8, -5.1, -2.7, -1.7, ],
[-0.8, -1.7, -2.5, 2.6, 4.2, 4.3, 8.0, 14.8, 20.7, 15.5, 2.8, -1.0, -3.4, -4.4, -3.4, -2.5, ],
[0.0, -1.7, -2.5, -2.5, -2.5, -1.1, 3.2, 4.8, 1.5, 0.0, -0.8, -1.7, -3.4, -1.7, -2.2, -2.0, ],
[0.0, -0.8, -1.7, -1.7, -1.7, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, -1.7, -2.5, -2.1, -1.1, -0.3, ],
[0.0, -0.8, -0.8, -0.8, -0.8, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -0.8, -1.7, -0.6, 0.0, ],
[0.0, 0.0, 0.0, 0.0, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -0.6, 0.2, 0.9, 1.4, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.2, 0.7, 1.4, 0.0, 0.0, ],
]
	]

	print(len(pos))
	print(len(path))
	print(len(maps))

	for i in range(len(path)):
		plt.figure(figsize=(10,5))
		map_plot(maps[i], i)
		path_plot(np.array(path[i]))
	

paths()
plt.show()