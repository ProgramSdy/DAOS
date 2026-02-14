import sys
import os

# Add project root (one folder above /tests) to Python search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from daos.nodes.ppt.create_ppt_node import CreatePPTNode


node = CreatePPTNode("CreatePPTNode")

template = r"C:\Users\sesa747199\OneDrive - Schneider Electric\1.0 Technical Support\1. Product_Category_with_Case\0. PPT Template\Case_Sample_PPT_Node.pptx"
output = r"C:\Users\sesa747199\OneDrive - Schneider Electric\1.0 Technical Support\1. Product_Category_with_Case\1. Hardware\1. PLC\Modicon M580\Case_121601668_BMEH584040_Hot Stdby Sys Issue"

result = node.run(template_path=template, output_folder=output)
print(result)