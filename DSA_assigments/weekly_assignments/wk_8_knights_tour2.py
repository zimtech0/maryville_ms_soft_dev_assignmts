# create a python program representing the Knight Tour

# import module
import sys

# create class
class KnightsTour:
    def __init__(self, width, height): # constructor with parameters
        self.w = width
        self.h = height

        self.board = []
        self.generate_board()

    def generate_board(self): # create board
        
       
        
        for i in range(self.h):  # nested list to mimic game board
            self.board.append([0]*self.w)

    def print_board(self): #create visual representation of board
        print ("  ")
        print("Start of Board Representation")
        print ("------")
       
        for elem in self.board:
            print (elem)
        print ("------")
        print("End of Board Representation")
        print ("  ")

    def generate_legal_moves(self, cur_pos): #list of legal moves that knight can take next
        
        
        possible_pos = []
        move_offsets = [(1, 2), (1, -2), (-1, 2), (-1, -2),
                        (2, 1), (2, -1), (-2, 1), (-2, -1)]

        for move in move_offsets:
            new_x = cur_pos[0] + move[0]
            new_y = cur_pos[1] + move[1]

            if (new_x >= self.h):
                continue
            elif (new_x < 0):
                continue
            elif (new_y >= self.w):
                continue
            elif (new_y < 0):
                continue
            else:
                possible_pos.append((new_x, new_y))

        return possible_pos

        #It is most efficient to visit the lonely neighbors first, 
        #since these are at the edges of the chessboard and cannot 
        #be reached easily if done later in the traversing the DS
    def sort_lonely_neighbors(self, to_visit):
        
        neighbor_list = self.generate_legal_moves(to_visit)
        empty_neighbours = []

        for neighbor in neighbor_list:
            np_value = self.board[neighbor[0]][neighbor[1]]
            if np_value == 0:
                empty_neighbours.append(neighbor)

        scores = []
        for empty in empty_neighbours:
            score = [empty, 0]
            moves = self.generate_legal_moves(empty)
            for m in moves:
                if self.board[m[0]][m[1]] == 0:
                    score[1] += 1
            scores.append(score)

        scores_sort = sorted(scores, key = lambda s: s[1])
        sorted_neighbours = [s[0] for s in scores_sort]
        return sorted_neighbours
    
        
        # Recursive definition of knights tour use the following inputs:
        # n = current depth of search tree
        # path = current path taken
        # to_visit = node to visit

    def tour(self, n, path, to_visit):
        
        self.board[to_visit[0]][to_visit[1]] = n
        path.append(to_visit) #append the newest vertex to the current point
        print ("Currently Visiting Position: ", to_visit)

        if n == self.w * self.h: #if every grid is filled
            self.print_board()
            print('Route Taken By Knight To Complete Board:\n ','_____________',path,'____________')
            print("\nTour Completed!")
            sys.exit(1)

        else:
            sorted_neighbours = self.sort_lonely_neighbors(to_visit)
            for neighbor in sorted_neighbours:
                self.tour(n+1, path, neighbor)

            #If we exit this loop, all neighbours failed so reset
            self.board[to_visit[0]][to_visit[1]] = 0
            try:
                path.pop()
                print("Going back: ", path[-1])
            except IndexError:
                print("No valid path found")
                sys.exit(1)

def main():
    kt = KnightsTour(8, 8)  #Define the size of grid (8x8)
    kt.tour(1, [], (0,0))
    kt.print_board()

if __name__ == '__main__':
    main()
   