from numpy import *

def compute_error_for_line_given_points(points_array, a, b):
    totalError = 0
    pionts_array_len = len(points_array)
    for i in range(0, pionts_array_len):
        x = points_array[i, 0]
        y = points_array[i, 1]
        totalError += (y - (a * x + b)) ** 2
    return totalError / pionts_array_len

#y = ax + b
def step_gradient(points_array, a, b, learning_rate):
	m = len(points_array)
	a_gradient = 0
	b_gradient = 0
	for i  in range(m):
		x = points_array[i, 0]
		y = points_array[i, 1]
		a_gradient += -(1/m) * learning_rate * (a * x + b - y) * x
		b_gradient += -(1/m) * learning_rate * (a * x + b - y)
	a += a_gradient
	b += b_gradient
	return [a, b]

def gradient_descent_runner(points_array, init_a, init_b, learning_rate, iteration_nums):
	a = init_a
	b = init_b
	for i in range(iteration_nums):
		a, b = step_gradient(array(points_array), a, b, learning_rate)
	return [a, b]

def run():
	points_array = genfromtxt("data.csv", delimiter=",")
	learning_rate = 0.0001
	init_a = 0
	init_b = 0
	iteration_nums = 10000
	print("running...")
	[a, b] = gradient_descent_runner(points_array, init_a, init_b, learning_rate, iteration_nums)
	print([a, b])
	print ("After {0} iterations b = {1}, m = {2}, error = {3}".format(iteration_nums, a, b, compute_error_for_line_given_points(points_array, a, b)))

if __name__ == '__main__':
	run()