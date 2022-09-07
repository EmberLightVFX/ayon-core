import os
from openpype.settings import get_project_settings


def create_workspace_mel(workdir, project_name):
    dst_filepath = os.path.join(workdir, "workspace.mel")
    if os.path.exists(dst_filepath):
        return

    if not os.path.exists(workdir):
        os.makedirs(workdir)

    project_setting = get_project_settings(project_name)
    mel_script = project_setting["maya"].get("mel_workspace")

    # Skip if mel script in settings is empty
    if not mel_script:
        return

    with open(dst_filepath, "w") as mel_file:
        mel_file.write(mel_script)
