std_msgs/Header header

string name # Robot's name
string local_planner # Name of local planner

geometry_msgs/PoseStamped pose # Robot's pose
TeamActions global_actions # Last global plan

InfoTraj global # Best global path
InfoTraj local # Best local trajectory
InfoTraj global_remainder # Local portion of global plan
InfoTraj optimized # Optimized version of global_remainder or local
bool optimize_local # If true, the local was optimized, otherwise global_remainder was
bool select_optimize # If true, optimized was selected over global

float64 optimization_duration # Time to run the SQP
float64 total_duration # Total time
