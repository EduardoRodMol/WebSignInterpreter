from streamlit_webrtc import (
    RTCConfiguration
)

local_turn = "turn:localhost:3478"
local_stun = "stun:localhost:3478"
google_stun = "stun:stun.l.google.com:19302"

RTC_CONFIGURATION = RTCConfiguration(
    {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
)

#STUN servers to get the IP address of your computer, 
#and TURN servers to function as relay servers in case peer-to-peer communication fails.
# (WebRTC in the real world explains in more detail.)