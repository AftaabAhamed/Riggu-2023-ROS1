; Auto-generated. Do not edit!


(cl:in-package joytf-msg)


;//! \htmlinclude EncoderCount.msg.html

(cl:defclass <EncoderCount> (roslisp-msg-protocol:ros-message)
  ((Left_tick_count
    :reader Left_tick_count
    :initarg :Left_tick_count
    :type cl:float
    :initform 0.0)
   (right_tick_count
    :reader right_tick_count
    :initarg :right_tick_count
    :type cl:float
    :initform 0.0))
)

(cl:defclass EncoderCount (<EncoderCount>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <EncoderCount>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'EncoderCount)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name joytf-msg:<EncoderCount> is deprecated: use joytf-msg:EncoderCount instead.")))

(cl:ensure-generic-function 'Left_tick_count-val :lambda-list '(m))
(cl:defmethod Left_tick_count-val ((m <EncoderCount>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joytf-msg:Left_tick_count-val is deprecated.  Use joytf-msg:Left_tick_count instead.")
  (Left_tick_count m))

(cl:ensure-generic-function 'right_tick_count-val :lambda-list '(m))
(cl:defmethod right_tick_count-val ((m <EncoderCount>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader joytf-msg:right_tick_count-val is deprecated.  Use joytf-msg:right_tick_count instead.")
  (right_tick_count m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <EncoderCount>) ostream)
  "Serializes a message object of type '<EncoderCount>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'Left_tick_count))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'right_tick_count))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <EncoderCount>) istream)
  "Deserializes a message object of type '<EncoderCount>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'Left_tick_count) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'right_tick_count) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<EncoderCount>)))
  "Returns string type for a message object of type '<EncoderCount>"
  "joytf/EncoderCount")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'EncoderCount)))
  "Returns string type for a message object of type 'EncoderCount"
  "joytf/EncoderCount")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<EncoderCount>)))
  "Returns md5sum for a message object of type '<EncoderCount>"
  "7f276c1d9cb78d3dadf8d8c2f65dfdbf")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'EncoderCount)))
  "Returns md5sum for a message object of type 'EncoderCount"
  "7f276c1d9cb78d3dadf8d8c2f65dfdbf")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<EncoderCount>)))
  "Returns full string definition for message of type '<EncoderCount>"
  (cl:format cl:nil "float64 Left_tick_count~%float64 right_tick_count~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'EncoderCount)))
  "Returns full string definition for message of type 'EncoderCount"
  (cl:format cl:nil "float64 Left_tick_count~%float64 right_tick_count~%~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <EncoderCount>))
  (cl:+ 0
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <EncoderCount>))
  "Converts a ROS message object to a list"
  (cl:list 'EncoderCount
    (cl:cons ':Left_tick_count (Left_tick_count msg))
    (cl:cons ':right_tick_count (right_tick_count msg))
))
