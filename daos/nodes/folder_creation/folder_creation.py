import os
from daos.core.node_base import Node

class FolderCreationNode(Node):
    """
    A node that creates an empty folder called 'From Customer'
    inside the specified case folder.
    """

    def run(self, case_folder):
        """
        case_folder: full path to the case folder (same as PPT output folder)
        Example: C:/Users/.../Case_121601668_BMEH584040_Hot Stdby Sys Issue
        """

        # Path for the new folder
        folder_name = "From Customer"
        new_folder = os.path.join(case_folder, folder_name)

        # Create the folder if it does not exist
        os.makedirs(new_folder, exist_ok=True)

        return {
            "folder_name": folder_name,
            "created": True,
            "folder_path": new_folder
        }
