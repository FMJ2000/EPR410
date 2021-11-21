from matplotlib import markers
import numpy as np
import matplotlib.pyplot as plt

startPos = [[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64],
	[-0.64, 0.64]]
res = 0.08

def pos_plot(pos, exPos):
	plt.scatter(pos[0], pos[1], c='r', marker='.', s=400, label='bot')
	plt.scatter(exPos[0], exPos[1], c='b', marker='.', s=400, label='frontier')

def map_plot(map, index):
	title = str(index + 1) if index >= 0 else "summary"
	index = 0 if index < 0 else index
	for i in range(len(map)):
		for j in range(len(map[0])):
			plt.scatter(startPos[index][0] + i*res, startPos[index][1] - j*res, c=str(1/(1+np.exp(map[i][j]))))
	plt.title(f'Robot exploring environment - map {title}')
	plt.xlabel('x (m)')
	plt.ylabel('y (m)')
	plt.grid()

def visit_plot(map, index):
	for i in range(len(map)):
		for j in range(len(map[0])):
			for k in range(8):
				if ((map[i][j] >> k) & 0x1):
					plt.scatter(startPos[index][0] + i*res, startPos[index][1] - (8*j + k)*res, c='lightgreen')

def path_plot(path):
	print(path)

	plt.scatter(path[0][0], path[0][1], c='darkred', s=50, label='init pos', zorder=10)
	plt.scatter(path[-1][0], path[-1][1], c='orange', s=50, label='final pos', zorder=10)
	plt.plot(path[:,0], path[:,1], c='r', marker='.', markersize=20, label='path')

