
(cl:in-package :asdf)

(defsystem "mesh80211s-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "MeshStation" :depends-on ("_package_MeshStation"))
    (:file "_package_MeshStation" :depends-on ("_package"))
    (:file "MeshStations" :depends-on ("_package_MeshStations"))
    (:file "_package_MeshStations" :depends-on ("_package"))
  ))