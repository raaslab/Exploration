
(cl:in-package :asdf)

(defsystem "roboclaw-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "motor_state" :depends-on ("_package_motor_state"))
    (:file "_package_motor_state" :depends-on ("_package"))
  ))