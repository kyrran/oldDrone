import pybullet as p
import numpy as np
import os

class Drone:
    MASS: float = 1.0
    _body_centre_bottom = np.array([0, 0, -0.05], dtype=np.float32)  # Adjust as needed for your drone model

    def __init__(self, start_pos: np.ndarray) -> None:
        self.startPos = start_pos
        self.startOrientation = p.getQuaternionFromEuler([0, 0, 0])
        urdf_path = "./cf2x.urdf"

        # Check if the URDF file exists
        if not os.path.isfile(urdf_path):
            raise FileNotFoundError(f"URDF file not found: {urdf_path}")

        # Load the URDF model
        self.model = p.loadURDF(urdf_path, self.startPos, self.startOrientation)

    def movement(self) -> None:
        # Set horizontal velocity for the drone
        horizontal_velocity_x = 1.0  # velocity along the x-axis
        horizontal_velocity_y = 0.0  # velocity along the y-axis
        current_velocity, _ = p.getBaseVelocity(self.model)

        p.resetBaseVelocity(
            objectUniqueId=self.model,
            linearVelocity=[horizontal_velocity_x, horizontal_velocity_y, current_velocity[2]],
            angularVelocity=[0, 0, 0]
        )

    def apply_controls(self, upward_force: float) -> None:
        upward_force = [0, 0, upward_force]

        # Apply the given force upwards to the drone - world coordinate frame
        # i.e. upwards along the z axis
        p.applyExternalForce(objectUniqueId=self.model,
                             linkIndex=-1,
                             forceObj=upward_force,
                             posObj=[0, 0, 0],
                             flags=p.LINK_FRAME)

    def get_world_centre_bottom(self) -> np.ndarray:
        # current position of the drone
        position, _ = p.getBasePositionAndOrientation(self.model)

        # bottom centre of the drone is the centre along com minus the half height
        return np.array([position[0], position[1], position[2] - 0.05], dtype=np.float32)  # Adjust as needed

    def get_world_centre_centre(self) -> np.ndarray:
        # current position of the drone
        position, _ = p.getBasePositionAndOrientation(self.model)
        return np.array([position[0], position[1], position[2]], dtype=np.float32)

    def get_body_centre_bottom(self) -> np.ndarray:
        return self._body_centre_bottom

    def set_position(self, position: np.ndarray) -> None:
        # No change in orientation, so retrieve the current orientation
        _, current_orientation = p.getBasePositionAndOrientation(self.model)

        # Set the new position and keep the current orientation
        p.resetBasePositionAndOrientation(self.model, position, current_orientation)

    def get_full_state(self):
        pos, orn = p.getBasePositionAndOrientation(self.model)
        orn_euler = p.getEulerFromQuaternion(orn)
        return pos, orn_euler

    def get_height_above_ground(self):
        _, _, z = self.get_world_centre_bottom()
        return z
