;; Auto-generated. Do not edit!


(when (boundp 'joytf::EncoderCount)
  (if (not (find-package "JOYTF"))
    (make-package "JOYTF"))
  (shadow 'EncoderCount (find-package "JOYTF")))
(unless (find-package "JOYTF::ENCODERCOUNT")
  (make-package "JOYTF::ENCODERCOUNT"))

(in-package "ROS")
;;//! \htmlinclude EncoderCount.msg.html


(defclass joytf::EncoderCount
  :super ros::object
  :slots (_Left_tick_count _right_tick_count ))

(defmethod joytf::EncoderCount
  (:init
   (&key
    ((:Left_tick_count __Left_tick_count) 0.0)
    ((:right_tick_count __right_tick_count) 0.0)
    )
   (send-super :init)
   (setq _Left_tick_count (float __Left_tick_count))
   (setq _right_tick_count (float __right_tick_count))
   self)
  (:Left_tick_count
   (&optional __Left_tick_count)
   (if __Left_tick_count (setq _Left_tick_count __Left_tick_count)) _Left_tick_count)
  (:right_tick_count
   (&optional __right_tick_count)
   (if __right_tick_count (setq _right_tick_count __right_tick_count)) _right_tick_count)
  (:serialization-length
   ()
   (+
    ;; float64 _Left_tick_count
    8
    ;; float64 _right_tick_count
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _Left_tick_count
       (sys::poke _Left_tick_count (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _right_tick_count
       (sys::poke _right_tick_count (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _Left_tick_count
     (setq _Left_tick_count (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _right_tick_count
     (setq _right_tick_count (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get joytf::EncoderCount :md5sum-) "7f276c1d9cb78d3dadf8d8c2f65dfdbf")
(setf (get joytf::EncoderCount :datatype-) "joytf/EncoderCount")
(setf (get joytf::EncoderCount :definition-)
      "float64 Left_tick_count
float64 right_tick_count


")



(provide :joytf/EncoderCount "7f276c1d9cb78d3dadf8d8c2f65dfdbf")


