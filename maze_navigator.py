import curses
from curses import wrapper
import queue
import time
maze=[
    ["|","|","|","|","|","O","|","|","|"],
    ["|"," "," "," "," "," "," "," ","|"],
    ["|"," ","|","|"," ","|","|"," ","|"],
    ["|"," ","|"," "," "," ","|"," ","|"],
    ["|"," ","|"," ","|"," ","|"," ","|"],
    ["|"," ","|"," ","|"," ","|"," ","|"],
    ["|"," ","|"," ","|"," ","|","|","|"],
    ["|"," "," "," "," "," "," "," ","|"],
    ["|","|","|","|","|","|","|","X","|"],
]
def print_maze(maze,stdscr,path=[]):
    GREEN =curses.color_pair(1)
    YELLOW = curses.color_pair(2)
    
    for i , row in enumerate(maze):
        for j,value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"X",GREEN)
            else:
                stdscr.addstr(i,j*2,value,YELLOW)
                
                
def find_start(maze,start):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == start:
                return i,j
    return None

def find_path(maze,stdscr):
    start ="O"
    end="X"
    start_pos = find_start(maze,start)
    
    q=queue.Queue()
    q.put((start_pos,[start_pos]))
    visited = set()
    
    while not q.empty():
        current_pos,path=q.get()
        row,col=current_pos
        
        stdscr.clear()
        
        print_maze(maze,stdscr,path)
        time.sleep(0.2)
        stdscr.refresh()
        
        if maze[row][col]==end:
            return path
        
        adjcents=find_adjcents(maze,row,col)
        for adjcent in adjcents:
            if adjcent  in visited:
                continue
            r,c=adjcent
            if maze[r][c] == "#":
                continue
            new_path=path+[adjcent]
            q.put((adjcent,path+[adjcent]))
            visited.add(adjcent)
                
def find_adjcents(maze,row,col):
    adjcents=[]
#upward 
    if row>0:
        adjcents.append((row-1,col))
#downward
    if row+1<len(maze):
        adjcents.append((row+1,col))
#left-direction
    if col>0:
        adjcents.append((row,col-1))
#right-direction
    if col+1<len(maze[0]):
        adjcents.append((row,col+1))
    return adjcents

def main (stdscr):
    curses.init_pair(1,curses.COLOR_GREEN,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_YELLOW,curses.COLOR_BLACK)
    
    find_path(maze,stdscr)

    stdscr.getch() #getting a single character from the user by user

wrapper(main)
    