"""Regenerate the 3D emblem's white shapes from the supplied favicon (requires Pillow)."""
from pathlib import Path
import json
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
image = Image.open(ROOT / 'resources/Favicon.png').convert('RGBA')
pixels = image.load()
width, height = image.size
white = {(x, y) for y in range(height) for x in range(width)
         if min(pixels[x, y][:3]) > 190 and pixels[x, y][3] > 128}
edges = {}
for x, y in white:
    for neighbor, a, b in [((x, y-1), (x, y), (x+1, y)),
                            ((x+1, y), (x+1, y), (x+1, y+1)),
                            ((x, y+1), (x+1, y+1), (x, y+1)),
                            ((x-1, y), (x, y+1), (x, y))]:
        if neighbor not in white:
            edges[a] = b

def simplify(points, epsilon):
    if len(points) < 3:
        return points
    a, b = points[0], points[-1]
    dx, dy = b[0]-a[0], b[1]-a[1]
    length = max((dx*dx+dy*dy)**.5, .0001)
    distances = [abs(dy*(p[0]-a[0])-dx*(p[1]-a[1]))/length for p in points]
    distance = max(distances)
    index = distances.index(distance)
    if distance > epsilon:
        return simplify(points[:index+1], epsilon)[:-1] + simplify(points[index:], epsilon)
    return [a, b]

loops = []
while edges:
    start = next(iter(edges))
    points, point = [], start
    while point in edges:
        points.append(point)
        point = edges.pop(point)
        if point == start:
            break
    if len(points) > 50:
        # Split the closed outline before simplifying to retain its full silhouette.
        middle = len(points)//2
        points = simplify(points[:middle+1], .8)[:-1] + simplify(points[middle:]+[points[0]], .8)[:-1]
        loops.append([[round((x-width/2)/width*4, 5), round((height/2-y)/height*4, 5)] for x,y in points])
(ROOT / 'resources/emblem-shapes.json').write_text(json.dumps(loops, separators=(',', ':'))+'\n')
print(f'Traced {len(loops)} emblem shapes')