def paths():
	pos = [
		[0, 0],
		[0.16, -0.11],
		[0.45, 0.14],
		[0.45, -0.20],
		[0.36, -0.13],
		[0.26, -0.02],
		[0.25, 0.03],
		[0.09, 0.03]
	]

	exPos = [
 		[0.32, -0.16],
		[0.56, 0.32],
		[0.48, -0.40],
		[-0.64, 0.64],
		[0.16, 0.16],
		[-0.64, 0.64],
		[0.16, 0.08],
		[0.48, -0.56]
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
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -16.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -16.9, -16.9, -16.9, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -16.9, -16.9, -16.9, -16.9, -16.9, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -16.9, -16.9, 0.0, -16.9, 0.0, -16.9, -16.9, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, -16.9, 0.0, 0.0, ],
[0.0, 0.0, -16.9, -16.9, -16.9, -16.9, 0.0, -16.9, -16.9, -16.9, 0.0, -16.9, -16.9, -16.9, -16.9, 0.0, ],
],
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -1.7, -1.7, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -16.9, -3.4, -1.7, -2.5, -2.5, -2.5, -2.5, -2.5, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -16.9, -16.9, -19.5, -7.9, 10.2, 8.0, -1.7, -3.4, -3.4, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -16.9, -17.8, -16.9, -26.3, -27.1, -6.2, 14.8, 1.8, -1.7, -1.7, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -16.9, -16.9, -0.8, -17.8, -8.5, -24.6, -27.1, -4.5, -3.4, -3.4, 0.0, ],
[0.0, 0.0, 0.0, 0.0, -16.9, -16.9, -17.8, -17.8, -18.6, -24.6, -27.3, -24.2, -24.3, -6.8, -3.4, -3.4, ],
[0.0, 0.0, 0.0, -16.9, -16.9, -16.9, -17.8, -18.6, -18.6, -24.6, -26.3, -23.2, -24.0, -24.9, -5.9, -3.4, ],
[0.0, 0.0, -16.9, -16.9, -16.9, -17.8, -1.7, -18.6, -18.6, -24.6, -9.3, -20.6, -23.2, -22.8, -26.3, -5.4, ],
],
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -1.7, -1.7, ],
[2.8, 0.0, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, -16.9, -3.4, -1.7, -2.5, -2.5, -2.5, -2.5, -2.5, ],
[4.9, 1.2, -0.3, -1.7, -1.7, -1.7, 0.0, -16.9, -16.9, -19.5, -7.9, 10.2, 8.0, -1.7, -3.4, -3.4, ],
[6.5, 2.5, 1.1, -0.6, -3.2, -3.4, -21.2, -21.2, -19.5, -30.5, -27.1, -6.2, 14.8, 1.8, -1.7, -1.7, ],
[7.9, 6.6, 4.7, 2.7, -1.9, -21.2, -22.0, -12.7, -33.9, -21.2, -36.4, -27.1, -4.5, -3.4, -3.4, 0.0, ],
[4.3, 6.2, 9.4, 4.7, -15.5, -20.3, -33.7, -34.7, -22.0, -37.3, -39.2, -31.0, -24.3, -6.8, -3.4, -3.4, ],
[3.5, 8.0, 12.7, -2.7, -8.5, -26.2, -30.8, -35.6, -30.5, -37.3, -36.4, -35.0, -24.0, -24.9, -5.9, -3.4, ],
[0.0, 9.0, -2.4, 2.5, 2.0, -14.0, -20.3, -28.8, -31.4, -37.3, -16.9, -32.5, -31.7, -22.8, -26.3, -5.4, ],
],
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.4, 1.4, 1.4, 4.0, 2.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.4, 1.4, 2.8, 2.8, 2.8, 1.4, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.8, 0.9, 1.9, 2.5, 1.4, 1.4, 1.4, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.7, -0.5, -1.0, 2.7, 2.3, 1.2, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -0.8, -1.7, 0.5, 1.9, 4.2, -0.8, -1.7, -1.7, ],
[2.8, 0.0, -0.8, 0.0, 0.0, 0.0, 0.0, -0.8, -18.6, -3.9, -1.2, 0.2, 1.6, 1.9, -2.5, -2.5, ],
[4.9, 1.2, -0.3, -1.7, -1.7, -1.7, 0.0, -17.8, -18.6, -20.6, -7.3, 14.3, 14.0, 6.0, -1.1, -3.4, ],
[6.5, 2.5, 1.1, -0.6, -3.2, -3.4, -21.2, -22.0, -21.2, -33.0, -28.0, -1.1, 27.2, 16.8, 7.0, -0.2, ],
[7.9, 6.6, 4.7, 2.7, -1.9, -21.2, -22.0, -13.6, -35.6, -22.9, -39.0, -21.7, 8.1, 10.7, 7.9, 2.0, ],
[4.3, 6.2, 9.4, 4.7, -15.5, -20.3, -33.7, -35.6, -23.7, -39.8, -44.4, -26.9, -13.4, 9.1, 10.7, 7.2, ],
[3.5, 8.0, 12.7, -2.7, -8.5, -26.2, -30.8, -37.3, -33.9, -44.1, -44.1, -42.6, -22.7, -18.5, 1.5, 5.3, ],
[0.0, 9.0, -2.4, 2.5, 2.0, -13.8, -22.0, -30.5, -32.2, -39.0, -20.3, -35.9, -33.9, -22.5, -25.0, -1.6, ],
],
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.1, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.6, -0.8, -0.8, -1.5, -1.5, -0.6, -1.2, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 3.3, 0.5, 0.5, 2.3, 0.3, -0.8, -1.7, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 3.4, 5.8, 2.8, 1.9, 1.9, 1.1, 1.1, 0.5, -1.7, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 0.0, 1.9, 6.6, 6.8, 5.0, 2.3, 1.0, 0.8, -0.3, 0.5, 0.5, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 1.8, 6.9, 4.2, 5.5, 4.3, -0.2, -1.8, 1.0, 0.6, -0.5, -0.8, -0.8, 0.0, ],
[0.0, 0.0, 0.0, 5.6, 1.4, 4.2, 3.7, 0.7, -2.0, -3.4, -1.2, 0.2, 2.5, -1.7, -2.5, -1.7, ],
[2.8, 0.0, 3.1, 5.5, 4.2, 2.4, 0.1, -2.3, -22.0, -4.8, -2.0, -1.5, -0.1, 1.1, -2.5, -2.5, ],
[4.9, 1.2, 5.3, 2.5, 2.5, 0.1, -1.8, -20.3, -22.0, -22.2, -8.1, 12.6, 13.1, 6.0, -1.1, -3.4, ],
[8.2, 3.9, 2.5, 0.8, -0.5, -3.4, -23.7, -24.6, -22.0, -36.4, -28.8, -1.9, 27.7, 21.0, 8.4, 1.2, ],
[11.4, 9.3, 7.5, 4.1, -3.4, -22.0, -23.7, -14.4, -38.1, -25.4, -40.7, -22.6, 10.8, 11.6, 12.2, 3.4, ],
[8.0, 10.3, 13.6, 7.2, -17.5, -22.8, -36.3, -38.1, -26.3, -41.5, -46.0, -27.0, -11.5, 10.5, 12.2, 6.4, ],
[6.8, 12.2, 16.9, 0.1, -10.1, -28.7, -31.7, -38.1, -33.9, -44.1, -44.1, -42.6, -23.6, -20.2, -0.2, 3.6, ],
[1.6, 14.5, 0.4, 3.8, 2.1, -13.8, -22.0, -30.5, -32.2, -39.0, -20.3, -35.9, -33.9, -23.4, -26.7, -2.5, ],
],
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -0.8, -0.8, -0.8, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -0.8, -0.8, -0.8, 0.0, -0.1, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -1.4, -1.7, -1.7, -1.5, -1.5, -0.6, -1.2, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, 2.5, -0.3, -0.3, 2.3, 0.3, -0.8, -1.7, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 3.4, 8.9, 6.2, 3.5, 1.9, 1.1, 1.1, 0.5, -1.7, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 0.0, 1.9, 6.6, 13.4, 12.4, 4.2, 1.0, 0.8, -0.3, 0.5, 0.5, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 1.8, 12.7, 10.6, 11.1, 9.0, 3.1, -1.8, 1.0, 0.6, -0.5, -0.8, -0.8, 0.0, ],
[1.4, 0.0, 0.0, 11.5, 9.0, 9.7, 7.8, 4.8, -0.4, -3.4, -1.2, 0.2, 2.5, -1.7, -2.5, -1.7, ],
[5.5, 2.6, 2.8, 10.6, 9.7, 7.9, 4.0, -1.1, -25.2, -4.8, -2.0, -1.5, -0.1, 1.1, -2.5, -2.5, ],
[9.0, 4.3, 5.8, 4.9, 5.8, 3.8, -1.9, -23.5, -26.3, -22.2, -8.1, 12.6, 13.1, 6.0, -1.1, -3.4, ],
[14.6, 7.8, 3.2, -1.0, -3.0, -5.0, -26.6, -27.1, -26.3, -38.1, -28.8, -1.9, 27.7, 21.0, 8.4, 1.2, ],
[16.6, 12.7, 8.8, 2.8, -5.9, -24.6, -26.3, -16.9, -39.8, -27.1, -40.7, -22.6, 10.8, 11.6, 12.2, 3.4, ],
[11.8, 13.1, 15.8, 6.7, -19.1, -23.7, -37.1, -38.1, -26.3, -41.5, -46.0, -27.0, -11.5, 10.5, 12.2, 6.4, ],
[9.1, 13.6, 16.9, 0.1, -10.1, -28.7, -31.7, -38.1, -33.9, -44.1, -44.1, -42.6, -23.6, -20.2, -0.2, 3.6, ],
[1.6, 14.5, 0.4, 3.8, 2.1, -13.8, -22.0, -30.5, -32.2, -39.0, -20.3, -35.9, -33.9, -23.4, -26.7, -2.5, ],
],
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -0.8, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -1.7, -1.7, -1.7, -1.7, -0.8, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -0.8, -1.7, -1.7, -1.7, -0.8, 0.0, -0.1, 0.0, 0.0, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.7, -2.3, -2.5, -1.7, -1.5, -1.5, -0.6, -1.2, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.7, 1.6, -1.2, -0.3, 2.3, 0.3, -0.8, -1.7, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 3.4, 8.0, 5.4, 2.7, 1.9, 1.1, 1.1, 0.5, -1.7, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 0.0, 1.9, 6.6, 13.4, 11.5, 3.4, 1.0, 0.8, -0.3, 0.5, 0.5, -0.8, -0.8, ],
[0.0, 0.0, 0.0, 1.8, 12.7, 15.3, 13.9, 8.2, 2.3, -1.8, 1.0, 0.6, -0.5, -0.8, -0.8, 0.0, ],
[1.4, 0.0, 0.0, 11.5, 11.1, 12.5, 10.6, 4.8, -1.2, -3.4, -1.2, 0.2, 2.5, -1.7, -2.5, -1.7, ],
[5.5, 2.6, 2.8, 13.6, 13.9, 10.7, 6.8, 0.0, -26.0, -4.8, -2.0, -1.5, -0.1, 1.1, -2.5, -2.5, ],
[9.0, 4.3, 5.8, 8.8, 9.9, 8.0, 0.5, -24.0, -27.1, -22.2, -8.1, 12.6, 13.1, 6.0, -1.1, -3.4, ],
[16.0, 8.0, 2.3, -1.9, -3.8, -5.9, -27.4, -28.0, -26.3, -38.1, -28.8, -1.9, 27.7, 21.0, 8.4, 1.2, ],
[19.4, 13.7, 7.2, 1.1, -7.6, -25.4, -26.3, -17.8, -39.8, -27.1, -40.7, -22.6, 10.8, 11.6, 12.2, 3.4, ],
[14.6, 14.7, 15.4, 5.8, -19.1, -24.5, -37.9, -38.1, -26.3, -41.5, -46.0, -27.0, -11.5, 10.5, 12.2, 6.4, ],
[10.5, 15.0, 16.9, 0.1, -10.9, -29.6, -31.7, -38.1, -33.9, -44.1, -44.1, -42.6, -23.6, -20.2, -0.2, 3.6, ],
[1.6, 14.5, 1.8, 4.9, 2.0, -14.6, -22.0, -30.5, -32.2, -39.0, -20.3, -35.9, -33.9, -23.4, -26.7, -2.5, ],
],
[[0.0, 0.0, 0.0, 0.0, -0.8, -2.5, -3.4, -4.2, -4.2, -1.7, -2.5, -1.7, -1.7, -0.8, 0.0, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -3.4, -4.2, -5.1, -4.2, -3.4, -2.5, -2.5, -3.4, -2.5, -0.8, 0.0, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -2.5, -4.2, -5.1, -4.2, -2.5, -3.4, -2.7, -3.4, -2.5, -2.5, -1.7, ],
[0.0, 0.0, 0.0, 0.0, 0.0, -1.7, -4.2, -5.7, -5.1, -4.2, -4.0, -4.9, -3.1, -4.6, -2.5, -3.4, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -4.2, -1.8, -3.7, -2.9, -0.2, -3.1, -3.4, -3.4, -3.4, -2.5, ],
[0.0, 0.0, 0.0, 0.0, 0.0, 3.4, 6.3, 2.0, 1.0, -1.5, -2.3, -1.5, -1.2, -4.2, -2.5, -3.4, ],
[0.0, 0.0, 0.0, 0.0, 1.9, 6.6, 12.6, 8.1, 1.7, -1.5, -1.7, -2.0, -2.0, -1.2, -3.4, -2.5, ],
[0.0, 0.0, 0.0, 1.8, 12.7, 18.6, 13.9, 5.6, -0.3, -5.2, -0.7, -1.1, -3.0, -2.5, -2.5, -1.7, ],
[1.4, 0.0, 0.0, 11.5, 12.9, 15.2, 10.6, 2.2, -4.6, -6.8, -2.9, -1.5, 0.8, -2.5, -3.4, -2.5, ],
[5.5, 2.6, 2.8, 13.6, 19.0, 12.1, 9.6, -0.8, -28.6, -6.5, -3.7, -2.3, -0.9, 0.3, -2.5, -2.5, ],
[9.0, 4.3, 5.8, 13.7, 14.1, 10.8, 1.4, -24.8, -27.1, -22.2, -8.1, 12.6, 13.1, 6.0, -1.1, -3.4, ],
[16.6, 7.6, 0.6, -1.6, -4.2, -6.2, -27.7, -30.4, -26.3, -38.1, -28.8, -1.9, 27.7, 21.0, 8.4, 1.2, ],
[19.9, 13.4, 5.5, -1.5, -10.1, -27.1, -28.0, -18.6, -39.8, -27.1, -40.7, -22.6, 10.8, 11.6, 12.2, 3.4, ],
[16.5, 16.2, 14.9, 5.3, -20.8, -25.4, -39.6, -38.1, -26.3, -41.5, -46.0, -27.0, -11.5, 10.5, 12.2, 6.4, ],
[11.0, 16.4, 19.6, 0.6, -11.8, -31.3, -32.5, -38.1, -33.9, -44.1, -44.1, -42.6, -23.6, -20.2, -0.2, 3.6, ],
[6.0, 17.3, 3.2, 6.1, 2.5, -15.1, -22.0, -30.5, -32.2, -39.0, -20.3, -35.9, -33.9, -23.4, -26.7, -2.5, ],
]
	]

	visited = [
		[[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[-128, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
],
[[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[-128, 0, ],
[0, 3, ],
[0, 2, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
],
[[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[-128, 0, ],
[0, 3, ],
[0, 2, ],
[0, 3, ],
[-128, 1, ],
[-64, 0, ],
[64, 0, ],
[0, 0, ],
[0, 0, ],
],
[[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[-128, 0, ],
[0, 3, ],
[0, 2, ],
[0, 3, ],
[-128, 1, ],
[-64, 0, ],
[-64, 7, ],
[-64, 1, ],
[0, 0, ],
],
[[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[-128, 0, ],
[0, 3, ],
[0, 2, ],
[0, 3, ],
[-128, 1, ],
[-64, 6, ],
[-64, 7, ],
[-64, 1, ],
[0, 0, ],
],
[[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[-128, 0, ],
[0, 3, ],
[0, 2, ],
[0, 3, ],
[-128, 1, ],
[-64, 6, ],
[-64, 7, ],
[-64, 1, ],
[0, 0, ],
],
[[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[-128, 0, ],
[0, 3, ],
[0, 2, ],
[-128, 3, ],
[-128, 1, ],
[-64, 6, ],
[-64, 7, ],
[-64, 1, ],
[0, 0, ],
],
[[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[0, 0, ],
[-128, 0, ],
[0, 3, ],
[-128, 2, ],
[-128, 3, ],
[-128, 1, ],
[-64, 6, ],
[-64, 7, ],
[-64, 1, ],
[0, 0, ],
]
	]

	print(len(pos))
	print(len(maps))

	for i in range(len(maps)):
		plt.figure(figsize=(5,5))
		map_plot(maps[i], i)
		visit_plot(visited[i], i)
		pos_plot(pos[i], exPos[i])
		plt.legend(loc='lower left')
		plt.savefig(f'Figures/explorer{i}.png', format='png')

	#full = np.concatenate((maps[7], maps[11]))
	plt.figure(figsize=(5,5))
	map_plot(maps[-1], -1)
	visit_plot(visited[-1], -1)
	path_plot(np.array(pos))
	plt.legend(loc='lower left')
	plt.savefig(f'Figures/explorer_full.png', format='png')
	

paths()
#plt.show()