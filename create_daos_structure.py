import os

# ----------- DEFINE PROJECT STRUCTURE -----------
structure = [
    "daos/",
    "daos/core/",
    "daos/nodes/",
    "daos/nodes/ppt/",
    "daos/nodes/case_database/",
    "daos/nodes/text/",
    "daos/data/",
    "daos/data/templates/",
    "daos/data/case_files/",
    "daos/workflows/",
    "daos/utils/",
    "daos/server/",
    "tests/"
]

files = {
    # root files
    "main.py": "",
    "requirements.txt": "",
    "README.md": "# DAOS – Daoyu Autonomous Operating System\n",

    # package init files
    "daos/__init__.py": "",
    "daos/core/__init__.py": "",
    "daos/nodes/__init__.py": "",
    "daos/nodes/ppt/__init__.py": "",
    "daos/nodes/case_database/__init__.py": "",
    "daos/nodes/text/__init__.py": "",
    "daos/data/__init__.py": "",
    "daos/data/templates/__init__.py": "",
    "daos/data/case_files/__init__.py": "",
    "daos/workflows/__init__.py": "",
    "daos/utils/__init__.py": "",
    "daos/server/__init__.py": "",
    "tests/__init__.py": "",

    # core files (empty for now)
    "daos/core/node_base.py": "",
    "daos/core/workflow_engine.py": "",
    "daos/core/registry.py": "",

    # nodes (empty template files)
    "daos/nodes/ppt/create_ppt_node.py": "",
    "daos/nodes/case_database/case_db_node.py": "",
    "daos/nodes/text/summarize_node.py": "",

    # utils
    "daos/utils/file_utils.py": "",

    # workflows
    "daos/workflows/example_ppt_workflow.json": "",

    # server
    "daos/server/mcp_server.py": "",

    # tests
    "tests/test_ppt_node.py": ""
}


# ----------- CREATE FOLDERS -----------
for folder in structure:
    os.makedirs(folder, exist_ok=True)
    print(f"Created folder: {folder}")

# ----------- CREATE FILES -----------
for filepath, content in files.items():
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created file: {filepath}")

print("\n🎉 DAOS project structure created successfully!")
