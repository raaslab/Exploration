std_msgs/Header header # Contains plan number and planning start time
string planner_type
float64 duration       # How long to plan (sec)

# Plan parameters used by InfoPlanner
float64 lethal_occ_dist
int64 num_angles
float64 eval_res
float64 min_info
float64 min_ttl_info
float64 max_seg_length
float64 max_seg_angle

float64 min_distance   # Minimum distance used to make trajectories
float64 max_distance   # Maximum distance used to make trajectories

# Trajectories
ite_command/TrajectoryData[] trajectories
