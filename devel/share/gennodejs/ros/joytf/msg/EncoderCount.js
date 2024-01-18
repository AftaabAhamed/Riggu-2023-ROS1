// Auto-generated. Do not edit!

// (in-package joytf.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class EncoderCount {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.Left_tick_count = null;
      this.right_tick_count = null;
    }
    else {
      if (initObj.hasOwnProperty('Left_tick_count')) {
        this.Left_tick_count = initObj.Left_tick_count
      }
      else {
        this.Left_tick_count = 0.0;
      }
      if (initObj.hasOwnProperty('right_tick_count')) {
        this.right_tick_count = initObj.right_tick_count
      }
      else {
        this.right_tick_count = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type EncoderCount
    // Serialize message field [Left_tick_count]
    bufferOffset = _serializer.float64(obj.Left_tick_count, buffer, bufferOffset);
    // Serialize message field [right_tick_count]
    bufferOffset = _serializer.float64(obj.right_tick_count, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type EncoderCount
    let len;
    let data = new EncoderCount(null);
    // Deserialize message field [Left_tick_count]
    data.Left_tick_count = _deserializer.float64(buffer, bufferOffset);
    // Deserialize message field [right_tick_count]
    data.right_tick_count = _deserializer.float64(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 16;
  }

  static datatype() {
    // Returns string type for a message object
    return 'joytf/EncoderCount';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '7f276c1d9cb78d3dadf8d8c2f65dfdbf';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float64 Left_tick_count
    float64 right_tick_count
    
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new EncoderCount(null);
    if (msg.Left_tick_count !== undefined) {
      resolved.Left_tick_count = msg.Left_tick_count;
    }
    else {
      resolved.Left_tick_count = 0.0
    }

    if (msg.right_tick_count !== undefined) {
      resolved.right_tick_count = msg.right_tick_count;
    }
    else {
      resolved.right_tick_count = 0.0
    }

    return resolved;
    }
};

module.exports = EncoderCount;
