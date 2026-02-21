import argparse
import os

from daos.nodes.ppt.create_ppt_node import CreatePPTNode
from daos.nodes.folder_creation.folder_creation import FolderCreationNode


def main():
    parser = argparse.ArgumentParser(description="DAOS Case Initialization Tool")
    parser.add_argument("folder", help="Path to the case folder (usually '.')")
    parser.add_argument(
        "--template",
        help="Path to PPT template",
        default=r"C:\Users\sesa747199\OneDrive - Schneider Electric\1.0 Technical Support\1. Product_Category_with_Case\0. PPT Template\Case_Sample_PPT_Node.pptx"
    )

    args = parser.parse_args()

    # resolve folder path
    case_folder = os.path.abspath(args.folder)

    # --- Step 1: Create PPT ---
    ppt_node = CreatePPTNode("pptNode")
    ppt_result = ppt_node.run(template_path=args.template, output_folder=case_folder)
    ppt_name = os.path.basename(ppt_result["output_path"])

    # --- Step 2: Create folder 'From Customer' ---
    folder_node = FolderCreationNode("folderCreationNode")
    folder_result = folder_node.run(case_folder)
    folder_name = folder_result["folder_name"]

    # --- Output summary ---
    print("\n===== DAOS Case Setup Complete =====")
    print(f"{ppt_name} is created.")
    print(f"{folder_name} folder is created.")
    print("====================================\n")


if __name__ == "__main__":
    main()
