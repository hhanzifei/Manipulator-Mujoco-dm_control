import os
from manipulator_mujoco.robots.arm import Arm

_AIRBOT_XML = os.path.join(
    os.path.dirname(__file__),
    '../assets/robots/airbot/airbot_play_v3_0_gripper.xml',
)

_JOINTS = (
    'joint1',
    'joint2',
    'joint3',
    'joint4',
    'joint5',
    'joint6',
)

_EEF_SITE = 'eef_site'

_ATTACHMENT_SITE = 'attachment_site'

class AirBot(Arm):
    def __init__(self, name: str = None):
        super().__init__(_AIRBOT_XML, _EEF_SITE, _ATTACHMENT_SITE, _JOINTS, name)