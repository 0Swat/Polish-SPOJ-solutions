def is_acute_triangle(p1, p2, p3):
    def squared_distance(a, b):
        return (a[0] - b[0])**2 + (a[1] - b[1])**2
    
    a2 = squared_distance(p2, p3)
    b2 = squared_distance(p1, p3)
    c2 = squared_distance(p1, p2)
    
    return (a2 + b2 > c2) and (a2 + c2 > b2) and (b2 + c2 > a2)

def solve_triangle_fields(input_data):
    import sys
    input = sys.stdin.read
    data = input_data.split()
    
    index = 0
    D = int(data[index])
    index += 1
    results = []
    
    for _ in range(D):
        N = int(data[index])
        index += 1
        points = []
        for i in range(N):
            x = int(data[index])
            y = int(data[index + 1])
            points.append((x, y, i + 1))  # Store with 1-based index
            index += 2
        
        points.sort()
        
        triangles = []
        for i in range(0, N, 3):
            p1, p2, p3 = points[i], points[i+1], points[i+2]
            if is_acute_triangle(p1, p2, p3):
                triangles.append(sorted([p1[2], p2[2], p3[2]]))
        
        results.append(triangles)
    
    output = []
    for result in results:
        for triangle in result:
            output.append(" ".join(map(str, triangle)))
        output.append("")  # Separate different datasets by a blank line
    
    return "\n".join(output)

# Example usage:
input_data = "2\n3\n0 0\n1 2\n2 1\n6\n-2 0\n2 0\n1 1\n-1 1\n0 3\n0 4\n"
print(solve_triangle_fields(input_data))
