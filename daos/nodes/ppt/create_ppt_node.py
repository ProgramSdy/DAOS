import os
from pptx import Presentation
from daos.core.node_base import Node


class CreatePPTNode(Node):

    def run(self, template_path, output_folder):
        """
        template_path: full path to Case_Sample_PPT_Node.pptx
        output_folder: folder where the new PPT will be created
        """

        # --- Step 1: Load template ---
        prs = Presentation(template_path)

        # --- Step 2: Extract folder name → ppt name ---
        folder_name = os.path.basename(output_folder.rstrip("\\/"))
        new_ppt_path = os.path.join(output_folder, folder_name + ".pptx")

        # --- Step 3: Extract case number + issue description ---
        # Example folder name:
        # Case_121601668_BMEH584040_Hot Stdby Sys Issue
        parts = folder_name.split("_", 2)  # split into 3 pieces max

        if len(parts) < 3:
            raise ValueError("Folder name must follow format Case_<number>_<description>")

        case_prefix = parts[0]          # "Case"
        case_number = parts[1]          # "121601668"
        issue_description = parts[2]    # "BMEH584040_Hot Stdby Sys Issue"

        full_case_number = f"{case_prefix}_{case_number}"

        # --- Step 4: Fill PPT template ---
        # Slide 1 (Cover Page)
        cover = prs.slides[0]
        for shape in cover.shapes:
            if not hasattr(shape, "text"):
                continue

            if "Presentation Title" in shape.text:
                shape.text = full_case_number

            if "Optional Subtitle" in shape.text:
                shape.text = issue_description

        # Slides 2–6 (content title)
        for slide_index in range(1, 6):  # slide 2 → slide 6
            slide = prs.slides[slide_index]
            for shape in slide.shapes:
                if hasattr(shape, "text") and "Page" in shape.text:
                    # only replace title, not footer
                    # better method → replace ONLY title placeholders
                    shape.text = issue_description

        # --- Step 5: Save new PPT ---
        prs.save(new_ppt_path)

        return {
            "output_path": new_ppt_path,
            "case_number": full_case_number,
            "issue_description": issue_description
        }
