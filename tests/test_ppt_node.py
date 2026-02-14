from daos.nodes.ppt.create_ppt_node import CreatePPTNode

node = CreatePPTNode("CreatePPTNode")

template = r"C:\Users\sesa747199\OneDrive - Schneider Electric\1.0 Technical Support\1. Product_Category_with_Case\0. PPT Template\Case_Sample_PPT_Node.pptx"
output = r"C:\Users\sesa747199\Desktop\Case_121601668_BMEH584040_Hot Stdby Sys Issue"

result = node.run(template_path=template, output_folder=output)
print(result)