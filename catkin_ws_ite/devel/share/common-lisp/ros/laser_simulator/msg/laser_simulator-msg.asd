
(cl:in-package :asdf)

(defsystem "laser_simulator-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :sensor_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "ScanPair" :depends-on ("_package_ScanPair"))
    (:file "_package_ScanPair" :depends-on ("_package"))
    (:file "PoseStampedNamed" :depends-on ("_package_PoseStampedNamed"))
    (:file "_package_PoseStampedNamed" :depends-on ("_package"))
    (:file "PoseStampedNamedArray" :depends-on ("_package_PoseStampedNamedArray"))
    (:file "_package_PoseStampedNamedArray" :depends-on ("_package"))
  ))