
(cl:in-package :asdf)

(defsystem "ite_grid-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :std_msgs-msg
)
  :components ((:file "_package")
    (:file "VoxelGrid" :depends-on ("_package_VoxelGrid"))
    (:file "_package_VoxelGrid" :depends-on ("_package"))
  ))