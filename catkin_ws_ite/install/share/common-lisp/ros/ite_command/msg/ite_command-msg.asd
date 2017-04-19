
(cl:in-package :asdf)

(defsystem "ite_command-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :ite_trajopt-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ExploreSystemData" :depends-on ("_package_ExploreSystemData"))
    (:file "_package_ExploreSystemData" :depends-on ("_package"))
    (:file "TrajectoryData" :depends-on ("_package_TrajectoryData"))
    (:file "_package_TrajectoryData" :depends-on ("_package"))
    (:file "TeamActions" :depends-on ("_package_TeamActions"))
    (:file "_package_TeamActions" :depends-on ("_package"))
    (:file "PlanData2" :depends-on ("_package_PlanData2"))
    (:file "_package_PlanData2" :depends-on ("_package"))
    (:file "RobotActions" :depends-on ("_package_RobotActions"))
    (:file "_package_RobotActions" :depends-on ("_package"))
    (:file "PlanData" :depends-on ("_package_PlanData"))
    (:file "_package_PlanData" :depends-on ("_package"))
    (:file "InfoTraj" :depends-on ("_package_InfoTraj"))
    (:file "_package_InfoTraj" :depends-on ("_package"))
    (:file "InfoPath" :depends-on ("_package_InfoPath"))
    (:file "_package_InfoPath" :depends-on ("_package"))
  ))