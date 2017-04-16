'''
Copyright (c) 2011-2017, Agora Games, LLC All rights reserved.

https://github.com/agoragames/haigha/blob/master/LICENSE.txt
'''

from chai import Chai

from haigha2.frames import heartbeat_frame
from haigha2.frames.heartbeat_frame import HeartbeatFrame
from haigha2.frames.frame import Frame


class HeartbeatFrameTest(Chai):

    def test_type(self):
        assert_equals(8, HeartbeatFrame.type())

    def test_parse(self):
        frame = HeartbeatFrame.parse(42, 'payload')
        assert_true(isinstance(frame, HeartbeatFrame))
        assert_equals(42, frame.channel_id)

    def test_write_frame(self):
        w = mock()
        expect(mock(heartbeat_frame, 'Writer')).args('buffer').returns(w)
        expect(w.write_octet).args(8).returns(w)
        expect(w.write_short).args(42).returns(w)
        expect(w.write_long).args(0).returns(w)
        expect(w.write_octet).args(0xce)

        frame = HeartbeatFrame(42)
        frame.write_frame('buffer')
