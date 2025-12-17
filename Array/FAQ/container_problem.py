def maxArea(height):
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # caculate width
        _width = right - left

        # calculate height
        _height = min(height[left], height[right])

        # get max_area
        max_area = max(max_area, _height*_width) # area => _height * _width

        # move the pointer to get max height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    # return maximum area which we calculated 
    return max_area

# Helper to test
if __name__ == "__main__":
    heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Max Area: {maxArea(heights)}") # Expected: 49