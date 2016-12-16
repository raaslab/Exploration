#include <ros/ros.h>
#include <nav_msgs/OccupancyGrid.h>
#include "tf/transform_broadcaster.h"
#include "tf/transform_listener.h"
#include <occupancy_grid_utils/combine_grids.h>
#include "stdio.h"
#include <ros/console.h>

/// This file merges two occupancy grids

nav_msgs::OccupancyGrid::ConstPtr map1;
nav_msgs::OccupancyGrid::ConstPtr map2;
bool newMap1 = false;
bool newMap2 = false;
bool eachMapReceivedOnce = false;
typedef boost::shared_ptr<nav_msgs::OccupancyGrid> GridPtr;
typedef boost::shared_ptr<nav_msgs::OccupancyGrid const> GridConstPtr;
void map1Callback(const nav_msgs::OccupancyGrid::ConstPtr &msg) {
    map1 = msg;
    //ROS_ERROR_STREAM("This is my index:" << msg->data);
    //ROS_INFO("I heard: [%s]", msg->data.c_str());
    newMap1 = true;
}

void map2Callback(const nav_msgs::OccupancyGrid::ConstPtr &msg) {
    map2 = msg;
    newMap2 = true;
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "mergeMap");

    ros::NodeHandle n;
    ros::Publisher map_pub = n.advertise<nav_msgs::OccupancyGrid>("/projected_map", 10);
    ros::Subscriber map1_sub = n.subscribe("/robot1/map", 10, map1Callback);
    ros::Subscriber map2_sub = n.subscribe("/robot2/map", 10, map2Callback);
    tf::TransformListener listener;
    //ROS_ERROR_STREAM("This is my index:");
    //std::out << "Output sentence";
    ros::Rate r(5.0);

    while(n.ok()){
        if (newMap1 && newMap2) {
            eachMapReceivedOnce = true;
        }

        if(eachMapReceivedOnce && (newMap1 || newMap2)){
            std::vector<nav_msgs::OccupancyGrid::ConstPtr> grids(2);
            nav_msgs::OccupancyGrid::ConstPtr mapOut;

            //TODO, move origin of map to align them
            GridPtr mapint1(new nav_msgs::OccupancyGrid());
            GridPtr mapint2(new nav_msgs::OccupancyGrid());
            
            
            
            mapint1->info=map1->info;
            mapint1->header=map1->header;
            mapint1->data=map1->data;
            mapint1->info.origin.orientation.w = 1;
            mapint2->info=map2->info;
            mapint2->header=map2->header;
            mapint2->data=map2->data;
            mapint2->info.origin.orientation.w = 1;
            ROS_ERROR_STREAM("This is my width: " <<  mapint1->info);
            //map1->info.origin.orientation.w = 1;
            //map2->info.origin.orientation.w = 1;
            grids[0] = mapint1;
            grids[1] = mapint2;
            ROS_ERROR_STREAM("This is my width: " <<  map1->info.origin.orientation.w);
            ROS_ERROR_STREAM("This is my width: " <<  map2->info.origin.orientation.w);
            mapOut = occupancy_grid_utils::combineGrids(grids,0.125);
            //ROS_ERROR_STREAM("This is my width: " <<  mapOut->info);
            map_pub.publish(mapOut);
            r.sleep();
            newMap1 = false;
            newMap2 = false;
        }

        ros::spinOnce();
        r.sleep();
    }
}