std_msgs/Header header
geometry_msgs/Point origin
uint32 num_x
uint32 num_y
uint32 num_z
float32 resolution
# Subscript (xi, yi, zi) indexes probability[xi + num_x * yi + zi * num_x * num_y] 
# represents (origin.x + xi * resolution, origin.y + yi * resolution, origin.z + zi * resolution)
uint8[] probability
