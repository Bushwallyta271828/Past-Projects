def grid_print(grid):
    for row in grid:
        to_print = ""
        for i, entry in enumerate(row[:-1]):
            to_print += str(entry) + " "
        to_print += str(row[-1])
        print to_print


def rectangles(grid):
	rects = 0
	zone_heights = [0 for i in range(len(grid) + 1)]
	last_seen_indices = [-1 for i in range(len(grid) + 1)]
	area_sums = [0 for i in range(len(grid) + 1)]
	heights = [0 for i in range(len(grid[0]))]
	for row in range(len(grid)):
		active_index = 0
		last_seen_indices[0] = -1
		for column in range(len(grid[0])):
			if grid[row][column] == 0:
				heights[column] = 0
				last_seen_indices[0] = column
				active_index = 0
			else: #grid[row][column] = 1
				heights[column] += 1
				if heights[column] > zone_heights[active_index]:
					active_index += 1
					zone_heights[active_index] = heights[column]
					last_seen_indices[active_index] = column
					area_sums[active_index] = area_sums[active_index - 1] + heights[column]
				elif heights[column] == zone_heights[active_index]:
					last_seen_indices[active_index] = column
					area_sums[active_index] += heights[column]
				else: #0 < heights[column] < zone_heights[active_index]:
					while zone_heights[active_index - 1] >= heights[column]:
						active_index -= 1
					zone_heights[active_index] = heights[column]
					last_seen_indices[active_index] = column
					area_sums[active_index] = area_sums[active_index - 1] + heights[column] * (column - last_seen_indices[active_index - 1])
			rects += area_sums[active_index]
	return rects

input_grid = [[0, 0, 0, 0], [0, 1, 1, 0], [1, 1, 1, 1], [1, 0, 1, 1]]
grid_print(input_grid)
print "\n\n"
print rectangles(input_grid)