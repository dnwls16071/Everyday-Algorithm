# [".#...", "..#..", "...#."]
def solution(wallpaper):
    ROW = len(wallpaper[0])
    COL = len(wallpaper)

    location_x = []
    location_y = []
    for i in range(COL):
         for j in range(ROW):
            if wallpaper[i][j] == "#":
                location_x.append(j)
                location_y.append(i)
    return [min(location_y), min(location_x), max(location_y)+1, max(location_x)+1]