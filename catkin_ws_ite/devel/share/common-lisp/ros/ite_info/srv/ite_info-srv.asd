
(cl:in-package :asdf)

(defsystem "ite_info-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
)
  :components ((:file "_package")
    (:file "orienteering" :depends-on ("_package_orienteering"))
    (:file "_package_orienteering" :depends-on ("_package"))
    (:file "generate_grid" :depends-on ("_package_generate_grid"))
    (:file "_package_generate_grid" :depends-on ("_package"))
  ))