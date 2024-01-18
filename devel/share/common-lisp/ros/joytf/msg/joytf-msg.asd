
(cl:in-package :asdf)

(defsystem "joytf-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "EncoderCount" :depends-on ("_package_EncoderCount"))
    (:file "_package_EncoderCount" :depends-on ("_package"))
  ))