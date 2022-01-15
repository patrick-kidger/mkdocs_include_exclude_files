from mkdocs import utils
from mkdocs.config.config_options import Type
from mkdocs.plugins import BasePlugin
from mkdocs.structure.files import File


__version__ = "0.0.1"


class IncludeExcludePlugin(BasePlugin):
    config_scheme = (
        ("include", Type(list, default=[])),
        ("exclude", Type(list, default=[])),
    )

    def on_files(self, files, config):
        plugin_config = config["plugins"]["include_exclude_files"].config
        for filename in plugin_config["include"]:
            files.append(
                File(
                    filename,
                    config["docs_dir"],
                    config["site_dir"],
                    config["use_directory_urls"],
                )
            )
        for to_exclude in plugin_config["exclude"]:
            for file in list(files):
                if file.src_path.startswith(to_exclude):
                    files.remove(file)
        return files
