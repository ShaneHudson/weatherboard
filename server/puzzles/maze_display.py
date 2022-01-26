import random
import heapq
import matplotlib.pyplot as plt

class MazePlot:
	"""
	https://github.com/lvngd/mazes/
	generates the matplotlib visualization from a maze_object - instance of Maze class

	"""
	def __init__(self,width,height, maze_object,path=None,maze_line_color="black",maze_name="untitled",random_entry_exits=True):
		self.width = width
		self.height = height
		self.maze_name = maze_name

		#maze colors
		self.maze_line_color = maze_line_color
		self.maze_line_width = 1
		self.entry_square_color = "blue"
		self.exit_square_color = "red"
		self.exit_square_alpha = 0
		self.path_square_color = "#717D7E"
		self.path_square_alpha = 0

		self.maze = maze_object
		self.edges = self.maze.maze
		self.path = path
		self.fig,self.ax = self.create_plot()
		self.entry_exit_points,self.entry_exit_edges = self.get_entry_exits()
		self.draw_maze_walls()

	def clear_maze(self):
		#clears previous path drawn on the maze
		[p.remove() for p in reversed(self.ax.patches)]
		self.draw_entry_exits()
		return

	def save_as_image(self):
		plt.savefig("puzzle.png", bbox_inches='tight', pad_inches=0, transparent=True)
		return

	def create_plot(self):
		fig = plt.figure(figsize = (1,1*self.height/self.width), frameon=False)
		ax = plt.axes()
		ax.set_axis_off()
		return fig,ax

	def get_edge_locations(self):
		"""
		get x and y data for matplotlib 2D lines that are legal edges and should not be colored in on plot
		"""
		edge_data = []
		for edge in sorted(self.edges):
			e1 = edge[0]
			e2 = edge[1]
			if e1[0] == e2[0]:
				#x is the same, draw edge between the 2 y values
				if e1[1] > e2[1]:
					#if the y value of the first coordinate is greater, need a left edge
					edge_data.append([[e1[1],e1[1]],[e1[0]+1,e1[0]]])					
				else:
					#need a right edge
					edge_data.append([[e1[1]+1,e1[1]+1],[e1[0],e1[0]+1]])
			if e1[1] == e2[1]:
				#y is the same, draw edge between 2 x values
				if e1[0] > e2[0]:
					#need a top edge
					edge_data.append([[e1[1],e1[1]+1],[e1[0],e1[0]]])
				else:
					#bottom edge
					edge_data.append([[e1[1]+1,e1[1]],[e1[0]+1,e1[0]+1]])
		#add entry/exit edges to those that should not be filled in
		edge_data.extend(self.entry_exit_edges)
		return edge_data

	def draw_maze_walls(self):
		"""draw the maze walls - draws all edges of the matrix except for the ones in the spanning tree and the entry/exits"""
		edge_data = self.get_edge_locations()
		for i in range(self.height):
			for j in range(self.width):
				top_edge = [[j,j+1],[i,i]]
				if top_edge in edge_data:
					pass
				elif [[j+1,j],[i,i]] in edge_data:
					pass
				else:
					self.ax.plot([j,j+1],[i,i],color=self.maze_line_color,linewidth=self.maze_line_width)
				bottom_edge = [[j+1,j],[i+1,i+1]]
				if bottom_edge in edge_data:
					pass
				elif [[j,j+1],[i+1,i+1]] in edge_data:
					pass
				else:
					self.ax.plot([j+1,j],[i+1,i+1],color=self.maze_line_color,linewidth=self.maze_line_width)
				right_edge = [[j+1,j+1],[i,i+1]]
				if right_edge in edge_data:
					pass
				elif [[j+1,j+1],[i+1,i]] in edge_data:
					pass
				else:
					self.ax.plot([j+1,j+1],[i,i+1],color=self.maze_line_color,linewidth=self.maze_line_width)
				left_edge = [[j,j],[i+1,i]]
				if left_edge in edge_data:
					pass
				elif [[j,j],[i,i+1],] in edge_data:
					pass
				else:
					self.ax.plot([j,j],[i+1,i],color=self.maze_line_color,linewidth=self.maze_line_width)
		return

	def draw_entry_exits(self):
		for count,pt in enumerate(self.entry_exit_points):
			if count == 0:
				square = plt.Rectangle((pt[1],pt[0]),1,1,fc=self.entry_square_color,alpha=1.0)
				self.ax.add_patch(square)
			else:
				square = plt.Rectangle((pt[1],pt[0]),1,1,fc=self.exit_square_color,alpha=self.exit_square_alpha)
				self.ax.add_patch(square)

	def get_entry_exits(self):
		"""entry and exit points in the maze - entry on one side and one exit on each other side"""
		entry_exit_edge_data = []
		p1 = (0,random.randint(0,self.width-1))
		#currently want the exits to be in the top half of the wall for side exit
		half_h = self.height //2
		p2 = (random.randint(half_h,self.height-1),0)
		p3 = (self.height-1,(random.randint(0,self.height-1)))
		#top half of the wall for the side exit
		half_w = self.width //2
		p4 = (random.randint(half_w,self.width-1), self.height-1)
		entry_exit_edge_data.append([[p1[1],p1[1]+1],[p1[0],p1[0]]]) #bottom edge
		entry_exit_edge_data.append([[p2[1],p2[1]],[p2[0]+1,p2[0]]]) #left edge
		entry_exit_edge_data.append([[p3[1],p3[1]+1],[p3[0]+1,p3[0]+1]]) #top edge
		entry_exit_edge_data.append([[p4[1]+1,p4[1]+1],[p4[0],p4[0]+1]]) #right edge
		#squares of entry/exit locations
		self.entry_exit_points = [p1,p2,p3,p4]
		self.draw_entry_exits()
		return self.entry_exit_points,entry_exit_edge_data