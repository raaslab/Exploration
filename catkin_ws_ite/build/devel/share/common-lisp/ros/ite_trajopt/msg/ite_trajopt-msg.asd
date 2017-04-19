
(cl:in-package :asdf)

(defsystem "ite_trajopt-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "StatesControls" :depends-on ("_package_StatesControls"))
    (:file "_package_StatesControls" :depends-on ("_package"))
  ))