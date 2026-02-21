import argparse
from daos.nodes.ppt.create_ppt_node import CreatePPTNode
import os

def main():
    parser = argparse.ArgumentParser(description="DAOS PPT Creator")
    parser.add_argument("folder", help="Path to the case folder where PPT should be created")
    parser.add_argument(
        "--template",
        help="Path to PPT template",
        default=r"C:\Users\sesa747199\OneDrive - Schneider Electric\1.0 Technical Support\1. Product_Category_with_Case\0. PPT Template\Case_Sample_PPT_Node.pptx"
    )
    
    args = parser.parse_args()

    node = CreatePPTNode("pptNode")
    # Expand '.' or relative path into absolute path
    output_folder = os.path.abspath(args.folder)
    result = node.run(template_path=args.template, output_folder=output_folder)

    print(f"PPT created here:\n{result['output_path']}")


if __name__ == "__main__":
    main()
