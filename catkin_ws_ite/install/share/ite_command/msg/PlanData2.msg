std_msgs/Header header # Contains plan number and planning start time
string planner_type
float64 duration       # How long to plan (sec)

bool scarab            # True if planning for scarab
bool quad              # True if planning for quad

bool scarab_action     # True if generated action for scarab
bool quad_action       # True if generated action for quad

geometry_msgs/PoseArray[] scarab_trajs
geometry_msgs/PoseArray[] quad_trajs
